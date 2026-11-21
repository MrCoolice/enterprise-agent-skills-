---
name: technical-book-publishing
description: >-
  Technical book authoring, 10 Golden Laws editorial review, IDDIA_DEFTERI.md & OPNsense 26.7+
  MVC fact-checking, cross-reference governance, and B5 print/PDF/EPUB typesetting (Pandoc,
  WeasyPrint, Typst) for OPNsense 2026 Book. Use when drafting/reviewing book chapters or
  building PDF/EPUB. Do NOT use for SEO blog posts (use seo-content-master), SVG/PNG figures
  (use editorial-architecture-diagrams), or .pptx slides (use native-pptx-presentations).
---

# 📖 Teknik Kitap Yazarlığı, Hakemlik & PDF/EPUB Dizgi Becerisi

Bu beceri; **dsebastien/technical-documentation-skill** (Google Developer Style & Diátaxis), **netresearch/markdown-to-pdf-skill** & **slapash/weasyprint-pdf-skill** (Pandoc + WeasyPrint CSS Paged Media), **lucifer1004/claude-skill-typst** ve **kshanxs/book-writer-skill** (Book Memory Bank) disiplinlerini **OPNsense: Kurumsal Ağ Güvenliği ve Altyapı El Kitabı (2026 Sürümü)** projesine özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **uzun form teknik kitap yazarlığı, hakem/iddia doğrulama, terim/çapraz referans tutarlılığı ve B5 baskı/PDF/EPUB dizgisi** içindir. Blog/Google Keşfet SEO makaleleri için `seo-content-master`, kitap içi `.svg`/`.png` diyagram üretimi için `editorial-architecture-diagrams` kullanılır.

---

## 📜 1. OPNsense 2026 Kitap Anayasası (10 Altın Kanun — İhlal Yasaktır)

Her yeni bölüm, revizyon veya hakem incelemesi şu 10 kanuna birebir uymak zorundadır:
1. **Jargon Yerine Analoji:** Soyut ağ kavramları önce gerçek hayat analojisiyle (apartman dairesi, pasaport polisi, posta kutusu) açılır.
2. **Önce Neden, Sonra Nasıl:** Hiçbir menü/buton *"neden yapıyoruz, yapmazsak ne patlar?"* açıklanmadan tıklatılmaz.
3. **Kademeli Zafer & Başarı Kontrol Noktası:** Her bölüm sonunda okuyucunun kendi labında test edeceği somut doğrulama kutusu (ping, yeşil ikon, log kanıtı) yer alır.
4. **Sadece Türkçe Uyarı Kutuları:** İngilizce `NOTE`/`WARNING` yerine yalnızca standart Türkçe bloklar kullanılır:
   - `> 🚨 **HAYATİ TUZAK — ...**` (lockout / kesinti / güvenlik tehlikesi)
   - `> 💡 **SAHA İNCİSİ — ...**` (GölgeSiber saha tecrübesi ve pro ipucu)
5. **Bölüm Girişi Kancası (Hook):** Ansiklopedi tanımıyla değil; gerçek bir saha arızası, güvenlik açığı veya çarpıcı senaryo ile başla.
6. **16x24 cm B5 Matbaa Disiplini:** Yatay taşan geniş tablolar ve 72–78 karakteri aşan uzun kod/komut satırları yasaktır (satırları temiz böl veya özetle).
7. **300 DPI Lab Görselleri + QR Video Köprüsü:** İnternetten bulanık görsel alınmaz; tüm ekran görüntüleri izole `vmbr99` labında 2026 MVC temasında üretilir, kritik adımlarda `secops-domain.example.com/opnsense/vXX` QR referansı tutulur.
8. **Sözlük & Çapraz Başvuru (`Ek_A`):** Terim tekrarlarıyla metni şişirme; ilk geçişte `*(Bkz. Sözlük)*`, diğer bölümlere kesin `Bölüm X.Y` / `Şekil X.Y` numarasıyla bağla.
9. **Türkiye Saha Gerçekliği:** Türk Telekom PPPoE VLAN 35, CGNAT, Proxmox Checksum Offload, SSD ömrünü koruyan MFS RAM diskleri ve yerli donanım/ISP deneyimleri doğal olarak işlenir.
10. **2026 Paradigma Doğruluğu:** Eski ISC DHCP yerine **Kea DHCP** (ve hibrit Dnsmasq), OpenVPN yerine **WireGuard (kmod)**, **CrowdSec (`os-crowdsec`)**, **FreeBSD 14+** ve **OPNsense 26.7+ MVC arayüzü** esas alınır.

