---
name: seo-content-master
description: >-
  Autonomous Turkish & Global SEO/GEO content and audit engine (multi-agent writing, PAS/BAB CRO
  copy, Wikidata entities, Local SEO/NAP, llms.txt/llms-full.txt, Pos 4-15 quick-wins, Google
  Discover). Use when writing SEO blog articles, optimizing search rankings, or generating
  llms.txt. Do NOT use for Matomo API reporting (use matomo-analytics-ops), daily social
  calendars (use social-media-growth), or GTM/pricing strategy (use founder-gtm-growth-council).
---

# 🚀 Autonomous SEO, GEO & Growth Content Engine (Sektör Standardı)

Bu beceri; GitHub ve AI ekosisteminin en gelişmiş SEO ve GEO repolarının (**angelotc/antigravity-seo**, **AgriciDaniel/claude-blog & claude-seo**, **mykpono/ultimate-seo-geo**, **coreyhaines31/marketingskills**, **AI-Marketing-Hub/local-seo-brain**, **raghul-tech/Multi-Agent**) sentezinden doğmuştur.

Sıradan bir makale yazıcısı değildir; **Audit (Denetim) ➔ Plan (Strateji) ➔ Execute (Yazım ve Dönüşüm)** döngüsüyle çalışan, arka planda 5 sanal uzman ajan çalıştıran otonom bir büyüme makinesidir.

---

## 👥 1. Dahili Çoklu Ajan (Multi-Agent) Pipeline

Bir içerik talep edildiğinde sistem tek bir prompt ile yüzeysel yazmak yerine dahili olarak 5 uzman ajanın süzgecinden geçer:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. ARAŞTIRMACI (Researcher): SERP eksiklerini ve Information Gain'i     │
│    (özgün veri/istatistik/rakiplerin bahsetmediği noktalar) çıkarır.   │
├────────────────────────────────────────────────────────────────────────┤
│ 2. İÇERİK MİMARI (Architect): BLUF (İlk 40 kelimede cevap), H2/H3      │
│    hiyerarşisi ve semantik Wikidata entity haritasını çıkarır.         │
├────────────────────────────────────────────────────────────────────────┤
│ 3. METİN YAZARI (Copywriter - Corey Haines CRO): Salt bilgi değil,     │
│    okuyucuyu aksiyona geçiren PAS (Problem-Agitate-Solution) uygular.   │
├────────────────────────────────────────────────────────────────────────┤
│ 4. KALİTE & ŞEMA DENETÇİSİ (Reviewer Gate): 4 aşamalı kapıdan geçirir; │
│    JSON-LD şemalarını ve meta etiketlerini doğrular (Min 90/100 Puan). │
├────────────────────────────────────────────────────────────────────────┤
│ 5. İNSANLAŞTIRICI (Humanizer & Scrubber): Tüm robotik AI kalıplarını   │
│    ve görünmez sıfır genişlikli (\u200B) filigranları yok eder.       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ 2. Üç Temel Çalışma Modu (Audit ➔ Plan ➔ Execute)

Kullanıcının isteğine göre bu 3 moddan biri tetiklenir:

### Mod A: EXECUTE (Sıfırdan Zirveye Makale Üretimi)
Kullanıcı *"Bana [Konu] hakkında yazı yaz"* dediğinde devreye girer. Hem Google Türkiye'de 1. sıraya hem Google Keşfet'e hem de Perplexity/ChatGPT alıntılarına uygun eksiksiz yayın paketi üretir.

### Mod B: AUDIT & QUICK WINS (angelotc/antigravity-seo)
Kullanıcı *"Şu yazımı/sayfamı denetle"* dediğinde veya Google Search Console'da **4. ile 15. sıra arasında sıkışmış** sayfalar verildiğinde:
* **Hızlı Tıklama Sıçraması (CTR Boost):** Sayfanın başlığını ve meta açıklamasını tıklama mıknatısına dönüştürür.
* **Eksik Entity & LSI Enjeksiyonu:** Rakiplerin bahsettiği ama sayfada olmayan kavramları ekletir.
* **Hemen Çıkma Oranı (Bounce Rate) İyileştirmesi:** Sayfanın ilk 100 kelimesine BLUF kutusu yerleştirir.

### Mod C: LOCAL SEO & MAPS (AI-Marketing-Hub / local-seo-brain)
Yerel işletmeler (Veri merkezi, tamir servisi, klinikler, ajanslar vb.) için:
* **NAP Uyumu:** İsim, Adres, Telefon tutarlılığı.
* **`LocalBusiness` JSON-LD:** Coğrafi koordinatlar (`geo:latitude/longitude`), çalışma saatleri ve hizmet bölgeleri.
* **Yerel Güven Sinyalleri:** İl/ilçe bazlı arama terimleri (Örn: *"İstanbul Anadolu Yakası Veri Merkezi"*).

---

## 📈 3. Corey Haines Dönüşüm Odaklı Metin Yazarlığı (CRO)

Bir makale milyonlarca kez okunsa bile ziyaretçiyi müşteriye veya takipçiye dönüştürmüyorsa başarısızdır. 

Metin yazılırken şu psikolojik kancalar zorunludur:
1. **PAS Formülü (Problem - Agitate - Solution):**
   * *Problem:* Ziyaretçinin canını sıkan acı nokta (Örn: Gece yarısı çöken sunucu).
   * *Agitate (Büyütme):* Çözülmezse maliyetin ve müşteri kaybının ne olacağı.
   * *Solution (Çözüm):* Adım adım net teknik kurtuluş planı.
