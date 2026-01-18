# 视频下载器 - YouTube & Bilibili

一个简单易用的视频下载工具，支持 YouTube、Bilibili 等 1000+ 视频网站。

## 功能特点

- ✅ 支持 YouTube 和 Bilibili 视频下载
- ✅ 自动转换为 mp4 格式
- ✅ 支持多种分辨率选择 (720p, 1080p, 4K等)
- ✅ 图形界面和命令行两种使用方式
- ✅ 下载进度实时显示
- ✅ 自动合并音视频流

## 安装步骤

### 1. 安装 Python

确保已安装 Python 3.7 或更高版本。

### 2. 安装 yt-dlp

```bash
pip install yt-dlp
```

### 3. 安装 ffmpeg

#### Windows:

**方法一: 使用 winget (推荐)**
```bash
winget install -e --id Gyan.FFmpeg
```

**方法二: 手动安装**
1. 访问 https://ffmpeg.org/download.html
2. 下载 Windows 版本
3. 解压到任意目录 (例如: `C:\ffmpeg`)
4. 将 `C:\ffmpeg\bin` 添加到系统环境变量 PATH

#### macOS:

```bash
brew install ffmpeg
```

#### Linux:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

### 4. 验证安装

```bash
# 检查 yt-dlp
yt-dlp --version

# 检查 ffmpeg
ffmpeg -version
```

## 使用方法

### 图形界面版本 (推荐)

运行图形界面程序:

```bash
python video_downloader_gui.py
```

操作步骤:
1. 粘贴视频链接到"视频链接"输入框
2. 选择保存位置
3. 选择视频质量
4. 点击"开始下载"

![GUI截图](gui_screenshot.png)

### 命令行版本

基本用法:

```bash
python video_downloader.py <视频链接>
```

指定输出目录:

```bash
python video_downloader.py <视频链接> -o my_videos
```

指定视频质量:

```bash
python video_downloader.py <视频链接> -q 720p
```

查看帮助:

```bash
python video_downloader.py --help
```

## 使用示例

### YouTube 视频下载

```bash
# 下载最高质量
python video_downloader.py https://www.youtube.com/watch?v=xxxxx

# 下载 720p
python video_downloader.py https://www.youtube.com/watch?v=xxxxx -q 720p

# 指定保存目录
python video_downloader.py https://www.youtube.com/watch?v=xxxxx -o C:\Videos
```

### Bilibili 视频下载

```bash
python video_downloader.py https://www.bilibili.com/video/BVxxxxx
```

### 其他支持的网站

yt-dlp 支持 1000+ 视频网站，包括:
- YouTube
- Bilibili
- Twitter
- Facebook
- Instagram
- TikTok
- Vimeo
- 等等...

完整列表: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## 常见问题

### Q: 下载速度慢怎么办？

A: 这通常是网络问题。可以尝试:
- 使用代理
- 选择较低分辨率
- 避开高峰时段

### Q: 下载失败提示 ffmpeg 错误？

A: 请确保:
1. ffmpeg 已正确安装
2. ffmpeg 在系统 PATH 中
3. 重启终端/命令提示符

### Q: 能下载整个播放列表吗？

A: 可以！直接使用播放列表链接:

```bash
python video_downloader.py https://www.youtube.com/playlist?list=xxxxx
```

### Q: 如何只下载音频？

A: 修改 `video_downloader.py` 中的 `format` 选项为 `bestaudio`。

## 技术细节

- **下载引擎**: yt-dlp (youtube-dl 的增强版)
- **视频处理**: ffmpeg
- **界面框架**: tkinter (Python 内置)
- **输出格式**: mp4 (自动合并音视频)

## 注意事项

1. ⚠️ 请尊重版权，仅下载您有权下载的内容
2. ⚠️ 某些网站可能有下载限制
3. ⚠️ 建议不要频繁大量下载，可能会被封IP

## 更新日志

### v1.0.0 (2026-01-18)
- 初始版本发布
- 支持 YouTube 和 Bilibili
- 图形界面和命令行版本
- 自动转换为 mp4 格式

## 贡献

欢迎提交 Issue 和 Pull Request!

## 许可证

MIT License

## 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [ffmpeg](https://ffmpeg.org/) - 多媒体处理工具
