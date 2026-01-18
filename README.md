# 视频下载器 - YouTube & Bilibili Video Downloader

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

一个简单易用的视频下载工具，支持 YouTube、Bilibili、Twitter 等 1000+ 视频网站。

[功能特点](#功能特点) • [快速开始](#快速开始) • [使用方法](#使用方法) • [常见问题](#常见问题) • [项目文档](#项目文档)

</div>

---

## 📖 项目简介

这是一个使用 Python 开发的跨平台视频下载工具，基于强大的 yt-dlp 引擎，提供友好的图形界面和灵活的命令行两种使用方式。无论你是普通用户还是开发者，都能轻松下载喜欢的视频。

**开发时间：** 2026年1月18日
**开发方式：** Claude Code 辅助开发
**测试状态：** ✅ YouTube、Bilibili、Twitter 全部测试通过

## ✨ 功能特点

- 🌍 **支持 1000+ 网站** - YouTube、Bilibili、Twitter、Facebook、Instagram、TikTok 等
- 🎨 **双模式使用** - 图形界面（GUI）+ 命令行（CLI）
- 🎬 **自动格式转换** - 自动转换为 mp4 格式，兼容性最好
- 🎯 **多分辨率选择** - 支持 720p、1080p、1440p、4K 等
- 📊 **实时进度显示** - 清晰的下载进度和速度提示
- 🔧 **智能错误处理** - 网络错误自动重试，SSL 问题自动处理
- 🎵 **音视频合并** - 自动合并分离的音视频流
- 💾 **智能路径检测** - 自动检测并使用本地 ffmpeg

## 🚀 快速开始

### 方式一：使用预配置脚本（Windows 推荐）

1. **克隆项目**
   ```bash
   git clone https://github.com/davidliuzhibo/video-downloader.git
   cd video-downloader
   ```

2. **运行安装脚本**
   - 双击 `install.bat` 自动安装依赖

3. **启动程序**
   - 双击 `start_gui.bat` 启动图形界面
   - 或运行 `python video_downloader_gui.py`

### 方式二：手动安装

#### 1. 安装 Python

确保已安装 Python 3.7 或更高版本：
```bash
python --version
```

#### 2. 安装 yt-dlp

```bash
pip install yt-dlp
```

#### 3. 安装 ffmpeg

**Windows:**
```bash
# 使用 winget (推荐)
winget install -e --id Gyan.FFmpeg

# 或从官网下载：https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

#### 4. 验证安装

```bash
yt-dlp --version
ffmpeg -version
```

## 📱 使用方法

### 图形界面版本（推荐新手）

1. **启动程序**
   ```bash
   python video_downloader_gui.py
   ```
   或双击 `start_gui.bat`（Windows）

2. **操作步骤**
   - 粘贴视频链接到"视频链接"输入框
   - 选择保存位置（默认为 downloads 文件夹）
   - 选择视频质量（best/720p/1080p/1440p/2160p）
   - 点击"开始下载"按钮

3. **查看进度**
   - 实时查看下载进度、速度和剩余时间
   - 下载完成后自动转换为 mp4 格式

### 命令行版本（推荐进阶用户）

**基本用法：**
```bash
python video_downloader.py <视频链接>
```

**指定输出目录：**
```bash
python video_downloader.py <视频链接> -o D:\MyVideos
```

**指定视频质量：**
```bash
python video_downloader.py <视频链接> -q 1080p
```

**完整示例：**
```bash
python video_downloader.py https://www.youtube.com/watch?v=xxxxx -o D:\Videos -q 720p
```

**查看帮助：**
```bash
python video_downloader.py --help
```

## 🌐 支持的网站

### 主要支持（已测试）

| 网站 | 状态 | 说明 |
|------|------|------|
| YouTube | ✅ | 完全支持，包括播放列表 |
| Bilibili | ✅ | 完全支持 |
| Twitter | ✅ | 完全支持 |
| Facebook | ✅ | 支持 |
| Instagram | ✅ | 支持 |
| TikTok | ✅ | 支持 |

### 其他支持的网站

yt-dlp 支持 1000+ 视频网站，包括但不限于：
- Vimeo、Dailymotion
- Reddit、Tumblr
- Twitch、StreamTV
- 各种新闻网站
- 教育平台

**完整列表：** https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## 🎯 使用示例

### 下载 YouTube 视频
```bash
# 下载最高质量
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

# 下载 720p
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -q 720p

# 指定保存目录
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -o C:\Videos
```

### 下载 Bilibili 视频
```bash
python video_downloader.py https://www.bilibili.com/video/BV1xx411c7mu
```

### 下载 Twitter 视频
```bash
python video_downloader.py https://twitter.com/user/status/1234567890
```

### 下载播放列表
```bash
python video_downloader.py https://www.youtube.com/playlist?list=PLxxxxxx
```

## 💡 常见问题

<details>
<summary><b>Q: 下载速度慢怎么办？</b></summary>

**A:** 这通常是网络问题。可以尝试：
- 选择较低分辨率（如 720p 而不是 4K）
- 避开网络高峰时段
- 检查网络连接是否稳定
- 考虑使用代理（如果网络有限制）
</details>

<details>
<summary><b>Q: YouTube 下载出现 SSL 错误怎么办？</b></summary>

**A:** 程序已内置解决方案：
- 自动跳过 SSL 证书验证
- 自动重试机制（最多10次）
- 如果仍然失败，请检查网络环境
- 详见 `YouTube下载问题说明.md`
</details>

<details>
<summary><b>Q: 下载失败提示 ffmpeg 错误？</b></summary>

**A:** 请确保：
1. ffmpeg 已正确安装
2. ffmpeg 在系统 PATH 中（运行 `ffmpeg -version` 验证）
3. 重启终端/命令提示符
4. 查看 `ffmpeg安装指南.bat` 获取详细安装步骤
</details>

<details>
<summary><b>Q: 能下载整个播放列表吗？</b></summary>

**A:** 可以！直接使用播放列表链接：
```bash
python video_downloader.py https://www.youtube.com/playlist?list=xxxxx
```
程序会自动下载播放列表中的所有视频。
</details>

<details>
<summary><b>Q: 如何只下载音频？</b></summary>

**A:** 修改 `video_downloader.py` 中的配置：
```python
'format': 'bestaudio/best'
```
或者使用专门的音频下载工具如 `yt-dlp` 命令行。
</details>

<details>
<summary><b>Q: 界面出现乱码怎么办？</b></summary>

**A:** 乱码问题已在最新版本修复：
- ANSI 颜色代码已自动清理
- 按钮文字使用英文避免编码问题
- 如果仍有问题，请重新下载最新版本
</details>

## 📚 项目文档

| 文档 | 说明 |
|------|------|
| [README.md](README.md) | 项目说明（本文档） |
| [使用指南.md](使用指南.md) | 详细使用教程 |
| [项目开发历程.md](项目开发历程.md) | 完整开发过程记录 |
| [YouTube下载问题说明.md](YouTube下载问题说明.md) | YouTube 问题排查 |
| [更新日志.md](更新日志.md) | 版本更新记录 |
| [安装完成.md](安装完成.md) | 安装完成确认 |
| [启动说明.txt](启动说明.txt) | 快速启动指南 |

## 🔧 技术细节

### 技术栈
- **Python 3.7+** - 编程语言
- **yt-dlp** - 视频下载引擎（youtube-dl 的增强版）
- **ffmpeg** - 视频处理和格式转换
- **tkinter** - Python 内置 GUI 框架

### 核心功能
- 自动合并音视频流
- 智能 ffmpeg 路径检测
- ANSI 颜色代码清理
- 网络错误自动重试
- SSL 证书问题处理

### 项目结构
```
video-downloader/
├── video_downloader.py         # 命令行版本
├── video_downloader_gui.py     # GUI 版本
├── start_gui.bat               # GUI 启动脚本
├── start_download.bat          # CLI 启动脚本
├── install.bat                 # 安装脚本
├── requirements.txt            # Python 依赖
├── .gitignore                  # Git 忽略配置
└── docs/                       # 文档目录
```

## 📊 测试报告

### 测试环境
- **操作系统：** Windows
- **Python 版本：** 3.13
- **yt-dlp 版本：** 2025.12.8
- **ffmpeg 版本：** 2026-01-14

### 测试结果

| 功能 | 状态 |
|------|------|
| YouTube 视频下载 | ✅ 通过 |
| Bilibili 视频下载 | ✅ 通过 |
| Twitter 视频下载 | ✅ 通过 |
| 音视频合并 | ✅ 通过 |
| mp4 格式转换 | ✅ 通过 |
| 进度实时显示 | ✅ 通过 |
| 错误自动重试 | ✅ 通过 |
| 多分辨率下载 | ✅ 通过 |
| GUI 界面 | ✅ 通过 |
| 命令行工具 | ✅ 通过 |

## ⚠️ 注意事项

1. **版权声明**
   - 请尊重版权，仅下载您有权下载的内容
   - 不要用于商业目的
   - 遵守各平台的服务条款

2. **使用限制**
   - 某些网站可能有下载限制
   - 建议不要频繁大量下载，可能会被限速或封IP
   - 部分地区访问某些网站可能需要特殊网络环境

3. **安全提示**
   - 本工具跳过了 SSL 证书验证以解决网络问题
   - 仅用于下载公开视频，安全风险可控
   - 不建议在企业或敏感环境中使用

## 🎯 未来计划

### v1.1（计划中）
- [ ] 添加下载队列功能
- [ ] 支持播放列表批量下载
- [ ] 添加下载历史记录
- [ ] 优化界面布局和样式

### v1.2（计划中）
- [ ] 添加代理设置选项
- [ ] 支持视频预览
- [ ] 添加字幕下载功能
- [ ] 创建独立可执行文件（exe）

### v2.0（远期规划）
- [ ] 支持更多视频网站的特殊功能
- [ ] 添加简单的视频编辑功能
- [ ] 支持云同步配置
- [ ] 多语言界面支持

## 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

1. Fork 本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📝 更新日志

### v1.0.0 (2026-01-18)
- ✨ 初始版本发布
- ✅ 支持 YouTube、Bilibili、Twitter
- ✅ 图形界面和命令行版本
- ✅ 自动转换为 mp4 格式
- ✅ 修复 SSL 错误和 ANSI 乱码问题
- ✅ 智能 ffmpeg 检测

详细更新日志请查看 [更新日志.md](更新日志.md)

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

这意味着你可以自由地：
- ✅ 使用本项目
- ✅ 复制、修改本项目
- ✅ 分发本项目
- ✅ 用于商业目的

只需保留版权声明即可。

## 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [ffmpeg](https://ffmpeg.org/) - 多媒体处理的瑞士军刀
- [Python](https://www.python.org/) - 优雅的编程语言
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI 框架
- [Claude Code](https://claude.ai/code) - AI 辅助开发工具

## 📬 联系方式

- **GitHub Issues:** https://github.com/davidliuzhibo/video-downloader/issues
- **项目主页:** https://github.com/davidliuzhibo/video-downloader

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️ Star 支持一下！**

Made with ❤️ by [davidliuzhibo](https://github.com/davidliuzhibo) & [Claude Code](https://claude.ai/code)

</div>
