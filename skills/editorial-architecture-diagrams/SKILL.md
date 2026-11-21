---
name: editorial-architecture-diagrams
description: >-
  Publication-grade technical architecture diagrams, print-ready book figures (.svg + .png), and
  self-contained interactive HTML topologies for OPNsense 2026 Book and secops-domain.example.com. Use when
  designing network topologies, VLAN/firewall flowcharts, or Slate-950/print editorial diagrams.
  Do NOT use for editable .pptx slides (use native-pptx-presentations), animated videos (use
  video-director-engine), or config.xml audits (use opnsense-proxmox-secops).
---

# 📐 Editoryal Teknik Mimari Diyagram & SVG/HTML Tasarım Becerisi

Bu beceri; **cathrynlavery/diagram-design**, **marola-dev/marola** (saf SVG geometri mühendisliği), **JOHNadonis** (siber koyu tema) ve **konraddzbik / tt-a1i/archify** (tek-dosya interaktif HTML) standartlarını **OPNsense 2026 Kitap Projesi**, **`secops-domain.example.com`** ve **GölgeSiber Veri Merkezi** şemaları için birleştirir.

> **Kapsam Sınırı:** Bu beceri **statik yayın/matbaa kalitesi (`.svg` + `.png`) ve tek-dosya interaktif HTML teknik diyagramları** içindir. Hareketli video/Reels/3D harita animasyonu için `video-director-engine`, OPNsense `config.xml` güvenlik denetimi için `opnsense-proxmox-secops` kullanılır.

---

## 🚫 1. Kesinlikle Yasaklanan "Mermaid Slop" ve SVG Hataları