2. **BAB Çerçevesi (Before - After - Bridge):**
   * *Before:* Öncesi (Hantal, güvensiz, yavaş durum).
   * *After:* Sonrası (380 ms hız, sıfır kesinti, güvenli altyapı).
   * *Bridge (Köprü):* Bu dönüşümü sağlayan yöntem ve eyleme çağrı (CTA).

---

## 🇹🇷 4. Google Türkiye & Keşfet (Discover) Hükümranlığı

* **1200px Genişlik Kuralı:** Keşfet için en az 1200x675px görsel brifi ve `<meta name="robots" content="max-image-preview:large">`.
* **Robotik Tercüme Yasağı:** *"Oyun kurallarını değiştiren"*, *"Günümüzün dijital dünyasında"*, *"Haydi dalalım"* gibi çeviri kokan tüm kalıpların mutlak engeli.
* **Türkiye Regülasyon Güveni:** KVKK, BTK ve yerel fatura/TL fiyatlandırma standartlarına doğal atıf.

---

## 📦 5. Standart Çıktı Paketi (Bütünleşik Teslimat)

Her üretilen içerikte şu bileşenler eksiksiz sunulur:

1. **H1 Başlık:** (<60 karakter, CTR tetikleyicili).
2. **BLUF Hızlı Özet Kutusu:** İlk 40-50 kelimede doğrudan çözüm.
3. **Google Keşfet Görseli Konsepti & Türkçe ALT Açıklaması.**
4. **Semantik Gövde:** E-E-A-T vaka tecrübesi + Karşılaştırma Tabloları + Kontrol Listesi.
5. **SSS:** Google Türkiye "Kullanıcılar Bunları da Sordu" (PAA) 3-5 soru.
6. **Teknik On-Page & Schema Kodu (HTML):**
   * Title, Description, Canonical, OG kartları.
   * `BlogPosting` + `FAQPage` + `about / mentions (Wikidata Entity)` JSON-LD.
7. **Çift Katmanlı `/llms.txt` ve `/llms-full.txt` Giriş Satırı:** Sitenizi yapay zekâ botlarına indeksleten markdown standardı.
8. **Sosyal Medya Dönüşüm Köprüsü:** LinkedIn postu, Instagram Carousel planı ve X flood taslağı.

---

## 🔥 6. Son 30 Gün Trend Avcısı (Konu Keşfi & Güncellik Modülü)
*(mvanhorn/last30days-skill & blader/humanizer yaklaşımlarından uyarlanmıştır)*

Kullanıcı *"Bu hafta/ay ne yazalım, ne videosu çekelim?"* dediğinde veya yeni içerik fikri arandığında:
1. **Çoklu Platform Taraması:** `search_web` ile son 30 günde Reddit (`r/homelab`, `r/OPNsenseFirewall`, `r/Proxmox`), Hacker News, YouTube ve X'te en çok tartışılan gerçek kullanıcı sorunlarını ve yeni sürümleri (örn. OPNsense 26.7, Proxmox CVE'leri, yeni self-hosted araçlar) tara.
2. **Trend → GölgeSiber Açısı:** Bulunan popüler konuyu Türkiye bağlamına (CGNAT, yerli ISP sorunları, KVKK/BTK, fiyat/performans homelab donanımı) uyarlayarak 3 somut başlık öner.
112: 3. **Humanizer Son Kontrolü:** Yayına hazırlanan metinde AI klişelerini (*"sonuç olarak", "hızla gelişen dijital dünyada", "adeta bir devrim"* vb.) temizle; gerçek saha komutu, hata kodu ve somut sayı bırak.

---

## 🛠️ 7. YENİ NESİL SEO/GEO ARAÇ & MCP ENTEGRASYON PROTOKOLÜ

İçerik araştırması, rakip analizi ve yapay zekâ görünürlüğü için şu modern araç mimarisi kullanılır:

1. **Firecrawl MCP (`mendableai/firecrawl-mcp-server`):**
   * Dinamik JavaScript render gerektiren modern SPA/Next.js sitelerini ve anti-bot arkasındaki rakip içerikleri LLM'lerin doğrudan analiz edebileceği temiz Markdown formatında çeker.
   * Derin crawl (`/crawl`) ve temiz içerik çıkarma (`/scrape`) ile rakiplerin H2/H3 yapısını ve gizli şemalarını anında deşifre eder.
2. **Perplexity API / MCP Platformu:**
   * Doğrudan canlı SERP alıntılarını, akademik/sektörel referansları ve gerçek kullanıcı arama niyetlerini (Search Intent) doğrular.
   * Üretilen içeriğin Perplexity, ChatGPT Search ve Google AI Overviews tarafından doğrudan kaynak gösterilme (Citations) oranını test eder.
3. **Google Search Console (GSC MCP) & OpenSEO Standardı:**
   * **GSC MCP:** Canlı tıklama, gösterim, ortalama sıra ve CTR verilerini çekerek **4-15. sırada sıkışmış (Quick-Win)** sayfaları otomatik tespit eder.
   * **OpenSEO:** Sıralama takibi, anahtar kelime zorluğu ve site denetimi için üçüncü parti pahalı SaaS araçlarına (Ahrefs/Semrush) gerek kalmadan yerel terminalden denetim yürütür.
4. **GEO Optimizer & LLM-Ready (AEO) Mimarisi:**
   * Sitenin kök dizininde `/llms.txt` ve `/llms-full.txt` dosyalarını güncel tutar.
   * `WebMCP` ve `Lighthouse Agentic Browsing` uyumluluğu için sayfaları otonom AI crawler botlarının token harcamadan anlayacağı semantik XML/JSON-LD ve temiz HTML hiyerarşisiyle sunar.
