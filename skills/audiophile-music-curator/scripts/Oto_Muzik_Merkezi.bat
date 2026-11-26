@echo off
title Evrensel Oto Muzik ve USB Yonetim Merkezi
color 0B
chcp 65001 >nul
cls

:: 1. Python Varligini Kontrol Et
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Python bulunamadi! Lutfen sisteminizde Python kurulu oldugundan emin olun.
    echo Indirmek icin: https://www.python.org/downloads/
    echo.
    pause
    exit /b
)

:: 2. Bagimlilik Kontrolu (Gerekirse otomatik kurar)
python -c "import mutagen, PIL" 2>nul
if %errorlevel% neq 0 (
    echo [KURULUM] Gerekli Python kutuphaneleri eksik, kuruluyor...
    python -m pip install mutagen Pillow yt-dlp
)

:: 3. Universal Car Audio Station Baslat
set SCRIPT_DIR=%~dp0
if exist "%SCRIPT_DIR%scripts\car_audio_station.py" (
    python "%SCRIPT_DIR%scripts\car_audio_station.py"
) else if exist "%SCRIPT_DIR%car_audio_station.py" (
    python "%SCRIPT_DIR%car_audio_station.py"
) else if exist "C:\Users\MrCoolice\Nextcloud\Music\car_audio_station.py" (
    python "C:\Users\MrCoolice\Nextcloud\Music\car_audio_station.py"
) else (
    echo [HATA] car_audio_station.py dosyasi bulunamadi!
    pause
)
