@echo off
:: ======================================================
:: 📱 DVFB - Dịch Vụ Facebook Git Tool
:: Copyright By Từ Quang Nam
:: Version: 1.0.0
:: ======================================================

:: Bật ANSI escape code
for /f "tokens=2 delims=: " %%a in ('reg query HKEY_CURRENT_USER\Console 2^>nul ^| find "VirtualTerminalLevel"') do set vt=%%a
if not defined vt (
    reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1
)

:: Định nghĩa màu (ANSI)
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "CYAN=[96m"
set "MAGENTA=[95m"
set "RESET=[0m"

:: Chuyển CMD sang UTF-8
chcp 65001 >nul
cls
echo =====================================================
echo %MAGENTA% 📱 DVFB - DỊCH VỤ FACEBOOK GIT TOOL %RESET%
echo ---------------------------------
echo %YELLOW% Copyright By Từ Quang Nam %RESET%
echo %YELLOW% Version: 1.0.0 %RESET%
echo =====================================================
echo.

:: [1/5] Check trạng thái
echo %BLUE%[1/5] Đang kiểm tra trạng thái Git...%RESET%
git status
if errorlevel 1 (
    echo %RED%❌ Không phải thư mục Git hoặc Git chưa cài đặt!%RESET%
    echo.
    pause
    exit /b 1
)
echo.

set /p choice=❓ %YELLOW%Bạn có muốn tiếp tục commit + push không? (Y/N): %RESET%
if /I "%choice%" NEQ "Y" (
    echo %RED%❌ Đã huỷ thao tác.%RESET%
    echo.
    pause
    exit /b 0
)

:: [2/5] Auto tạo commit message
setlocal enabledelayedexpansion

:: File lưu số lần commit
set "counterFile=dvfb-commit-counter.txt"
if not exist "%counterFile%" (
    echo 0 > "%counterFile%"
)

:: Đọc số commit
set /p commitCount=<"%counterFile%"
set /a commitCount+=1
echo !commitCount! > "%counterFile%"

:: Lấy ngày giờ định dạng đẹp
for /f "tokens=1-3 delims=/" %%a in ('date /t') do (
    set ngay=%%a-%%b-%%c
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set gio=%%a:%%b
)

set "commitMsg=DVFB - Commit #!commitCount! - !ngay! !gio!"

echo %BLUE%[2/5] Tin nhắn commit tự động:%RESET%
echo    %GREEN%"!commitMsg!"%RESET%
echo.

:: [3/5] Add file
echo %BLUE%[3/5] Đang thêm files...%RESET%
git add .
if errorlevel 1 (
    echo %RED%❌ Lỗi khi thêm files!%RESET%
    echo.
    pause
    exit /b 1
)
echo.

:: [4/5] Commit
echo %BLUE%[4/5] Đang commit...%RESET%
git commit -m "!commitMsg!"
if errorlevel 1 (
    echo %YELLOW%⚠  Không có thay đổi để commit hoặc lỗi!%RESET%
    echo.
)

:: [5/5] Push
echo %BLUE%[5/5] Đang đẩy code lên GitHub...%RESET%
git push origin main
if errorlevel 1 (
    echo %YELLOW%⚠  Đang thử push với force...%RESET%
    git push -f origin main
    if errorlevel 1 (
        echo %RED%❌ Push thất bại!%RESET%
        echo %YELLOW%💡 Kiểm tra kết nối internet và quyền truy cập GitHub%RESET%
        echo.
        pause
        exit /b 1
    )
)

:: Ghi log
echo [!date! !time!] !commitMsg! >> dvfb-commit-history.txt

:: Thông báo thành công
echo.
echo =====================================================
echo %GREEN%✅ Đẩy code thành công!%RESET%
echo %CYAN%📂 Log đã lưu vào dvfb-commit-history.txt%RESET%
echo %CYAN%📊 Tổng số commit DVFB: !commitCount!%RESET%
echo %MAGENTA%🌐 Repository: https://github.com/tuquangnam07/DVFB%RESET%
echo =====================================================
echo.

:: Mở repository trên trình duyệt
echo %YELLOW%🚀 Đang mở repository trên GitHub...%RESET%
start https://github.com/tuquangnam07/DVFB

:: Tạo khoảng trống trước khi đóng tool
echo.
echo.
echo %GREEN%Nhấn phím bất kỳ để đóng tool...%RESET%
pause >nul
exit /b 0