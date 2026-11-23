---
name: editorial-web-design-studio
description: >-
  Anti-AI-slop art direction, DESIGN.md systems, live URL computed-CSS reverse-engineering,
  selective feature rebuild, motion/react animations, Driver.js onboarding tours, SVG logos,
  favicons/OG packs, and Web Audio UI micro-sounds (with Chrome DevTools & Mobbin). Use when
  designing distinctive editorial websites or extracting a reference URL's design DNA. Do NOT
  use for CWV/Next.js 16/Prisma backend engineering (use web-quality-modern-guidance) or
  technical diagrams (use editorial-architecture-diagrams).
---

# 🎨 Editoryal Web Tasarım Stüdyosu, Anti-AI-Slop & URL Tasarım DNA'sı Becerisi

Bu beceri; **anthropics/skills (`frontend-design`)**, **Leonxlnx/taste-skill**, **pbakaus/impeccable**, **nextlevelbuilder/ui-ux-pro-max-skill**, **uxKero/anydesign**, **senlindesign/taste-skill**, **bergside / jpoindexter (`DESIGN.md` computed-CSS çıkarımı)** ve **qCanoe / JCodesMore** sistemlerini tek bir **Sanat Yönetmenliği & Referans Site Çözümleme Stüdyosunda** birleştirir.

> **Kapsam Sınırı:** Bu beceri **görsel sanat yönetmenliği, Anti-AI-Slop estetik, `DESIGN.md` tasarım anayasası ve referans URL'den özellik/tasarım DNA'sı sökme** içindir. Kodun Core Web Vitals, Next.js 16/React 19, Strict TS/Zod ve Prisma/SQLite mühendisliği için `web-quality-modern-guidance`, teknik mimari diyagramlar için `editorial-architecture-diagrams` kullanılır.

---

## 🚫 1. Kesin "AI Slop" Yasağı (`anthropics/frontend-design`, `pbakaus/impeccable` & `Nutlope/hallmark`)

Kod yazarken bir sayfanın *"yapay zekâ şablonu"* gibi görünmesine yol açan şu 7 klişe ve **Hallmark "The Floor" linter kuralları** kesinlikle zorunludur:
1. **Jenerik Mor/Lacivert Neon Gradyanlar & Klişe Glow Yığını:** Marka kimliğine dayanmayan varsayılan `#6366f1 → #a855f7` gradyanları kullanma.
2. **Varsayılan `Inter` / `Roboto` / `Arial` Tekdüzeliği:** Karakterli, eşleşmiş editoryal tipografi çiftleri kullan (ör. belirgin Display başlık + rafine gövde + teknik değerlerde monospace; harici link yerine `next/font`).
3. **Birbirinin Aynısı 3'lü Eşit Kart Izgaraları:** Her bölümü 3 aynı kutu + üstünde küçük Lucide ikon + 2 satır metin şeklinde tekrarlama; **asimetrik Bento, editoryal bölünmüş düzen (split layout), tam genişlik tipografik bantlar** kullan.
4. **Sahte Metrik, Logo Duvarı & Süs Rozeti Yasağı (`Nutlope/hallmark`):** Doğrulanmamış sahte sayaçlar (*"10.000+ mutlu müşteri"*, *"99.99% uptime"* uydurmaları), içi boş marka logo şeritleri ve süs amaçlı durum hapları (*"✨ AI-Powered"*, *"New"*) kesinlikle yasaktır; tüm renk/fontlar `:root` CSS token'larına bağlı ve görünür klavye odak halkası (`focus-visible`) eksiksiz olmalıdır.
5. **Sahte Görsel / Stok Klişeleri & Kutu İçinde Kutu:** Gereksiz iç içe kart/gölge yığınları yerine negatif alan (boşluk), keskin `1px` saç çizgisi sınırlar (hairline borders) ve gerçek ürün/mekân fotoğrafları kullan.
6. **Anlamsız Hareket Kirliliği & `framer-motion` (`motion/react`) Disiplini:** Her elemanın aynı anda aşağıdan yukarı `fade-in` kayması yasaktır. React/Next.js 16 projelerinde rafine layout geçişleri (`layoutId`), jestler (`whileHover`/`whileTap`), scroll bağlı efektler (`useScroll`/`useTransform`) ve `AnimatePresence` için **`motion/react`** kullan; yalnızca GPU katmanlı özelliklere (`transform`, `opacity`) dokun, izole `"use client"` yaprak bileşeninde tut ve `<MotionConfig reducedMotion="user">` ile `prefers-reduced-motion` uyumunu zorunlu kıl.
7. **Birebir Telif Kopyası Yasağı:** Referans URL'den asla başka bir markanın logosunu, metnini veya telifli fotoğrafını kopyalama; yalnızca **tasarım mimarisini, etkileşim mantığını ve seçilen UX özelliklerini** kendi marka kimliğine özgünleştir.

