@echo off
chcp 65001 >nul
echo ===============================================
echo    FFmpeg 手动安装指南
echo ===============================================
echo.
echo 由于自动安装失败，请按照以下步骤手动安装 ffmpeg：
echo.
echo 步骤 1: 下载 ffmpeg
echo ----------------------------------------
echo 1. 打开浏览器，访问以下网址：
echo    https://github.com/BtbN/FFmpeg-Builds/releases
echo.
echo 2. 找到最新的 release，下载文件名类似：
echo    ffmpeg-master-latest-win64-gpl.zip
echo.
echo.
echo 步骤 2: 解压文件
echo ----------------------------------------
echo 1. 下载完成后，解压 zip 文件
echo 2. 将解压后的文件夹重命名为 "ffmpeg"
echo 3. 移动到 C:\ 目录，最终路径应该是：
echo    C:\ffmpeg
echo.
echo.
echo 步骤 3: 添加到系统 PATH
echo ----------------------------------------
echo 1. 右键点击"此电脑"或"我的电脑"
echo 2. 选择"属性"
echo 3. 点击"高级系统设置"
echo 4. 点击"环境变量"
echo 5. 在"系统变量"中找到"Path"，双击
echo 6. 点击"新建"，添加：
echo    C:\ffmpeg\bin
echo 7. 点击"确定"保存所有设置
echo.
echo.
echo 步骤 4: 验证安装
echo ----------------------------------------
echo 1. 关闭当前所有命令提示符窗口
echo 2. 重新打开命令提示符
echo 3. 输入命令: ffmpeg -version
echo 4. 如果显示版本信息，说明安装成功！
echo.
echo.
echo ===============================================
echo    快速链接
echo ===============================================
echo.
echo FFmpeg 官方下载页面:
echo https://ffmpeg.org/download.html
echo.
echo Windows 构建版本 (推荐):
echo https://github.com/BtbN/FFmpeg-Builds/releases
echo.
echo 视频教程搜索关键词:
echo "Windows 安装 ffmpeg"
echo.
echo ===============================================
echo.
pause
