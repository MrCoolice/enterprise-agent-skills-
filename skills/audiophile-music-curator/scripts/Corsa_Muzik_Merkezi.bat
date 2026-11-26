@echo off
title Oto Muzik ve USB Yonetim Merkezi
color 0B
chcp 65001 >nul
cls

:: Python varligini dogrula
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Python bulunamadi! Lutfen sisteminizde Python kurulu oldugundan emin olun.
    echo.
    pause
    exit /b
)

:: Car Audio Station v3.0 calistir
set SCRIPT_DIR=%~dp0
if exist "%SCRIPT_DIR%scripts\car_audio_station.py" (
    python "%SCRIPT_DIR%scripts\car_audio_station.py"
) else if exist "%SCRIPT_DIR%car_audio_station.py" (
    python "%SCRIPT_DIR%car_audio_station.py"
) else if exist "C:\Users\MrCoolice\Nextcloud\Music\car_audio_station.py" (
    python "C:\Users\MrCoolice\Nextcloud\Music\car_audio_station.py"
) else if exist "C:\Users\MrCoolice\Nextcloud\Music\corsa_station.py" (
    python "C:\Users\MrCoolice\Nextcloud\Music\corsa_station.py"
) else (
    echo [HATA] Muzik merkezi dosyasi bulunamadi!
    pause
)