---

## 🎛️ 2. Mod A: Sıfırdan Modern & Sanatsal Tasarım (Koddan Önce Sanat Yönetmenliği)
*(Leonxlnx/taste-skill + nextlevelbuilder/ui-ux-pro-max-skill + kurulu Mobbin)*

Hiçbir HTML/TSX kodu yazmadan önce kullanıcıya kısa bir **Tasarım Manifestosu (`DESIGN.md` / `MASTER.md`)** sun:

1. **Tek Satırlık Sanat Yönetmenliği Kararı (One-Line Read):** Projenin ruhu ve benzersiz estetik yönü (ör. *"GölgeSiber: İsviçre ızgaralı koyu editoryal siber terminal"*, *"Dalaman Suites: Sıcak Ege traverteni, sessiz Akdeniz lüksü"*).
2. **3 Estetik Kadran Ayarı (`1–10`):**
   - **`DESIGN_VARIANCE`** *(1 = muhafazakâr/kurumsal, 8–10 = cesur asimetrik/sanatsal editoryal)*
   - **`MOTION_INTENSITY`** *(1 = neredeyse statik, 7–9 = rafine mikro-etkileşimler ve akışkan geçişler)*
   - **`VISUAL_DENSITY`** *(1 = bol beyaz alan / müze ferahlığı, 8–10 = bilgi yoğun kokpit/dashboard)*
3. **Tasarım Anayasası (`DESIGN.md`):**
   - **Renk Mimarisi:** 1 ana zemin, 1 yüzey tonu, 1 yüksek kontrast metin, **en fazla 1–2 kasıtlı vurgu rengi** (60/30/10 kuralı).
   - **Tipografi Ölçeği:** Display H1 (`clamp()`), H2/H3, gövde, mikro-etiket (uppercase tracking) ve sayısal/kod tabular rakamları (`tabular-nums`).
   - **Gerçek Ürün Referansı (Mobbin):** Gerekirse kurulu **Mobbin** (`search` / `redesign-screen`) ile gerçek dünya lider uygulamalarının aynı ekranı nasıl çözdüğünü incele.

---

## 🔎 3. Mod B: Referans Site URL ➔ Tasarım DNA'sı & Seçmeli Özellik Dökümü
*(uxKero/anydesign + senlindesign/taste-skill + bergside/jpoindexter + qCanoe + kurulu Chrome DevTools)*

Kullanıcı bir site linki verip *"Bu sitenin özelliklerini dök, seçtiklerimi bana yap"* dediğinde şu **4 aşamalı protokolü** çalıştır:

### Aşama 1: Canlı Tarayıcı İncelemesi (Kurulu Chrome DevTools ile)
- Hedef URL'yi masaüstü (`1440x900`) ve mobil (`390x844`) boyutlarında açıp **gerçek computed CSS** değerlerini (aktif font ailesi, başlık/gövde boyutları, `line-height`, arka plan/vurgu renkleri, `border-radius`, `max-width`, grid/flex yapısı, gölge/cam efektleri) ve sayfa bölümlerini analiz et.

### Aşama 2: 7 Bölümlü Tasarım DNA'sı & Özellik Döküm Raporu (`DESIGN.md`)
1. **Estetik & Zevk Analizi (`senlindesign` "Neden?" Okuması):** Bu site neden kaliteli/özgün görünüyor? Hangi kısıtlamalar onu temiz tutuyor?
2. **Renk & Kontrast Token'ları:** Hex/OKLCH paleti + W3C DTCG uyumlu CSS değişkenleri.
3. **Tipografi Sistemi:** Kullanılan font çifti, ölçek oranı, satır yüksekliği ve harf aralığı.
4. **Izgara (Grid), Boşluk & Kart Geometrisi:** Konteyner genişliği, bölüm aralıkları, köşe yarıçapı ve kenarlık dili.
5. **Numaralandırılmış Özellik & Bölüm Envanteri (Seçim Menüsü):**
   - `[1]` Navigasyon & Sticky Davranış • `[2]` Hero Kompozisyonu • `[3]` Sosyal Kanıt / Güven Şeridi • `[4]` Bento / İnteraktif Özellik Vitrini • `[5]` Fiyatlama / Dönüşüm Kartı • `[6]` SSS / Footer • `[7]` Özel Araçlar / Filtreler / Arama.
