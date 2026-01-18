@echo off
chcp 65001 >nul
echo ===============================================
echo    添加 ffmpeg 到系统 PATH
echo ===============================================
echo.
echo 检测到 ffmpeg 位置：
echo C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin
echo.
echo 正在测试 ffmpeg...
"C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin\ffmpeg.exe" -version | findstr "version"
echo.
echo.

REM 添加到用户 PATH（不需要管理员权限）
echo 正在添加到用户环境变量 PATH...
setx PATH "%PATH%;C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin"

if %errorlevel% equ 0 (
    echo.
    echo ✅ 成功添加到 PATH！
    echo.
    echo ⚠️  重要提示：
    echo    1. 请关闭当前所有命令提示符窗口
    echo    2. 重新打开命令提示符
    echo    3. 输入 "ffmpeg -version" 验证安装
    echo.
    echo 或者，你现在可以直接双击运行：启动下载器.bat
) else (
    echo.
    echo ❌ 自动添加失败
    echo.
    echo 请手动添加：
    echo 1. 右键"此电脑" - "属性"
    echo 2. "高级系统设置" - "环境变量"
    echo 3. 在"用户变量"中找到"Path"，双击
    echo 4. 点击"新建"，添加以下路径：
    echo    C:\Private\Software\ffmpeg-2026-01-14-git-6c878f8b82-full_build\bin
    echo 5. 确定保存
)

echo.
echo ===============================================
pause
