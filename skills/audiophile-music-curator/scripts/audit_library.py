#!/usr/bin/env python3
"""
Audiophile Music Curator - Library Health Audit
Scans music library for missing covers (APIC), missing lyrics (USLT),
duplicate tracks, and path length / character compatibility issues.
"""
import os
import re
import sys
from mutagen.id3 import ID3, APIC, USLT

DEFAULT_DIR = r"C:\Users\MrCoolice\Nextcloud\Music"


def audit(target_dir: str):
    if not os.path.isdir(target_dir):
        # Fallback to current user profile or relative path
        alt_path = os.path.expanduser(r"~\Nextcloud\Music")
        if os.path.isdir(alt_path):
            target_dir = alt_path
        else:
            print(f"HATA: Dizin bulunamadi: {target_dir}")
            return

    total = 0
    missing_covers = []
    missing_lyrics = []
    long_paths = []
    seen_titles = {}
    duplicates = []

    for root, _, files in os.walk(target_dir):
        rel_dir = os.path.relpath(root, target_dir)
        for fn in files:
            if not fn.lower().endswith(".mp3"):
                continue
            total += 1
            full_path = os.path.join(root, fn)
            rel_file = os.path.join(rel_dir, fn)

            if len(full_path) > 160:
                long_paths.append(rel_file)

            clean_name = re.sub(r"^\d{3}\s*-\s*", "", os.path.splitext(fn)[0]).strip().lower()
            if clean_name in seen_titles:
                duplicates.append((rel_file, seen_titles[clean_name]))
            else:
                seen_titles[clean_name] = rel_file

            try:
                tags = ID3(full_path)
                has_cover = any(isinstance(t, APIC) for t in tags.values())
                has_lyrics = any(isinstance(t, USLT) for t in tags.values())
                if not has_cover:
                    missing_covers.append(rel_file)
                if not has_lyrics:
                    missing_lyrics.append(rel_file)
            except Exception:
                missing_covers.append(rel_file)
                missing_lyrics.append(rel_file)

    print("=" * 60)
    print("AUDIOPHILE MUSIC CURATOR - KUTUPHANE SAGLIK RAPORU")
    print("=" * 60)
    print(f"Taranan Dizin         : {target_dir}")
    print(f"Toplam MP3 Parca      : {total}")
    print(f"Kapak Resmi Eksik     : {len(missing_covers)} (%{(100 * (total - len(missing_covers)) / max(total, 1)):.1f} tamam)")
    print(f"Sarki Sozu Eksik      : {len(missing_lyrics)} (%{(100 * (total - len(missing_lyrics)) / max(total, 1)):.1f} tamam)")
    print(f"Mukerrer Suphelileri  : {len(duplicates)}")
    print(f"Uzun Yol (>160 karak) : {len(long_paths)}")
    print("-" * 60)

    if missing_covers:
        print("Kapak Resmi Olmayan Ilk 5 Parca:")
        for p in missing_covers[:5]:
            print(f"  [X] {p}")
        if len(missing_covers) > 5:
            print(f"  ... ve {len(missing_covers) - 5} parca daha.")

    if duplicates:
        print("Mukerrer Kayitlar:")
        for a, b in duplicates[:5]:
            print(f"  [!] {a}  <===>  {b}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR
    audit(path)