1. **Hızlı Taslak Dışında Ham Mermaid Yasağı:** Yalnızca sohbet içi hızlı taslak veya Markdown notu istenirse Mermaid kullanılır; **kitap figürü, blog görseli veya kurumsal sunum** istendiğinde daima **el işçiliği kontrollü SVG veya tek-dosya HTML+SVG** üretilir.
2. **Bozuk Unicode Emoji (`[]`) Yasağı:** SVG içinde ham emoji karakteri kullanılmaz (PDF/Windows/Linux render'da boş kareye döner); tüm ikonlar basit, temiz **saf SVG path vektörleri** olmalıdır.
3. **Çakışan Kutu, Kesişen Ok & Taşan Metin Yasağı:**
   - Metin hiçbir zaman kutu kenarına yapışamaz veya taşamaz (her kutuda en az `16–20px` iç dolgu, uzun etiketlerde açık `<tspan>` satır kırılımı).
   - Oklar asla kutu ve yazıların üzerinden geçemez.
4. **Ağır Gölge & Bulanık Efekt Yasağı:** Kitap ve teknik şemalarda ucuz `drop-shadow` yığınları yerine keskin `1px–1.5px` kenarlıklar, temiz renk hiyerarşisi ve net ızgara (grid) hizalaması kullanılır.

---

## 🎨 2. İki Standart Tema Modu (Bağlama Göre Seçim)

### Mod A: Kitap / PDF / Matbaa Modu (`OPNsense_2026_Kitap_Projesi`)
* **Zemin & Kontrast:** Temiz beyaz/açık gri zemin (`#FFFFFF` / `#F8FAFC`), koyu arduvaz metin (`#0F172A`), baskıda solmayacak net kenarlıklar (`#CBD5E1` / `#475569`) ve **en fazla 3 kontrollü vurgu rengi** (örn. Güvenlik/WAN: `#DC2626`, Güvenilir LAN/Altyapı: `#0284C7`, İzole/Onaylı: `#059669`).
* **Çift Çıktı & Adlandırma Disiplini:** `OPNsense_2026_Kitap_Projesi/images/diagrams/` altında her figür için kaynak **`.svg`** + yüksek DPI (min `2x` / `1600px+` genişlik) **`.png`** çifti (`diyagram_X_Y_*.svg/png` veya `sekil_X_Y_*.svg/png`) üretilir.
* **Siyah-Beyaz Okunabilirlik:** Renk körlüğü veya siyah-beyaz baskıda bile akış bozulmasın diye kritik ayrımlarda kesikli çizgi (`stroke-dasharray`), farklı ok ucu ve açık etiket (`[WAN]`, `[VLAN 10]`) kullanılır.

### Mod B: GölgeSiber Web / NOC Koyu Modu (`secops-domain.example.com` & Veri Merkezi)
* **Zemin & Tipografi:** `Slate-950` (`#020617`) zemin + opsiyonel ince `40px` teknik ızgara (`rgba(148,163,184,0.08)`), teknik kod/IP/port değerlerinde `JetBrains Mono` / monospace, başlıklarda temiz sans-serif (`Inter` / `Segoe UI`).
* **Semantik Renk Kodlaması:**
  - `WAN / İnternet / Saldırı Yüzeyi`: Mercan / Kırmızı (`#F43F5E`)
  - `Firewall / Güvenlik / CrowdSec`: Kehribar / Turuncu (`#F59E0B`)
  - `Proxmox / Altyapı / MGMT`: Siber Cyan (`#06B6D4`)
  - `Sağlıklı Servis / Doğrulanmış Akış`: Nane / Zümrüt (`#10B981`)
  - `DMZ / Web / Proxy`: İndigo / Mor (`#8B5CF6`)
* **İnteraktif HTML Seçeneği (`konraddzbik` / `archify`):** Web vitrini veya canlı sistem haritası istendiğinde tek dosya, sıfır harici CDN bağımlılıklı HTML+SVG üret: düğüm tıklayınca sağ detay paneli (IP, VLAN, port, görev), koyu/aydınlık geçişi ve tek tıkla `SVG` / `PNG` indirme butonu.

---

## 📏 3. Katı SVG Geometri & Katman Mühendisliği (`marola` Standardı)

Her SVG dosyası şu **5 geometrik kurala** birebir uymalıdır:

1. **Sabit `viewBox` & Matematiksel Izgara:** Tüm koordinatlar `8px` veya `10px` katlarında hizalanır; `viewBox="0 0 W H"` etrafında en az `32–40px` dış boşluk (padding) bırakılır.
2. **Katman Sırası (Z-Order) Kuralı:** SVG içinde gruplar şu sırayla yazılır ki oklar asla kutuların üstüne binmesin:
   - `<g id="layer-bg">` (Zemin, ızgara, başlık)
   - `<g id="layer-zones">` (VLAN / Host / DMZ sınır kutuları)
   - `<g id="layer-edges">` (Tüm bağlantılar ve oklar — **kutulardan önce!**)
   - `<g id="layer-nodes">` (Servis/cihaz kutuları ve SVG ikonları)
   - `<g id="layer-labels">` (Hat etiketleri — ok çizgisini maskelemek için arkasında zemin renginde ince `<rect>` / `double-rect masking` ile!)
   - `<g id="layer-legend">` (Sistem sınırının tamamen dışında, alt veya sağda ayrı Lejant)
3. **Dik Açılı (Orthogonal) Yol Yönlendirme:** Karmaşık eğri spagetti yerine yatay/dikey dik açılı (`M x1,y1 L x2,y1 L x2,y2`, köşelerde hafif `Q` yuvarlama) bağlantılar kullan.
4. **Tek Yönlü Okuma Akışı:** Okuyucunun gözü yorulmasın diye diyagram ya **Soldan Sağa (LR: İnternet → Firewall → VLAN → Servis)** ya da **Yukarıdan Aşağıya (TD: Katmanlı mimari)** akar; iki yönü gelişigüzel karıştırma.
5. **Bilgi Yoğunluğu Sınırı:** Tek bir diyagramda en fazla `12–16` ana düğüm bulunmalı; daha büyük sistemler üst düzey genel bakış + alt katman detay diyagramı olarak bölünür.

---

## ✅ 4. Render Öncesi Görsel QA Kapısı

Bir diyagramı teslim etmeden önce şu 5 kontrolü doğrula:
1. [ ] `viewBox` sınırlarından taşan veya kesilen herhangi bir metin/kutu var mı?
2. [ ] Oklar kutuların arkasında mı ve hat üzerindeki etiketler arka plan maskesiyle net okunuyor mu?
3. [ ] Sıfır ham unicode emoji (`[]` riski yok) — tüm ikonlar temiz SVG vektörü mü?
4. [ ] Kitap modundaysa hem `.svg` hem yüksek çözünürlüklü `.png` üretilip görsel olarak kontrol edildi mi?
5. [ ] Sistem sınırının dışında net bir **Başlık + Lejant** yer alıyor mu?