6. **Mikro-Etkileşimler & Hareket Dili:** Hover, scroll reveal, tab/drawer geçişleri, klavye kısayolları.
7. **Dönüşüm (CRO) & Psikolojik Kancalar:** CTA yerleşimi, kontrast odağı ve mobil ilk ekran (above-the-fold) stratejisi.

### Aşama 3: Seçmeli Onay Kapısı (Kullanıcı Seçimi)
- Kodlamaya geçmeden önce kullanıcıya numaralı listeyi sun: *"Bu özelliklerden hangilerini (`örn. 1, 3, 5`) kendi markana ve yığınına (`Next.js 16 + Tailwind` veya `FastAPI/HTML`) özgünleştirerek inşa edelim?"*

### Aşama 4: Özgünleştirerek İnşa & Acımasız Eleştiri (`pbakaus/impeccable`)
- Seçilen özellikleri kendi markanın renk/font/içerik DNA'sıyla kodla (`web-quality-modern-guidance` performans standartlarına uyarak).
- Teslim etmeden önce kendi çıktını **Chrome DevTools** ile `390x844` ve `1280x800` ekranlarda açıp **eleştiri/cila (critique → polish)** turundan geçir: hizalama, boşluk simetrisi, kontrast, mobil taşma ve sıfır AI-slop teyidi!

---

## 🏷️ 4. Logo, Favicon / PWA / `og:image` Paketi & Web UI Mikro-Sesleri
*(kaankiziltug/logo-design-skill, rampstackco/brand-identity, jezweb/favicon-gen & open-design/brand-extract standartlarından uyarlanmıştır)*

### A. Geometrik SVG Logo & Tam Favicon / Sosyal Kart Paketi
1. **Saf SVG Logo İnşası:** İnce karmaşık detaylar yerine temel geometrik yapıyla (`viewBox="0 0 64 64"`), optik hizalamayla ve **tek renk (monochrome) + koyu/aydınlık zemin** uyumuyla tasarla.
2. **16px / 32px Okunabilirlik Kapısı:** Her logo ikonu `16x16px` tarayıcı sekmesinde (favicon) bulanıklaşmadan ayırt edilebilir olmalıdır; gerekirse küçük boyut için sadeleştirilmiş monogram (`mark`) üret.
3. **Eksiksiz Web Varlık Çıktısı:** Bir site için marka paketi istendiğinde şu tam seti üret/doğrula:
   - `favicon.svg` (koyu/aydınlık tema destekli `@media (prefers-color-scheme: dark)`), `favicon.ico` (`16x16` + `32x32`), `apple-touch-icon.png` (`180x180`), PWA `icon-192.png` + `icon-512.png`, `site.webmanifest` ve **`og-image.png` (`1200x630`, sosyal medya/WhatsApp paylaşım önizleme kartı)**.

### B. Web Arayüzü Mikro-Sesleri (Sıfır Bağımlılık — Web Audio API)
Sitede veya etkileşimli araçlarda rafine dokunsal ses geri bildirimi istendiğinde (ağır MP3 yüklemeden):
1. **Prosedürel Web Audio Sentezi:** Kısa (`30–120ms`), düşük genlikli (`gain <= 0.08`) yumuşak klik, onay tınısı veya sayfa geçiş sesi üret; `AudioContext`'i yalnızca ilk kullanıcı etkileşiminde (click/keydown) başlat (tarayıcı autoplay politikası).
2. **Sessiz Varsayılan & Erişilebilirlik:** Web sitelerinde ses **asla kullanıcı izni olmadan yüksek sesle otomatik çalmaz**; görünür sessize alma (`Mute/Sound Toggle`) düğmesi ve `prefers-reduced-motion` uyumu zorunludur. *(Video/Reels SFX ve ElevenLabs seslendirme için `video-director-engine`, oyun ses efektleri için `quiz-word-game-master` kullanılır.)*

