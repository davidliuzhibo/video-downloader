#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube & Bilibili 视频下载器
使用 yt-dlp 下载视频并自动转换为 mp4 格式
"""

import os
import sys
import argparse
from pathlib import Path


def download_video(url, output_path="downloads", format_preference="best"):
    """
    下载视频并转换为mp4格式

    参数:
        url: 视频链接 (YouTube 或 Bilibili)
        output_path: 输出目录
        format_preference: 格式偏好 (best/720p/1080p等)
    """
    try:
        import yt_dlp
    except ImportError:
        print("错误: 未安装 yt-dlp，请运行: pip install yt-dlp")
        sys.exit(1)

    # 创建输出目录
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

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
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'prefer_ffmpeg': True,
        'keepvideo': False,
        'progress_hooks': [progress_hook],
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

    # 如果指定了特定分辨率
    if format_preference != 'best':
        if format_preference in ['720p', '1080p', '1440p', '2160p']:
            height = format_preference[:-1]
            ydl_opts['format'] = f'bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}]'

    print(f"开始下载: {url}")
    print(f"输出目录: {output_dir.absolute()}")
    print("-" * 60)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 获取视频信息
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'Unknown')
            print(f"视频标题: {video_title}")
            print(f"时长: {info.get('duration', 0) // 60} 分钟")
            print("-" * 60)

            # 下载视频
            ydl.download([url])

        print("\n" + "=" * 60)
        print(f"下载完成！视频已保存到: {output_dir.absolute()}")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\n下载失败: {str(e)}")
        return False


def progress_hook(d):
    """显示下载进度"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r下载进度: {percent} | 速度: {speed} | 剩余时间: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\n下载完成，正在转换为 mp4 格式...")


def main():
    parser = argparse.ArgumentParser(
        description='YouTube & Bilibili 视频下载器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python video_downloader.py <视频链接>
  python video_downloader.py <视频链接> -o my_videos
  python video_downloader.py <视频链接> -q 720p

支持的平台:
  - YouTube (youtube.com, youtu.be)
  - Bilibili (bilibili.com)
  - 以及 yt-dlp 支持的其他 1000+ 网站
        """
    )

    parser.add_argument('url', help='视频链接')
    parser.add_argument(
        '-o', '--output',
        default='downloads',
        help='输出目录 (默认: downloads)'
    )
    parser.add_argument(
        '-q', '--quality',
        default='best',
        choices=['best', '720p', '1080p', '1440p', '2160p'],
        help='视频质量 (默认: best)'
    )

    args = parser.parse_args()

    # 检查 ffmpeg
    if not check_ffmpeg():
        print("\n警告: 未检测到 ffmpeg!")
        print("请访问 https://ffmpeg.org/download.html 下载安装")
        print("或者在 Windows 上运行: winget install -e --id Gyan.FFmpeg")
        response = input("\n是否继续尝试下载? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)

    # 下载视频
    success = download_video(args.url, args.output, args.quality)
    sys.exit(0 if success else 1)


def check_ffmpeg():
    """检查 ffmpeg 是否安装"""
    import shutil

    # 首先检查系统 PATH
    if shutil.which('ffmpeg') is not None:
        return True

    # 检查本地安装路径
    local_ffmpeg = r"C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin\ffmpeg.exe"
    if os.path.exists(local_ffmpeg):
        return True

    return False


if __name__ == '__main__':
    main()
