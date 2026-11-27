#!/usr/bin/env python3
"""
Audiophile Music Curator - Metadata, Cover Art (500x500) & Lyrics Embedder
Fetches square artwork (iTunes/Deezer/YouTube) and synchronized lyrics (LRCLIB),
embedding them strictly as ID3v2.3 tags for automotive & mobile compatibility.
"""
import io
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from mutagen.id3 import ID3, APIC, USLT, ID3NoHeaderError
from PIL import Image

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AudiophileCurator/1.0"}


def clean_query(filename: str) -> str:
    name = os.path.splitext(filename)[0]
    name = re.sub(r"^\d{3}\s*-\s*", "", name)
    name = re.sub(r"\(.*?\)|\[.*?\]", " ", name)
    name = re.sub(r"\b(official|video|audio|lyrics|hd|4k|remaster|remastered|mv|cover|mix|ft|feat)\b", " ", name, flags=re.I)
    name = re.sub(r"[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ&'\- ]+", " ", name)
    return " ".join(name.split())[:80]


def fetch_bytes(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            if data and len(data) > 1000:
                return data
    except Exception:
        pass
    return None


def to_square_500_jpeg(raw_img: bytes) -> bytes | None:
    try:
        im = Image.open(io.BytesIO(raw_img)).convert("RGB")
        w, h = im.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        im_cropped = im.crop((left, top, left + min_dim, top + min_dim)).resize((500, 500), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im_cropped.save(buf, format="JPEG", quality=90)
        return buf.getvalue()
    except Exception:
        return None


def find_cover(query: str) -> bytes | None:
    # 1. iTunes
    try:
        url = f"https://itunes.apple.com/search?term={urllib.parse.quote(query)}&media=music&limit=1"
        raw = fetch_bytes(url)
        if raw:
            res = json.loads(raw.decode("utf-8", errors="ignore")).get("results") or []
            if res and res[0].get("artworkUrl100"):
                art_url = res[0]["artworkUrl100"].replace("100x100bb", "600x600bb")
                img = fetch_bytes(art_url)
                if img:
                    sq = to_square_500_jpeg(img)
                    if sq:
                        return sq
    except Exception:
        pass

    # 2. Deezer
    try:
        url = f"https://api.deezer.com/search?q={urllib.parse.quote(query)}&limit=1"
        raw = fetch_bytes(url)
        if raw:
            res = json.loads(raw.decode("utf-8", errors="ignore")).get("data") or []
            if res:
                alb = res[0].get("album") or {}
                art_url = alb.get("cover_big") or alb.get("cover_medium")
                if art_url:
                    img = fetch_bytes(art_url)
                    if img:
                        sq = to_square_500_jpeg(img)
                        if sq:
                            return sq
    except Exception:
        pass

    # 3. YouTube Thumbnail fallback
    try:
        res = subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--get-thumbnail", "--no-playlist", "--quiet", f"ytsearch1:{query}"],
            capture_output=True, text=True, timeout=15
        )
        t_url = (res.stdout or "").strip().splitlines()
        if t_url:
            img = fetch_bytes(t_url[0])
            if img:
                return to_square_500_jpeg(img)
    except Exception:
        pass

    return None


def fetch_lyrics(track_name: str, artist_name: str = "") -> str | None:
    try:
        params = {"track_name": track_name}
        if artist_name:
            params["artist_name"] = artist_name
        url = f"https://lrclib.net/api/get?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode("utf-8", errors="ignore"))
            return data.get("syncedLyrics") or data.get("plainLyrics")
    except Exception:
        pass
    return None


def process_mp3(path: str):
    try:
        try:
            tags = ID3(path)
        except ID3NoHeaderError:
            tags = ID3()

        has_cover = any(isinstance(t, APIC) for t in tags.values())
        has_lyrics = any(isinstance(t, USLT) for t in tags.values())

        if has_cover and has_lyrics:
            return ("SKIP", path)

        q = clean_query(os.path.basename(path))
        changed = False

        # Kapak ekle
        if not has_cover:
            img = find_cover(q)
            if img:
                tags.delall("APIC")
                tags.add(APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=img))
                changed = True

        # Soz ekle
        if not has_lyrics:
            parts = q.split(" - ", 1)
            artist = parts[0].strip() if len(parts) == 2 else ""
            title = parts[1].strip() if len(parts) == 2 else q
            lyr = fetch_lyrics(title, artist)
            if lyr:
                tags.delall("USLT")
                tags.add(USLT(encoding=3, lang="eng", desc="", text=lyr))
                changed = True

        if changed:
            tags.save(path, v2_version=3)
            return ("OK", path)
        return ("MISS", path)
    except Exception as e:
        return ("ERR", f"{path}: {e}")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\devops-engineer\Nextcloud\Music"
    if not os.path.isdir(target):
        target = os.path.expanduser(r"~\Nextcloud\Music")

    all_mp3s = []
    for root, _, files in os.walk(target):
        for fn in files:
            if fn.lower().endswith(".mp3"):
                all_mp3s.append(os.path.join(root, fn))

    print(f"Toplam taranacak MP3: {len(all_mp3s)}")
    ok = skip = miss = err = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        for fut in as_completed([pool.submit(process_mp3, p) for p in all_mp3s]):
            st, p = fut.result()
            if st == "OK":
                ok += 1
            elif st == "SKIP":
                skip += 1
            elif st == "MISS":
                miss += 1
            else:
                err += 1

    print(f"Bitti: Guncellenen: {ok} | Zaten Tam: {skip} | Bulunamayan: {miss} | Hata: {err}")


if __name__ == "__main__":
    main()
