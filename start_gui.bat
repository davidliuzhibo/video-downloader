@echo off
python video_downloader_gui.py
if %errorlevel% neq 0 (
    echo.
    echo Failed to start! Please run install.bat first.
    pause
)
