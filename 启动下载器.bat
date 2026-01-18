@echo off
chcp 65001 >nul
echo 启动视频下载器（图形界面）...
python video_downloader_gui.py
if %errorlevel% neq 0 (
    echo.
    echo 启动失败！请确保已运行 install.bat 安装依赖。
    pause
)
