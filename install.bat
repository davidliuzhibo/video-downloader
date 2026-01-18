@echo off
chcp 65001 >nul
echo ===============================================
echo    视频下载器 - 安装脚本
echo ===============================================
echo.

REM 检查 Python
echo [1/3] 检查 Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未检测到 Python！
    echo    请从 https://www.python.org/downloads/ 下载安装
    pause
    exit /b 1
)
python --version
echo ✅ Python 已安装
echo.

REM 安装 yt-dlp
echo [2/3] 安装 yt-dlp...
pip install yt-dlp --upgrade
if %errorlevel% neq 0 (
    echo ❌ yt-dlp 安装失败
    pause
    exit /b 1
)
echo ✅ yt-dlp 安装成功
echo.

REM 检查并安装 ffmpeg
echo [3/3] 检查 ffmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ ffmpeg 已安装
    ffmpeg -version | findstr "version"
) else (
    echo ⚠️  未检测到 ffmpeg
    echo.
    echo 正在尝试通过 winget 安装 ffmpeg...
    winget install -e --id Gyan.FFmpeg
    if %errorlevel% neq 0 (
        echo.
        echo ⚠️  自动安装失败，请手动安装 ffmpeg：
        echo    1. 访问 https://ffmpeg.org/download.html
        echo    2. 下载 Windows 版本
        echo    3. 解压到 C:\ffmpeg
        echo    4. 将 C:\ffmpeg\bin 添加到系统 PATH
        echo.
        echo 或者运行以下命令：
        echo    winget install -e --id Gyan.FFmpeg
    ) else (
        echo ✅ ffmpeg 安装成功
        echo ⚠️  请重新打开命令提示符以使 PATH 生效
    )
)

echo.
echo ===============================================
echo    安装完成！
echo ===============================================
echo.
echo 使用方法：
echo    图形界面: python video_downloader_gui.py
echo    命令行:   python video_downloader.py [视频链接]
echo.
pause
