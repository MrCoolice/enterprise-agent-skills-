#!/usr/bin/env python3
"""
Sosyal Medya Takvimi CSV Dışa Aktarıcı (Buffer & Meta Business Suite Formatı)
Bu script, üretilen aylık planı tek tıkla Buffer veya Meta'ya yüklenecek standart CSV'ye çevirir.
"""

import sys
import csv
import json
import os

def export_to_csv(posts, output_path="sosyal_medya_takvimi_buffer.csv"):
    """
    Buffer ve Meta CSV Standart Sütunları:
    Date, Time, Text, Link, Platform, Media_Note
    """
    headers = ["Date", "Time", "Platform", "Content_Type", "Text", "Hashtags", "Link", "Visual_Notes"]
    
    with open(output_path, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for post in posts:
            writer.writerow([
                post.get("date", ""),
                post.get("time", ""),
                post.get("platform", "Instagram"),
                post.get("type", "Reels"),
                post.get("caption", ""),
                post.get("hashtags", ""),
                post.get("link", "https://secops-domain.example.com/links"),
                post.get("visual_note", "")
            ])
            
    print(f"[+] CSV başarıyla oluşturuldu: {output_path}")

def main():
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            posts = json.load(f)
    else:
        # Örnek Şablon Verisi
        posts = [
            {
                "date": "2026-11-10",
                "time": "19:45",
                "platform": "Instagram",
                "type": "Reels",
                "caption": "Web siteniz dün gece saldırı aldı mı? İşte hemen kontrol etmeniz gereken 3 kritik sunucu logu...",
                "hashtags": "#golgesiber #siberguvenlik #datacenter #sunucu #ddos",
                "link": "https://secops-domain.example.com/links",
                "visual_note": "Terminal log akışı, konuşan kişi, hızlı kesmeler"
            },
            {
                "date": "2026-11-12",
                "time": "09:00",
                "platform": "LinkedIn",
                "type": "PDF Carousel",
                "caption": "Bir BT yöneticisinin en büyük kabusu: Yanlış yapılandırılmış güvenlik duvarı. İşte 2026'da şirketlerin yaptığı 5 ölümcül hata.",
                "hashtags": "#siberguvenlik #btyonetimi #datacenter",
                "link": "https://secops-domain.example.com/links",
                "visual_note": "Koyu lacivert ve neon mavi kurumsal infografik slaytları"
            },
            {
                "date": "2026-11-14",
                "time": "12:00",
                "platform": "Instagram",
                "type": "Fotoğraf",
                "caption": "Veri merkezinde 36 saatin özeti ☕ Sunucular ayakta, kahveler taze. Sizin haftanız nasıl geçti?",
                "hashtags": "#golgesiber #datacenterlife #lifestyle #ofis #girisimcilik",
                "link": "https://secops-domain.example.com/links",
                "visual_note": "Kahve bardağı, arkada yanıp sönen sunucu kabinleri ve sıcak ışık"
            }
        ]
        
    export_to_csv(posts)

if __name__ == "__main__":
    main()