---

## 🧠 2. Kitap Hafıza Bankası & Hakem Doğrulama Kapısı (Fact-Check Gate)
*(kshanxs Book Memory Bank + OPNsense_2026_Kitap_Projesi doğrulama altyapısı)*

Her düzenlemede şu proje hafıza dosyalarıyla tutarlılık zorunludur:
- **`IDDIA_DEFTERI.md`:** Kitaptaki her teknik iddia, sürüm numarası, RFC/standart, performans rakamı ve OPNsense 26.7+ MVC menü yolu doğrulanmadan kesin yargı olarak yazılmaz (uydurma menü yolu kesinlikle yasak!).
- **`Ek_A_Donanim_ve_Ag_Terimleri_Sozlugu.md` & `Ek_B_Kaynakca_ve_Uluslararasi_Standartlar.md`:** Yeni teknik terim veya standart eklendiğinde sözlük/kaynakça tutarlılığını kontrol et.
- **`EK_ONERI_Gorsel_ve_QR_Takip_Tablosu.md` & `scratch/check_*.py`:** Şekil/Diyagram numaraları (`diyagram_X_Y`, `sekil_X_Y`), dosya varlığı ve çapraz referanslar kırık bırakılmaz.

---

## 🖨️ 3. B5 (16x24 cm) PDF & EPUB Dizgi Standartları
*(Pandoc + WeasyPrint CSS Paged Media & Typst en iyi pratikleri)*

`build_preview_pdf.py` (WeasyPrint/HTML→PDF) veya Pandoc/Typst çıktılarında şu matbaa kurallarını koru:
1. **CSS `@page` & Baskı Marjları:** `@page { size: 160mm 240mm; }` + çift taraflı cilt (iplik dikiş) için iç marj (`@page :left` / `@page :right`) dış marjdan `4–6mm` daha geniş (gutter) bırakılır; sayfa numarası ve koşan üst başlık (running header) bölüm kapak sayfalarında gizlenir.
2. **Yetim/Dul Satır & Blok Kırılması Koruması:**
   - Başlıklarda `break-after: avoid;`, uyarı kutuları/kod blokları/figür+altyazı çiftlerinde `break-inside: avoid;`, paragraflarda `orphans: 3; widows: 3;`.
3. **Tipografi & Kod Blokları:** Gövde metni `9.5pt–10.5pt` rahat satır aralığı (`1.45`), kod bloklarında `JetBrains Mono` / `Consolas` (`8pt–8.5pt`, `white-space: pre-wrap`, baskıda okunaklı açık gri kutu).
4. **Görsel & Emoji Hijyeni:** PDF içinde bozuk unicode emoji basımı yerine yalnızca metin veya temiz SVG rozet/ikon; tüm diyagramlar `editorial-architecture-diagrams` Mod A standardında (`.svg` + 300 DPI `.png`).

---

## 📋 4. Standart Kitap Editörü / Hakem Çıktı Formatı

1. **Hakem & Anayasa Kontrolü:** 10 Altın Kanun ve OPNsense 26.7+ MVC doğruluk bulguları (`🔴 Hata / Uyumsuzluk`, `🟡 İyileştirme`, `🟢 Güçlü`).
2. **Düzenlenmiş Metin / Yama:** B5 uyumlu, Türkçe kutulu, sözlük/çapraz referanslı metin veya `build_preview_pdf.py` CSS/dizgi güncellemesi.
3. **Tutarlılık Kontrol Listesi:** `IDDIA_DEFTERI.md`, `Ek_A`, şekil/QR numaraları ve tek-cilt (`OPNsense_2026_Kurumsal_El_Kitabi_Tek_Cilt.md`) senkron notu.
