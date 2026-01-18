@echo off
echo Video Downloader for YouTube and Bilibili
echo.
if "%~1"=="" (
    echo Usage: start_download.bat [video_url]
    echo Example: start_download.bat https://www.youtube.com/watch?v=xxxxx
    echo.
    pause
    exit /b 1
)

python video_downloader.py %*
pause
