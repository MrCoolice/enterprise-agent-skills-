#!/usr/bin/env python3
"""
Web Sitesi & Blog Tarayıcı (Omnichannel Content Scraper)
Bu script, secops-domain.example.com veya müşteri web sitesindeki blog yazılarını, başlıkları
ve hizmet sayfalarını tarayarak sosyal medyaya uyarlanacak (repurpose) ham veriyi JSON olarak çıkarır.
"""

import sys
import json
import re
from urllib.request import Request, urlopen
from urllib.parse import urlparse

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return ' '.join(cleantext.split())

def scrape_url(url):
    print(f"[*] Taranıyor: {url}")
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    try:
        with urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Başlık (Title)
            title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else ""
            
            # Meta Description
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
            desc = desc_match.group(1).strip() if desc_match else ""
            
            # H1 ve H2 Başlıkları
            h1_tags = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE)
            h2_tags = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE)
            
            clean_h1 = [clean_html(h) for h in h1_tags if h.strip()]
            clean_h2 = [clean_html(h) for h in h2_tags if h.strip()][:10]
            
            # Paragraflardan kısa bir özet
            p_tags = re.findall(r'<p[^>]*>(.*?)</p>', html, re.IGNORECASE)
            clean_paragraphs = [clean_html(p) for p in p_tags if len(p.strip()) > 40][:8]
            
            result = {
                "url": url,
                "title": clean_html(title),
                "description": desc,
                "h1_headings": clean_h1,
                "h2_headings": clean_h2,
                "key_excerpts": clean_paragraphs
            }
            return result
    except Exception as e:
        print(f"[!] Hata: {e}", file=sys.stderr)
        return {"url": url, "error": str(e)}

def main():
    if len(sys.argv) < 2:
        target_url = "https://secops-domain.example.com"
    else:
        target_url = sys.argv[1]
        
    data = scrape_url(target_url)
    output_filename = "scraped_blog_data.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[+] Başarılı! Veriler kaydedildi: {output_filename}")
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
