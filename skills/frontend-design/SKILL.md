---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces using creative design ideation and perform comprehensive UI/UX, accessibility, design-token, and performance audits on live URLs or local code. Use when building components, pages, or web apps, or when asked to review, audit, inspect, or re-check a website.
---

# Frontend Design & UI/UX Audit Engine

Bu yetenek, arayüz geliştirmeyi ve teknik denetimi üç entegre operasyonel modda yönetir:
1. **MOD A: Yaratıcı Tasarım & Kod Üretimi (Creative Ideation & Build)** — Şablonlaşmış "AI slop" kalıplarından uzak, 10 cesur estetik yönden birine tam bağlı, imza unsuru olan, tipografisi ve renk hikayesi güçlü prodüksiyon kalitesinde arayüzler inşa etmek.
2. **MOD B: Canlı Site Denetim Modu (Live Audit & Profiling)** — Verilen bir web sitesi URL'sini veya yerel kod tabanını inceleyerek erişilebilirlik (A11y), semantik DOM yapısı, tasarım sistemi tokenleri, performans ve dönüşüm mimarisini sayısallaştırıp 1.0-10.0 arası puanlamak.
3. **MOD C: Yeniden Kontrol & Regresyon Doğrulama (Re-Audit / Diff)** — Geliştirmeler yapıldıktan sonra canlı build'i yeniden çekip "Önce / Sonra" delta tablosu ve güncellenmiş skor karnesi sunmak.

---

## MOD A: Yaratıcı Tasarım & Kod Üretimi (Creative Ideation Engine)

Her arayüz çalışmasına butik bir dijital stüdyonun kreatif direktörü gibi yaklaşın. Sıradan SaaS şablonlarına sığınmayın.

### Adım 1: Kullanıcı Talebini Ayrıştırın (Requirements Parsing)
Koda başlamadan önce kullanıcının talebinden şu parametreleri çıkarın:
* **Bileşen / Sayfa Tipi:** (Landing page, gösterge paneli/dashboard, form, kart vb.)
* **Amaç & Kitle:** Bu arayüz hangi problemi çözüyor, hedef kullanıcı kim?
* **Teknik Kısıtlar:** Framework (React, Vue, Vanilla), Stil yaklaşımı (Tailwind, CSS Değişkenleri, CSS-in-JS).
* **Estetik İpuçları:** Kullanıcının belirttiği özel tercihler (koyu tema, minimal, lüks, oyunsu vb.).

### Adım 2: 10 Cesur Estetik Yönden BİRİNE Tam Bağlanın (Commit to ONE)
Tasarımınızda aşağıdaki 10 kavramsal yönden **yalnızca birini** seçin ve tavizsiz uygulayın:

1. **Brutally Minimal:** Aşırı yalınlık, yüksek negatif alan (whitespace), kusursuz tipografik oranlar, sıfır süsleme, cerrahi disiplin.
2. **Maximalist Chaos:** Katmanlı yapılar, zengin dokular, cesur tipografik çakışmalar, yoğun enerji, kontrollü karmaşa.
3. **Retro-Futuristic:** CRT monitör hissi, scanline'lar, neon parlamalar, krom detaylar, retro-fütüristik bilimkurgu estetiği.
4. **Organic / Natural:** Akıcı ve amorf formlar, sıcak toprak tonları, kağıt/taş dokuları, yumuşak geçişler.
5. **Luxury / Refined:** Altın/vizon/şampanya metalik vurgular, zarif serif fontlar, derin koyu arka planlar, yüksek prestij hissi.
6. **Playful / Toy-like:** Belirgin yuvarlatılmış köşeler, canlı ve dopamin renkler, esnek/yaylanan mikro etkileşimler, neşeli hava.
7. **Editorial / Magazine:** Büyük ölçekli dergi tipografisi, dramatik başlık kontrastları, asimetrik ızgaralar, editoryal sayfa akışı.
8. **Brutalist / Raw:** Çıplak grid çizgileri, sert monokrom kenarlıklar, alışılmadık sayfa düzeni, filtrelenmemiş ham endüstriyel yapı.
9. **Art Deco / Geometric:** Simetrik lüks, geometrik desenler, pirinç/altın ışıltısı, Gatsby tarzı zarif 1920'ler modernizmi.
10. **Industrial / Utilitarian:** Yüksek veri yoğunluğu, monospace fontlar, ikaz sarısı/siyah vurgular, saf fonksiyonellik, kokpit arayüzü.

