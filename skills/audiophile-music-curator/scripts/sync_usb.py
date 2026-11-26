#!/usr/bin/env python3
"""
Audiophile Music Curator - High-Speed Automotive Mirror Sync
Safely synchronizes Nextcloud\\Music to automotive FAT32/MBR USB drive (CORSA_MUZIK).
"""
import os
import shutil
import subprocess
import sys

try:
    from library_config import get_library_dir
    DEFAULT_NC = get_library_dir()
except Exception:
    DEFAULT_NC = os.path.expanduser(r"~\Nextcloud\Music")
USB_LABEL = "CORSA_MUZIK"


def get_nc_dir() -> str:
    if os.path.isdir(DEFAULT_NC):
        return DEFAULT_NC
    alt = os.path.expanduser(r"~\Nextcloud\Music")
    if os.path.isdir(alt):
        return alt
    return DEFAULT_NC


def find_usb_root(label: str = USB_LABEL) -> str | None:
    try:
        out = subprocess.check_output(
            ["powershell", "-NoProfile", "-Command",
             f"(Get-Volume | Where-Object {{ $_.DriveType -eq 'Removable' -and $_.FileSystemLabel -eq '{label}' }} | Select-Object -First 1).DriveLetter"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        if out and len(out) == 1:
            return f"{out}:\\"
    except Exception:
        pass
    return None


def sync():
    nc_music = get_nc_dir()
    if not os.path.isdir(nc_music):
        print(f"HATA: Kaynak muzik klasoru bulunamadi: {nc_music}")
        sys.exit(1)

    usb_root = find_usb_root()
    if not usb_root:
        print(f"UYARI: '{USB_LABEL}' etiketli USB bellek takili degil! Lutfen USB'yi takip tekrar deneyin.")
        sys.exit(1)

    print(f"Kaynak : {nc_music}")
    print(f"Hedef  : {usb_root} ({USB_LABEL})")
    print("-" * 55)

    # 50-parca taban guvenlik kilidi
    src_rel_mp3s = set()
    for root, _, files in os.walk(nc_music):
        rel_dir = os.path.relpath(root, nc_music)
        if rel_dir == ".":
            continue
        for fn in files:
            if fn.lower().endswith(".mp3"):
                src_rel_mp3s.add(os.path.join(rel_dir, fn))

    if len(src_rel_mp3s) < 50:
        print(f"GUVENLIK DURDURMA: Kaynakta sadece {len(src_rel_mp3s)} MP3 gorunuyor; USB'den silme yapilmayacak.")
        sys.exit(1)

    copied = updated = skipped = deleted = 0

    # 1. Kopyalama / Guncelleme
    for root, _, files in os.walk(nc_music):
        rel_dir = os.path.relpath(root, nc_music)
        if rel_dir == ".":
            continue
        dst_dir = os.path.join(usb_root, rel_dir)
        os.makedirs(dst_dir, exist_ok=True)

        for fn in files:
            if not fn.lower().endswith(".mp3"):
                continue
            src = os.path.join(root, fn)
            dst = os.path.join(dst_dir, fn)
            if not os.path.exists(dst):
                shutil.copy2(src, dst)
                copied += 1
                print(f"[YENI] {rel_dir}\\{fn}")
            else:
                s_stat = os.stat(src)
                d_stat = os.stat(dst)
                # FAT32 2-saniye toleransi
                if s_stat.st_size != d_stat.st_size or (s_stat.st_mtime - d_stat.st_mtime) > 2:
                    shutil.copy2(src, dst)
                    updated += 1
                    print(f"[GUNCELLENDI] {rel_dir}\\{fn}")
                else:
                    skipped += 1

    # 2. Artik dosyalari temizle (Arac sistem dosyalarina dokunma)
    for root, dirs, files in os.walk(usb_root, topdown=False):
        rel_dir = os.path.relpath(root, usb_root)
        if rel_dir == "." or rel_dir.startswith("System Volume Information"):
            continue
        for fn in files:
            if not fn.lower().endswith(".mp3"):
                continue
            rel_file = os.path.join(rel_dir, fn)
            if rel_file not in src_rel_mp3s:
                os.remove(os.path.join(root, fn))
                deleted += 1
                print(f"[SILINDI] {rel_file}")
        if not os.listdir(root):
            os.rmdir(root)

    print("-" * 55)
    print(f"Esitleme tamamlandi! Yeni: {copied} | Guncellenen: {updated} | Silinen: {deleted} | Zaten esit: {skipped}")


if __name__ == "__main__":
    sync()
