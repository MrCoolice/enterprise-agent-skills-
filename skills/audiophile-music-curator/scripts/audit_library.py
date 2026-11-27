#!/usr/bin/env python3
"""
Audiophile Music Curator - Library Health & Zero-Duplicate Audit
Scans music library for missing covers (APIC), missing lyrics (USLT),
fuzzy duplicate tracks across all folders, and path length / character issues.
"""
import os
import re
import sys
from collections import defaultdict
from mutagen.id3 import ID3, APIC, USLT

try:
    from library_config import get_library_dir
    DEFAULT_DIR = get_library_dir()
except Exception:
    DEFAULT_DIR = os.path.expanduser(r"~\Nextcloud\Music")


def normalize_title(filename: str) -> str:
    """Normalizes track title for fuzzy duplicate detection."""
    name = os.path.splitext(filename)[0]
    # Remove leading track index
    name = re.sub(r"^\d+\s*[-_.]\s*", "", name)
    # Remove parenthesized details like (Official Video), [Remastered], (feat. ...), etc.
    name = re.sub(r"[\(\[\{].*?[\)\]\}]", "", name)
    # Lowercase and clean non-alphanumeric
    name = re.sub(r"[^a-zA-Z0-9\sğüşıöçĞÜŞİÖÇ]", " ", name.lower())
    name = re.sub(r"\s+", " ", name).strip()
    return name


def is_song_in_library(query: str, target_dir: str = DEFAULT_DIR) -> tuple:
    """
    Checks if a song already exists in the library using fuzzy matching.
    Returns (True, matching_relative_path) or (False, None).
    """
    norm_query = normalize_title(query)
    if not norm_query:
        return False, None

    for root, _, files in os.walk(target_dir):
        rel_dir = os.path.relpath(root, target_dir)
        for fn in files:
            if not fn.lower().endswith((".mp3", ".flac", ".m4a")):
                continue
            norm_fn = normalize_title(fn)
            if norm_query == norm_fn or (len(norm_query) > 5 and norm_query in norm_fn) or (len(norm_fn) > 5 and norm_fn in norm_query):
                return True, os.path.join(rel_dir, fn)
    return False, None


def audit(target_dir: str):
    if not os.path.isdir(target_dir):
        target_dir = DEFAULT_DIR
        if not os.path.isdir(target_dir):
            print(f"HATA: Dizin bulunamadi: {target_dir}")
            return

    total = 0
    missing_covers = []
    missing_lyrics = []
    long_paths = []
    by_norm = defaultdict(list)

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

            norm = normalize_title(fn)
            if len(norm) > 4:
                by_norm[norm].append(rel_file)

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

    duplicates = {k: v for k, v in by_norm.items() if len(v) > 1}

    print("=" * 65)
    print("AUDIOPHILE MUSIC CURATOR - KUTUPHANE SAGLIK & MUKERRER RAPORU")
    print("=" * 65)
    print(f"Taranan Dizin         : {target_dir}")
    print(f"Toplam MP3 Parca      : {total}")
    print(f"Kapak Resmi Eksik     : {len(missing_covers)} (%{(100 * (total - len(missing_covers)) / max(total, 1)):.1f} tamam)")
    print(f"Sarki Sozu Eksik      : {len(missing_lyrics)} (%{(100 * (total - len(missing_lyrics)) / max(total, 1)):.1f} tamam)")
    print(f"Mukerrer Sarki Grubu  : {len(duplicates)}")
    print(f"Uzun Yol (>160 karak) : {len(long_paths)}")
    print("-" * 65)

    if duplicates:
        print("\nMukerrer / Ayni Sarki Kayitlari:")
        for norm_title, paths in list(duplicates.items())[:10]:
            print(f"  [!] '{norm_title}':")
            for p in paths:
                print(f"      -> {p}")
        if len(duplicates) > 10:
            print(f"  ... ve {len(duplicates) - 10} mukerrer grup daha.")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR
    audit(path)
