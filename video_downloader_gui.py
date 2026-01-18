#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube & Bilibili 视频下载器 - GUI版本
使用 yt-dlp 下载视频并自动转换为 mp4 格式
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import threading
import os
import re
from pathlib import Path


class VideoDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("视频下载器 - YouTube & Bilibili")
        self.root.geometry("700x550")
        self.root.resizable(True, True)

        # 检查依赖
        self.check_dependencies()

        # 创建界面
        self.create_widgets()

        # 下载线程
        self.download_thread = None
        self.is_downloading = False

    @staticmethod
    def remove_ansi_codes(text):
        """移除 ANSI 颜色代码和控制字符"""
        # 移除 ANSI escape sequences
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def check_dependencies(self):
        """检查必要的依赖"""
        try:
            import yt_dlp
        except ImportError:
            messagebox.showerror(
                "缺少依赖",
                "未安装 yt-dlp！\n\n请在命令行运行:\npip install yt-dlp"
            )

        import shutil
        # 检查系统 PATH 或本地安装
        local_ffmpeg = r"C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin\ffmpeg.exe"
        if not shutil.which('ffmpeg') and not os.path.exists(local_ffmpeg):
            messagebox.showwarning(
                "缺少 ffmpeg",
                "未检测到 ffmpeg！\n\n"
                "请访问 https://ffmpeg.org/download.html\n"
                "或在 Windows 上运行:\nwinget install -e --id Gyan.FFmpeg"
            )

    def create_widgets(self):
        """创建界面组件"""
        # 样式
        style = ttk.Style()
        style.theme_use('clam')

        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="视频下载器",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # 视频链接
        ttk.Label(main_frame, text="视频链接:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)

        # 输出目录
        ttk.Label(main_frame, text="保存位置:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_entry = ttk.Entry(main_frame, width=50)
        self.output_entry.insert(0, str(Path.cwd() / "downloads"))
        self.output_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)

        browse_btn = ttk.Button(main_frame, text="浏览", command=self.browse_folder)
        browse_btn.grid(row=2, column=2, pady=5, padx=5)

        # 视频质量
        ttk.Label(main_frame, text="视频质量:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.quality_var = tk.StringVar(value='best')
        quality_combo = ttk.Combobox(
            main_frame,
            textvariable=self.quality_var,
            values=['best', '2160p (4K)', '1440p', '1080p', '720p'],
            state='readonly',
            width=20
        )
        quality_combo.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)

        # 下载按钮
        self.download_btn = ttk.Button(
            main_frame,
            text="开始下载",
            command=self.start_download,
            style='Accent.TButton'
        )
        self.download_btn.grid(row=4, column=0, columnspan=3, pady=15)

        # 进度条
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=600
        )
        self.progress.grid(row=5, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))

        # 日志输出
        ttk.Label(main_frame, text="下载日志:").grid(row=6, column=0, columnspan=3, sticky=tk.W, pady=(10, 5))
        self.log_text = scrolledtext.ScrolledText(
            main_frame,
            width=70,
            height=15,
            wrap=tk.WORD,
            font=('Consolas', 9)
        )
        self.log_text.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        main_frame.rowconfigure(7, weight=1)

    def browse_folder(self):
        """选择保存文件夹"""
        folder = filedialog.askdirectory()
        if folder:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder)

    def log(self, message):
        """添加日志"""
        # 清理 ANSI 颜色代码
        clean_message = self.remove_ansi_codes(str(message))
        self.log_text.insert(tk.END, clean_message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def start_download(self):
        """开始下载"""
        if self.is_downloading:
            messagebox.showinfo("提示", "正在下载中，请稍候...")
            return

        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("错误", "请输入视频链接！")
            return

        output_path = self.output_entry.get().strip()
        if not output_path:
            messagebox.showerror("错误", "请选择保存位置！")
            return

        # 清空日志
        self.log_text.delete(1.0, tk.END)

        # 禁用按钮
        self.download_btn.config(state='disabled', text="Downloading...")
        self.progress.start()
        self.is_downloading = True

        # 在新线程中下载
        self.download_thread = threading.Thread(
            target=self.download_video,
            args=(url, output_path),
            daemon=True
        )
        self.download_thread.start()

    def download_video(self, url, output_path):
        """下载视频（在后台线程中运行）"""
        try:
            import yt_dlp

            # 创建输出目录
            output_dir = Path(output_path)
            output_dir.mkdir(parents=True, exist_ok=True)

            # 获取质量设置
            quality = self.quality_var.get()
            if quality == 'best':
                format_str = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            else:
                height = quality.split()[0][:-1]  # 移除 'p'
                format_str = f'bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}]'

            # 配置 ffmpeg 路径
            import shutil
            ffmpeg_location = None
            local_ffmpeg_dir = r"C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin"

            if shutil.which('ffmpeg'):
                # 系统 PATH 中有 ffmpeg
                pass
            elif os.path.exists(os.path.join(local_ffmpeg_dir, 'ffmpeg.exe')):
                # 使用本地 ffmpeg
                ffmpeg_location = local_ffmpeg_dir

            # 配置下载选项
            ydl_opts = {
                'format': format_str,
                'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'prefer_ffmpeg': True,
                'keepvideo': False,
                'progress_hooks': [self.progress_hook],
                # 添加网络和 SSL 相关选项
                'nocheckcertificate': True,  # 跳过 SSL 证书验证
                'socket_timeout': 30,  # 设置超时时间
                'retries': 10,  # 重试次数
                'fragment_retries': 10,  # 片段重试次数
                'extractor_retries': 3,  # 提取器重试次数
            }

            # 如果找到了本地 ffmpeg，添加到配置中
            if ffmpeg_location:
                ydl_opts['ffmpeg_location'] = ffmpeg_location

            self.log(f"视频链接: {url}")
            self.log(f"保存位置: {output_dir.absolute()}")
            self.log("-" * 60)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # 获取视频信息
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)

                self.log(f"视频标题: {video_title}")
                self.log(f"时长: {duration // 60} 分 {duration % 60} 秒")
                self.log("-" * 60)

                # 下载视频
                ydl.download([url])

            self.log("=" * 60)
            self.log("下载完成！")
            self.log("=" * 60)

            # 显示成功消息
            self.root.after(0, lambda: messagebox.showinfo(
                "完成",
                f"视频下载完成！\n\n保存位置:\n{output_dir.absolute()}"
            ))

        except Exception as e:
            error_msg = f"下载失败: {str(e)}"
            self.log(error_msg)
            self.root.after(0, lambda: messagebox.showerror("错误", error_msg))

        finally:
            # 恢复按钮状态
            self.root.after(0, self.finish_download)

    def progress_hook(self, d):
        """下载进度回调"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')

            # 清理 ANSI 颜色代码
            percent = self.remove_ansi_codes(str(percent))
            speed = self.remove_ansi_codes(str(speed))
            eta = self.remove_ansi_codes(str(eta))

            msg = f"下载进度: {percent} | 速度: {speed} | 剩余: {eta}"
            # 更新最后一行
            self.root.after(0, lambda: self.update_last_log(msg))
        elif d['status'] == 'finished':
            self.log("下载完成，正在转换为 mp4 格式...")

    def update_last_log(self, message):
        """更新日志最后一行"""
        # 删除最后一行
        self.log_text.delete("end-2l", "end-1l")
        # 添加新消息
        self.log(message)

    def finish_download(self):
        """完成下载"""
        self.progress.stop()
        self.download_btn.config(state='normal', text="开始下载")
        self.is_downloading = False


def main():
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
