import urllib.request
import urllib.parse
import json
import sys

def get_youtube_suggestions(query, lang="tr"):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl={lang}&q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data[1] if len(data) > 1 else []
    except Exception as e:
        return [f"Hata: {e}"]

def get_google_suggestions(query, lang="tr"):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&hl={lang}&q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data[1] if len(data) > 1 else []
    except Exception as e:
        return [f"Hata: {e}"]

def scout_topic(keyword):
    print(f"\n=======================================================")
    print(f"📡 GECE LORE TREND RADARI: '{keyword.upper()}'")
    print(f"=======================================================")
    
    variations = [
        f"{keyword} türkçe",
        f"{keyword} lore",
        f"{keyword} hikayesi",
        f"{keyword} kimdir",
        f"{keyword} nedir",
        f"{keyword} sonu"
    ]
    
    yt_results = set()
    google_results = set()
    
    for v in variations:
        for s in get_youtube_suggestions(v):
            if s and not s.startswith("Hata"):
                yt_results.add(s)
        for s in get_google_suggestions(v):
            if s and not s.startswith("Hata"):
                google_results.add(s)
                
    print(f"\n🔴 YOUTUBE TÜRKİYE EN ÇOK ARANANLAR ({len(yt_results)} Sorgu):")
    for r in sorted(yt_results)[:8]:
        print(f"   • {r}")
        
    print(f"\n🔵 GOOGLE TÜRKİYE ORGANİK ARAMA NİYETİ ({len(google_results)} Sorgu):")
    for r in sorted(google_results)[:8]:
        print(f"   • {r}")

if __name__ == "__main__":
    kw = sys.argv[1] if len(sys.argv) > 1 else "warhammer 40k"
    scout_topic(kw)