### Adım 3: Temel Yaratıcı Kurallar (Creative Rules)
* **İmza Unsur (Signature Element):** Tasarımı unutulmaz kılan **TEK bir detay** belirleyin (Sayfayı gören biri 24 saat sonra bu tasarımı hangi özelliğiyle hatırlayacak?).
* **Tipografi:** Asla *Inter*, *Roboto*, *Arial* gibi jenerik varsayılanları kullanmayın! Google Fonts kütüphanesinden seçilmiş karakteristik bir **Display/Başlık fontu** ile okunabilirliği yüksek bir **Gövde (Body) fontunu** eşleştirin.
* **Renk Paleti:** 4-6 renkten oluşan tutarlı bir hikaye kurun. Soluk ve her yere eşit dağıtılmış renkler yerine; baskın bir zemin üzerinde keskin bir vurgu (accent) rengi kullanın.
* **Beklenmedik Düzenler (Unexpected Layouts):** Dümdüz 3 kartlık ızgaralar yerine asimetri, örtüşen elemanlar (overlap), dinamik boşluklar ve grid kırılmaları tercih edin.
* **Kesinlikle Yasak Olan "AI Slop" Kalıpları:**
  - ❌ Beyaz zemin üzerinde mor/mavi gradyanlı başlıklar veya butonlar.
  - ❌ Her yerde aynı yuvarlak köşeli, yarı saydam mor kenarlıklı yapay AI kartları.
  - ❌ Standart monoton akış: Hero -> 3 Kart Özellikler -> Fiyatlandırma -> Testimonial.
  - ❌ Anlamı olmayan süsleme amaçlı stok ikon kalabalığı.

### Adım 4: Standart Üretim Çıktı Formatı (Output Schema)
Kod üretirken her zaman şu yapılandırılmış şablonu kullanın:

```markdown
## Design Direction
[Seçtiğiniz estetik yönü ve gerekçesini 2-3 cümlede açıklayın]

## Signature Element
[Bu tasarımda akılda kalacak o TEK imza detayı belirtin]

## Color Palette
- Primary: #hex
- Secondary: #hex
- Accent: #hex
- Background: #hex
- Text: #hex

## Typography
- Display Font: [Google Fonts Font Adı] (örn: 'Cinzel', 'Syne', 'Playfair Display', 'Clash Display')
- Body Font: [Google Fonts Font Adı] (örn: 'Plus Jakarta Sans', 'Cabinet Grotesk', 'Space Grotesk')

## Code
```[html/jsx/vue]
[Eksiksiz, çalışan, tüm CSS değişkenlerini içeren, responsive, animasyonlu ve semantik prodüksiyon kodu]
```
```

### Adım 5: Çoklu Tasarım Keşfi (Multi-Shot Design Exploration)
Kullanıcı alternatifli tasarım istediğinde veya geniş kapsamlı projelerde, aynı anda 2-3 farklı estetik varyant (Örn: *Varyant A: Brutally Minimal* vs. *Varyant B: Retro-Futuristic*) sunarak en iyi yönün seçilmesini sağlayın.

### Adım 6: Tasarım Kalite Kontrol Listesi (Pre-Flight Checklist)
Kodu sunmadan önce şu 8 maddeyi doğrulayın:
* [ ] **Tipografi:** Jenerik font kullanılmadı, Display ve Body fontu amaca uygun seçildi.
* [ ] **Renk:** CSS değişkenleriyle hiyerarşik ve kontrastı WCAG uyumlu bir palet kuruldu.
* [ ] **Düzen:** Monoton grid kalıpları kırıldı, asimetri veya boşluklar amaca hizmet ediyor.
* [ ] **Hareket:** Yükleme, hover ve etkileşim durumları (150-250ms) eksiksiz yazıldı.
* [ ] **Erişilebilirlik:** `:focus-visible`, semantik HTML etiketleri, `aria-*` tanımları hazır.
* [ ] **Duyarlılık (Responsive):** Mobil, tablet ve masaüstünde akıcı çalışıyor.
* [ ] **Eksiksizlik:** Kod parçalı veya `// buraya kod gelecek` gibi yer tutuculu değil; tam ve çalışır durumda.