### C. İlk Ziyaretçi İnteraktif Ürün Turu (`Driver.js` Onboarding Spotlight)
Çok araçlı portallarda (`golgesiber-v3` 22+ siber araç, `booking-whatsapp-bot` 3 sekmeli ortak paneli, `golgesiber-dashboard`) ilk gelen kullanıcıya siteyi 20 saniyede tanıtmak için sıfır bağımlılıklı **`driver.js`** (~5 KB) kullan:
1. **Next.js 16 / SSR Güvenliği:** Daima izole bir **`"use client"`** yaprak bileşeninde (`OnboardingTour.tsx`), yalnızca `useEffect` içinde veya **"Turu Başlat (?)"** butonuna tıklanınca `driver()` çağır; `driver.js/dist/driver.css` temasını sitenin `:root` renk token'larıyla özelleştir.
2. **Kullanıcıyı Boğmayan Akış:** En fazla **4–6 net adım**, `showProgress: true`, `allowClose: true` (`Esc`/dış tıklama ile anında çıkış), `localStorage` (`tour_v1_seen`) ile yalnızca ilk ziyarette otomatik tetikleme ve mobilde (`<640px`) hedeflerin ekran dışına taşmadığını Chrome DevTools ile doğrula.

---

## 💎 5. UI/UX Pro Max & Emil Kowalski "Taste Skill" (Tasarım Zekâsı ve Ritim Motoru)
*(Kaynaklar: `nextlevelbuilder/ui-ux-pro-max-skill`, `tasteskill.dev`, `emilkowal.ski/skill`)*

Yapay zekanın "jenerik, ruhsuz ve şablon" arayüzler üretmesini tamamen engelleyen dünya standardı tasarım zevki (taste) disiplini:

1. **4px / 8px Katı Ritim & Optik Merkezleme:**
   * Tüm margin, padding, gap ve yükseklik değerleri katı `4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px` ölçeğine oturmalıdır. Rastgele `13px`, `27px` gibi değerler yasaktır.
   * İkonlar ve metinler yan yana geldiğinde matematiksel merkez yerine **optik merkezleme** (ikonun görsel ağırlığına göre `translateY(-0.5px)` veya font baseline ayarı) yapılır.
2. **Akışkan (Fluid) Tipografi & Oranlar:**
   * Başlık ve gövde metinlerinde sabit piksel yerine akıcı clamp fonksiyonları kullanılır:
     `font-size: clamp(1.75rem, 1.25rem + 1.8vw, 2.75rem); line-height: 1.15; letter-spacing: -0.02em;`
3. **Dokunsal (Tactile) Mikro-Etkileşimler (Emil Kowalski Standartları):**
   * Buton tıklamalarında sert geçiş yerine hafif baskı (`scale: 0.98`), hover durumunda yaylanmalı yükselme (`transform: translateY(-2px)` + `transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1)`).
   * Modallar ve çekmeceler (Drawers) sahneye girerken fiziksel kütle hissi veren sönümlemeli yay (damping spring) eğrileriyle açılır.
4. **Gerçek Tarayıcı Cila Kapısı (Real-Browser Taste Check):**
   * Kod yazımı bittikten sonra çıktı Chrome DevTools ile incelenir: Görsel hiyerarşide en önemli tek bir eylem (Primary CTA) parlamalı; ikincil eylemler sessiz (ghost/outline) kalmalıdır.

---

## ⚡ 6. Google Labs "Stitch Skills" (Hızlı Wireframe/HTML Dönüştürücü)
*(Kaynak: `google-labs-code/stitch-skills`)*

Kaba bir HTML taslağı, wireframe çizimi veya harici ham DOM bloğu paylaşıldığında:
1. **Semantik & Tip Güvenli Bileşen Dönüşümü:** Ham `div` yığınlarını `<header>`, `<main>`, `<section>`, `<article>`, `<aside>` etiketlerine ve katı TypeScript arayüzlerine (`interface Props`) dönüştür.
2. **Tailwind & shadcn/ui Enjeksiyonu:** Satır içi (inline) CSS stillerini sitenin mevcut Tailwind CSS token'larına ve `cn()` yardımcı fonksiyonuna (`clsx` + `tailwind-merge`) uyarla.
3. **Görsel & Erişilebilirlik Hijyeni:** Tüm butonlara görünür `:focus-visible` halkası (`ring-2 ring-emerald-500/50 ring-offset-2`), interaktif alanlara `min-h-[44px]` dokunma hedefi ve dekoratif ikonlara `aria-hidden="true"` ekle.
