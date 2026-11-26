@echo off
title Opel Corsa Muzik ve USB Yonetim Merkezi
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

:: Corsa Station interaktif uygulamasini baslat
python "%~dp0corsa_station.py"