---

## MOD B: Canlı Site Denetim Modu (Live Audit & Profiling Engine)

Kullanıcı bir web sitesi linki verdiğinde veya arayüzün denetlenmesini istediğinde şu adımları izleyin:

### 1. Canlı Veri Toplama ve Paket Tespiti
* Sayfanın HTML kaynak kodunu, kullanılan CSS ve JS paketlerini (varsa build hash'lerini) tespit edin.
* Güvenlik başlıklarını (HSTS, CSP, X-Frame) ve sayfa ağırlığını inceleyin.

### 2. Sayısal Metrik Denetim Kriterleri
* **Erişilebilirlik (A11y):** `:focus-visible` tanımı, `outline-offset`, klavye atlama bağı (`Skip-link`), `prefers-reduced-motion` medya sorgusu, `aria-*` ve `role=` etiket sayısı, başlık hiyerarşisi (H1-H6 kopuklukları).
* **Semantik & DOM Kalitesi:** `div` enflasyonu, `<header>`, `<main>`, `<article>`, `<nav>`, `<footer>` semantik etiketleri, formların semantik `<form>` ve `<label for="...">` eşleşmesi, inline `style="..."` sayısı.
* **Tasarım Sistemi & Token Hijyeni:** 
  - Kaç farklı `border-radius` değeri var? (Skala 3 temel token'a konsolide mi?).
  - Dağınık piksel fontları (örn: 11px, 12px mikro metinler) ve rem tutarsızlıkları.
  - Dağınık inline renkler.
* **Dönüşüm Mimarisi (CRO):** Tıklanabilir `tel:`, `mailto:`, doğrudan sayfada teklif toplayan `<form>` ve WhatsApp/iletişim tutarlılığı.
* **Performans & Varlıklar:** Görsel formatları (WebP vs JPG), lazy loading dağılımı, JS bundle ağırlığı.

### 3. Standart Raporlama Şablonu
Raporu her zaman şu 4 ana başlık altında sunun:
1. **📊 Ölçüm Tablosu:** Doğrulanan Başarılı Maddeler vs. İyileştirme Alanları.
2. **🔍 Kritik İnce Noktalar:** (Örn: `:focus-visible` içine radius eklenmesinin köşeleri zıplatması, telefon numarası tutarsızlığı, başlık atlamaları).
3. **📈 Güncel Skorlama Karnesi (1.0 - 10.0 Puan):**
   - Erişilebilirlik (A11y)
   - Semantik HTML
   - Performans & Varlıklar
   - Dönüşüm Mimarisi (CRO)
   - Bilgi Mimarisi
   - Tasarım Sistemi & Tokenlar
   - Görsel Kimlik & Estetik
   - **Ağırlıklı Genel Skor**
4. **🎯 En Yüksek Getirili İlk 3 Öncelikli Aksiyon.**

---

## MOD C: Yeniden Kontrol & Regresyon Doğrulama (Re-Audit / Diff Engine)

Kullanıcı *"Düzeltmeleri yaptım, tekrar kontrol et"* dediğinde:
1. **Build / Hash Doğrulaması:** Yeni canlı build'in yayına girip girmediğini kontrol edin (CSS hash, Last-Modified, ETag).
2. **Önce / Sonra Delta Tablosu:**
   `| Kriter / Görev | Önceki Durum | Yeni Canlı Ölçüm | Durum (✅/⚠️/❌) |`
3. **Skor Güncellemesi:** Skorlardaki artışı ve değişimi (Örn: `Erişilebilirlik: 3.0 -> 8.8 ⬆️`) güncelleyin.
4. **Yan Etki Taraması:** Yapılan düzeltmelerin arayüzde yeni bir stil çakışmasına veya bozulmaya yol açıp açmadığını raporlayın.
