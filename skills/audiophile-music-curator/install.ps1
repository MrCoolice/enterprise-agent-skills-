# ==============================================================================
# Universal Car Audio Station (Oto Muzik Merkezi) - 1-Click Standalone Installer
# ==============================================================================
# Usage in PowerShell:
#   irm https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/audiophile-music-curator/install.ps1 | iex
# ==============================================================================

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "  EVRENSEL OTO MUZIK MERKEZI (UNIVERSAL CAR AUDIO STATION v3.0)" -ForegroundColor Cyan
Write-Host "  1-Tikla Otomatik Kurulum ve Baslatici" -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan

# Hedef Klasor: Kullanicinin Muzik klasoru altinda Oto-Muzik-Merkezi
$TargetDir = Join-Path ([Environment]::GetFolderPath("MyMusic")) "Oto-Muzik-Merkezi"
if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}
$ScriptsDir = Join-Path $TargetDir "scripts"
if (-not (Test-Path $ScriptsDir)) {
    New-Item -ItemType Directory -Path $ScriptsDir -Force | Out-Null
}

$BaseRawUrl = "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/audiophile-music-curator"

$Files = @(
    @{ Remote = "$BaseRawUrl/requirements.txt"; Local = (Join-Path $TargetDir "requirements.txt") },
    @{ Remote = "$BaseRawUrl/README.md"; Local = (Join-Path $TargetDir "README.md") },
    @{ Remote = "$BaseRawUrl/scripts/car_audio_station.py"; Local = (Join-Path $ScriptsDir "car_audio_station.py") },
    @{ Remote = "$BaseRawUrl/scripts/bootstrap.py"; Local = (Join-Path $ScriptsDir "bootstrap.py") },
    @{ Remote = "$BaseRawUrl/scripts/library_config.py"; Local = (Join-Path $ScriptsDir "library_config.py") },
    @{ Remote = "$BaseRawUrl/scripts/audit_library.py"; Local = (Join-Path $ScriptsDir "audit_library.py") },
    @{ Remote = "$BaseRawUrl/scripts/normalize_audio.py"; Local = (Join-Path $ScriptsDir "normalize_audio.py") },
    @{ Remote = "$BaseRawUrl/scripts/embed_metadata.py"; Local = (Join-Path $ScriptsDir "embed_metadata.py") },
    @{ Remote = "$BaseRawUrl/scripts/sync_usb.py"; Local = (Join-Path $ScriptsDir "sync_usb.py") },
    @{ Remote = "$BaseRawUrl/scripts/Oto_Muzik_Merkezi.bat"; Local = (Join-Path $TargetDir "Oto_Muzik_Merkezi.bat") }
)

Write-Host "`n[1/3] En guncel dosyalar GitHub'dan indiriliyor..." -ForegroundColor Yellow
foreach ($f in $Files) {
    $fn = Split-Path $f.Local -Leaf
    Write-Host "  -> Indiriliyor: $fn"
    Invoke-WebRequest -Uri $f.Remote -OutFile $f.Local -UseBasicParsing
}

# Masaustune Kisayol / Bat Kopyala
$Desktop = [Environment]::GetFolderPath("Desktop")
$DesktopBat = Join-Path $Desktop "Oto_Muzik_Merkezi.bat"
Copy-Item (Join-Path $TargetDir "Oto_Muzik_Merkezi.bat") $DesktopBat -Force
Write-Host "  [OK] Masaustune 'Oto_Muzik_Merkezi.bat' kisayolu yerlestirildi!" -ForegroundColor Green

Write-Host "`n[2/3] Sistem bagimliliklari dogrulaniyor (bootstrap)..." -ForegroundColor Yellow
$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $PythonCmd) {
    Write-Host "[HATA] Sistemde Python bulunamadi! Lutfen https://python.org adresinden Python 3.10+ yukleyin." -ForegroundColor Red
    pause
    exit 1
}

$BootstrapPy = Join-Path $ScriptsDir "bootstrap.py"
& python $BootstrapPy

Write-Host "`n[3/3] KURULUM BASARIYLA TAMAMLANDI!" -ForegroundColor Green
Write-Host "Masaustunuzdeki 'Oto_Muzik_Merkezi.bat' dosyasina cift tiklayarak hemen baslatabilirsiniz." -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
