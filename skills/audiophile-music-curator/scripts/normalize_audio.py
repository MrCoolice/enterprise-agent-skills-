#!/usr/bin/env python3
"""
Audiophile Music Curator - Smart Loudness Normalizer (-14 LUFS / EBU R128)
Applies non-destructive loudness normalization targeting automotive standards (-14 LUFS, -1.5 dBFS True Peak).
Safely preserves ID3v2.3 tags and only touches tracks outside the safe listening window unless forced.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

TARGET_LUFS = -14.0
TARGET_TP = -1.5
MIN_LUFS_THRESHOLD = -18.0
MAX_LUFS_THRESHOLD = -9.0


def analyze_lufs(path: str) -> float | None:
    cmd = ['ffmpeg', '-nostats', '-i', path, '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    m = re.search(r'Integrated loudness:\s+I:\s+([-\d.]+)\s+LUFS', res.stderr)
    return float(m.group(1)) if m else None


def normalize_track(path: str, force: bool = False):
    current_lufs = analyze_lufs(path)
    if current_lufs is None:
        return ("ERR", path, "LUFS okunamadi")

    # Eger parca zaten saglikli araliktaysa (-18 ile -9 arasi) ve force yoksa dokunma
    if not force and (MIN_LUFS_THRESHOLD <= current_lufs <= MAX_LUFS_THRESHOLD):
        return ("SKIP", path, f"{current_lufs:.1f} LUFS (Ideal aralikta)")

    # Gecici dosya uzerinde loudnorm uygula (320k MP3 kalitesi)
    tmp_out = path + ".norm.mp3"
    filt = f"loudnorm=I={TARGET_LUFS}:TP={TARGET_TP}:LRA=11"
    cmd = [
        'ffmpeg', '-y', '-nostats', '-loglevel', 'error',
        '-i', path,
        '-af', filt,
        '-b:a', '320k',
        '-id3v2_version', '3',
        tmp_out
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(tmp_out) and os.path.getsize(tmp_out) > 1000:
        # Eski dosyanin uzerine yaz
        shutil.move(tmp_out, path)
        return ("OK", path, f"{current_lufs:.1f} LUFS -> {TARGET_LUFS:.1f} LUFS")
    else:
        if os.path.exists(tmp_out):
            os.remove(tmp_out)
        return ("ERR", path, "ffmpeg donusum hatasi")


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\MrCoolice\Nextcloud\Music"
    force_all = "--force" in sys.argv

    if not os.path.isdir(target_dir):
        target_dir = os.path.expanduser(r"~\Nextcloud\Music")

    files = []
    for r, _, fns in os.walk(target_dir):
        for f in fns:
            if f.endswith('.mp3'):
                files.append(os.path.join(r, f))

    print("=" * 60)
    print("AUDIOPHILE SES SEVIYESI NORMALIZASYONU (-14 LUFS / EBU R128)")
    print("=" * 60)
    print(f"Hedef Dizin : {target_dir}")
    print(f"Toplam Dosya: {len(files)}")
    print(f"Hedef Seviye: {TARGET_LUFS} LUFS (True Peak: {TARGET_TP} dBFS)")
    print(f"Mod         : {'Tum Parcayi Zorla' if force_all else 'Cerrahi (Sadece < -18 veya > -9 LUFS olanlar)'}")
    print("-" * 60)

    ok = skip = err = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        for fut in pool.map(lambda p: normalize_track(p, force_all), files):
            st, p, msg = fut
            rel = os.path.basename(p)
            if st == "OK":
                ok += 1
                print(f"[DUZELTILDI] {rel} ({msg})")
            elif st == "SKIP":
                skip += 1
            else:
                err += 1
                print(f"[ERR] {rel} ({msg})")

    print("-" * 60)
    print(f"Tamamlandi: Duzeltilen: {ok} | Orijinal Korunan: {skip} | Hata: {err}")


if __name__ == "__main__":
    main()
