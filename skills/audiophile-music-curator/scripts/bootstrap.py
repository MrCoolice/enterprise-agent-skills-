#!/usr/bin/env python3
"""
Audiophile Music Curator - Autonomous Bootstrap & Dependency Installer
Ensures all required Python packages (mutagen, Pillow, yt-dlp) and system binaries (ffmpeg)
are present. Can be invoked automatically by AI agents or human users.
"""
import os
import sys
import shutil
import subprocess

REQUIRED_PACKAGES = {
    "mutagen": "mutagen>=1.47.0",
    "PIL": "Pillow>=10.0.0",
    "yt_dlp": "yt-dlp>=2024.0.0"
}


def check_and_install_packages():
    print("[1/3] Python kutuphaneleri kontrol ediliyor...")
    missing = []
    for import_name, pkg_spec in REQUIRED_PACKAGES.items():
        try:
            __import__(import_name)
        except ImportError:
            missing.append(pkg_spec)

    if missing:
        print(f"  -> Eksik kutuphaneler tespit edildi: {', '.join(missing)}")
        print("  -> Pip ile otomatik kuruluyor...")
        cmd = [sys.executable, "-m", "pip", "install", "--upgrade"] + missing
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print("  [OK] Tum Python kutuphaneleri basariyla kuruldu!")
            else:
                print(f"  [HATA] Pip kurulumu basarisiz: {res.stderr}")
                return False
        except Exception as e:
            print(f"  [HATA] Pip calistirilamadi: {e}")
            return False
    else:
        print("  [OK] mutagen, Pillow ve yt-dlp eksiksiz kurulu.")
    return True


def check_ffmpeg():
    print("[2/3] Sistem ses isleme motoru (ffmpeg / ffprobe) kontrol ediliyor...")
    has_ffmpeg = shutil.which("ffmpeg") is not None
    has_ffprobe = shutil.which("ffprobe") is not None

    if has_ffmpeg and has_ffprobe:
        print("  [OK] ffmpeg ve ffprobe sistemde aktif.")
        return True

    print("  [UYARI] ffmpeg veya ffprobe PATH uzerinde bulunamadi!")
    if sys.platform == "win32":
        print("  -> Windows tespit edildi. Otomatik 'winget' ile kurulum deneniyor...")
        if shutil.which("winget"):
            cmd = ["winget", "install", "Gyan.FFmpeg", "--accept-package-agreements", "--accept-source-agreements"]
            try:
                r = subprocess.run(cmd)
                if r.returncode == 0:
                    print("  [OK] FFmpeg winget ile kuruldu! (Terminali yeniden baslatmaniz gerekebilir)")
                    return True
            except Exception:
                pass
        print("  -> Manuel Kurulum: PowerShell'de calistirin:")
        print("     winget install Gyan.FFmpeg")
        print("     veya chocolatey: choco install ffmpeg")
    elif sys.platform == "darwin":
        print("  -> macOS icin terminalden calistirin: brew install ffmpeg")
    else:
        print("  -> Linux icin terminalden calistirin: sudo apt update && sudo apt install -y ffmpeg")
    return False


def verify_library():
    print("[3/3] Muzik kutuphanesi dizini kontrol ediliyor...")
    try:
        from library_config import get_library_dir
        lib_dir = get_library_dir()
        print(f"  [OK] Aktif Kutuphane: {lib_dir}")
        if not os.path.exists(lib_dir):
            os.makedirs(lib_dir, exist_ok=True)
            print(f"  -> Dizin olusturuldu: {lib_dir}")
    except Exception as e:
        print(f"  [!] Kutuphane yapilandirma uyarisi: {e}")


def main():
    print("=" * 70)
    print("  AUDIOPHILE MUSIC CURATOR - OTOMATIK SİSTEM VE BAGIMLILIK KURULUMU")
    print("=" * 70)
    p_ok = check_and_install_packages()
    f_ok = check_ffmpeg()
    verify_library()
    print("=" * 70)
    if p_ok and f_ok:
        print("SISTEM %100 HAZIR! 'car_audio_station.py' veya 'Oto_Muzik_Merkezi.bat' calistirilabilir.")
        return 0
    else:
        print("BAZI BAGIMLILIKLAR EKSIK. Lutfen yukaridaki adimlari takip edin.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
