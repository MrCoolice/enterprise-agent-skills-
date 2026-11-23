---
name: video-director-engine
description: >-
  Code-rendered video, Reels, talking-head editing, and motion graphics engine (Remotion,
  HyperFrames, 3D Vox/Mapbox maps, shot recipes/film styles, kinetic captions, ElevenLabs
  TTS/SFX, FFmpeg -14 LUFS & cut-list gate). Use when scripting, editing raw talking-head
  footage, or rendering programmatic videos/Reels. Do NOT use for editable .pptx decks (use
  native-pptx-presentations), social post calendars (use social-media-growth), or static
  diagrams (use editorial-architecture-diagrams).
---

# 🎬 Video Director Engine — Premium Motion Design & Remotion Standartları

Bu beceri; **GölgeSiber**, **Dalaman Airport Suites** ve **Oyun Projeleri** için Apple, Linear, Vercel ve Airbnb seviyesinde dünya standardı kod tabanlı video (code-rendered motion design) üretim mimarisini zorunlu kılar.

İlkel slayt gösterileri, düz dikdörtgenler, taşan ve kesilen metinler, bozuk emoji kutuları `[]` ve sabit blok altyazılar **TAMAMEN YASAKLANMIŞTIR.**

---

## 🚫 1. KESİNLİKLE YASAKLANAN İLKEL YÖNTEMLER (ANTI-PATTERNS)

1. **YASAK: Taşan ve Başı/Sonu Kesilen Metinler (Overflow & Clipping):**
   * Hiçbir metin veya altyazı ekran kenarlarından taşamaz veya kesilemez.
   * **Zorunlu Marj:** 1080x1920 dikey tuvalde sol ve sağdan en az **100px güvenli marj** (`max-width: 880px`) bırakılmalıdır.
   * Cümleler ekranda asla tek satırda 10 kelime halinde yığılmaz. `@remotion/captions` standardında **en fazla 2 ila 4 kelimelik mikro-sayfalar (chunking)** halinde sunulur veya otomatik 2 satıra sarılır (`flex-wrap`).
2. **YASAK: Bozuk Emoji Kutuları `[]` (Missing Glyph Box):**
   * Standart fontlarla (Segoe UI, Arial vb.) ham unicode emoji basmak yasaktır; bu fontlar renkli emoji desteklemediğinde ekranda boş kare `[]` basar.
   * Tüm ikonlar (WhatsApp, uçak, anahtar, ay, yıldız, konum) **saf SVG vektörleri, PNG veya Lucide React ikonları** olarak render edilmelidir.
3. **YASAK: Düz 2D Doğrusal (Linear) Hareket:**
   * Hiçbir nesne sabit hızla kayamaz veya tek boyutta hareket edemez. Her hareket yaylanma fiziği (`spring()` — damping: 12, stiffness: 100, mass: 0.8) ve hafif 3D uzamsal derinlik (`perspective(1200px) rotateX`) kullanmalıdır.
4. **YASAK: Python Pillow (PIL) İlkel Çizimleri:**
   * Python Pillow ile kutu çizip metin basmak ilkeldir ve GPU filtrelerini desteklemez. Tüm sahneler modern CSS (Tailwind, Glassmorphism), SVG vektörleri, Three.js ve Remotion React bileşenleriyle oluşturulmalıdır.
5. **YASAK: Sabit Blok Altyazılar & Yavaş Tempo:**
   * Konuşmanın tamamını altta 3 satır sabit metin olarak göstermek yasaktır. Altyazı **Kinetik (Word-by-Word)** olmak, Safe Zone içinde kalmak ve ses temposu **170–200 WPM** (sıfır ölü boşluk) bandında akmak zorundadır.

---

## 💎 2. DÜNYA STANDARDI MOTION DESIGN İLKELERİ

### A. Reels & TikTok Safe Zone ve Otomatik Metin Koruması
* **Üst Bölge (0 - 230 px):** Instagram üst barı için güvenli boşluk.
* **Üst-Orta (230 - 650 px):** Frosted Glassmorphism kanca ve bildirim kartları.
* **Merkez (650 - 1350 px):** Ana görsel ve dinamik rota odağı (Ken Burns mikro yaklaşma).
* **🎯 Altyazı Güvenli Bölgesi (1350 - 1520 px):** Kinetik altyazının konulacağı TEK YER.
* **Alt Bölge (1540 - 1920 px):** Instagram kullanıcı adı, açıklama ve sağ butonlar için temiz bırakılmış karanlık geçiş (vignette).

### B. 3D Harita & Rota Uçuş Standartları (`/map-route` & Vox Style)
*(Kaynaklar: `artemnovitckii/claude-animation-skills`, `iart-ai/map-animation-skills`, `remotion-maps`)*
* **3D Kamera & Pitch (60°):** Kuşbakışı düz 2D harita yerine, 60 derece eğik açılı 3D perspektif kamera kullanılır.
* **Gerçek Uydu / Arazi (Satellite & 3D Terrain):** MapLibre / Mapbox GPU katmanlarıyla gerçek coğrafi doku ve yükseklikler gösterilir.
* **Akıcı Rota & Takip Eden Kamera:** Havalimanı terminalinden otel kapısına giden D555 otoyolu boyunca neon çizgi kendiliğinden akar; kamera hareket eden VIP transfer aracını havadan takip eder (`camera follow`).
* **Varış Rozeti & Ripple Effect:** Hedefe ulaşıldığında 3D zümrüt pini esneyerek haritaya oturur, etrafında genişleyen şeffaf dalga halkaları patlar ve canlı ETA sayacı ("5 dk") kilitlenir.

### C. 2-4 Kelimelik Akıllı Altyazı Bölme (Micro-Pagination / Chunking)
* Cümleler `createTikTokStyleCaptions` mantığıyla parçalanır:
  * ❌ *Hatalı:* `"Doğrudan rezervasyon ve transfer: hotel-suites.example.com"` (Tek satırda 1300px olur, başı sonu kesilir!)
  * ✅ *Doğru (3 Aşamalı Akış):*
    * 1. Kare: `Doğrudan Rezervasyon:` (2 kelime)
    * 2. Kare: `hotel-suites.example.com` (Tekil odak)

### D. 3D Uzamsal Yaylanma Fiziği (Spatial Spring Physics)
* **3D Giriş (Perspective Tilt):** Kart sahneye inerken hafif 3D derinlikle gelir:
  `transform: perspective(1200px) rotateX(6deg) translateY(-20px) scale(0.92);`
* **Esneme (Overshoot):** `spring({ damping: 12, stiffness: 100, mass: 0.8 })` ile hedefini %4 aşar ve yaylanarak `rotateX(0deg) scale(1.0)` konumuna oturur.
* **Kademeli Giriş (Stagger):** Çoklu kartlar birbirinden **4 ila 6 kare** gecikmeyle peş peşe akar.
* **Nefes Alma (Micro-Breathing):** 2 saniyeden uzun ekranda kalan nesneler sinüs salınımıyla (`Math.sin(frame * 0.05) * 1.5%`) nefes alır.

### E. Kinetik Altyazı Elastik Sıçraması (Word-Level Elastic Pop)
* Konuşulan kelime aktif olduğu milisaniyede:
  * **Ölçek:** `%120` sıçrar (`scale: 1.20`),
  * **Renk:** Neon Sarı (`#FFD700`) veya Neon Cyan (`#00F2FE`),
  * **Dış Işıma:** `text-shadow: 0 0 20px rgba(0, 242, 254, 0.85)`.
* Kelime tamamlandığında yumuşakça `%105` seviyesine geri oturur.

### F. Gerçek Buzlu Cam (Frosted Glassmorphism)
* **Arka Plan:** `background: rgba(14, 24, 44, 0.70);`
* **Bulanıklık:** `backdrop-filter: blur(28px) saturate(190%);`
* **Kenarlık:** `border: 1px solid rgba(255, 255, 255, 0.14);`
* **İç Işık:** `box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.20), 0 20px 45px rgba(0, 0, 0, 0.55);`

### G. Ses Temposu ve Ölü Boşluk Temizliği (Audio Pacing & Dead-Air Removal)
* **Reels / TikTok Standart Hızı:** **170 – 200 WPM** (Dakika Başı Kelime).
* **Neural TTS Hız Ayarı:** Edge-TTS veya ElevenLabs gibi motorlarda seslendirme hızı `+22%` ile `+28%` arasına ayarlanmalıdır.
* **Dead-Air / Ölü Boşluk Yasağı:** Cümle sonlarındaki 1 saniyelik yapay duraklamalar kırpılmalı; cümleler arası mikro nefes payı **0.20 - 0.25 saniye** ile sınırlandırılmalıdır.

---

## 🛠️ 3. PRODÜKSİYON TEKNOLOJİ YIĞINI

1. **`artemnovitckii/claude-animation-skills` & HyperFrames (HeyGen):** 3D WebGL / Three.js ve GSAP tabanlı `/map-route` (3D kamera takibi, otomatik rota çizimi, varış pini ve canlı ETA sayacı) ve `/breakdown` (3D patlatılmış görünüm) motoru.
2. **`iart-ai/map-animation-skills`:** Vox tarzı editoryal harita animasyonları; MapLibre/Mapbox GPU 3D terrain kabartması, uydu zemini, dinamik yörünge (orbit) kamera geçişleri ve bölgesel sınır parlamaları.
3. **Remotion CLI, Programmatic API (`@remotion/renderer`), NullMotion & Çekim/Stil Katalogları:** Webpack + React tabanlı GPU hızlandırmalı video motoru; sinematik sahne tarifleri ve 150 hazır Remotion hareket kalıbı için **`Vincentwei1021/video-shotcraft` (124 shot recipes)**, **`blixvip/NullMotion`** (After Effects/Lottie hassasiyetinde sıfır bağımlılıklı saf Bezier/Spring eğrileri ve SVG/Canvas mikro-animasyonları) ve 15 farklı görsel estetik kategorisinde (kinetik tipografi, veri hikâyesi, terminal/kod vitrini, ürün lansmanı) kod tabanlı film dili seçimi için **`lemomo-ai/lemo-opuscar` (99 film style archetypes)** kalıplarını storyboard aşamasında referans al.
4. **`@remotion/captions` (`createTikTokStyleCaptions`):** Kelime zaman damgalarını akıllı 2-4 kelimelik mikro-sayfalara bölen resmi Remotion kütüphanesi.
5. **SVG & Lucide Vektör Motoru:** Emojileri bozuk karakter kutularından `[]` kurtaran saf vektör ikon katmanı.
6. **Whisper / Edge-TTS & Resmi `elevenlabs/skills` Ses Motoru:** Milisaniye hassasiyetli `WordBoundary` zaman damgaları; doğal seslendirme (`eleven_v4` TTS veya Edge-TTS), zaman damgalı/konuşmacı ayrımlı transkript (**Scribe STT** / Whisper) ve sahne geçişleri, ortam atmosferi, UI/whoosh vurgu efektleri için **`elevenlabs/skills` (`sound-effects`)** + FFmpeg **`-14 LUFS`** miksaj (ses efekti arka planı konuşmanın `-18` ila `-24 dB` altında tutulur).

---

## 🎯 4. PREMİUM KALİTE KONTROL KAPISI (QA GATE)
Video render edilmeden önce şu sorulara **"EVET"** denmek zorundadır:
1. [ ] Hiçbir metnin başı veya sonu ekrandan taşmıyor veya kesilmiyor mu (min 100px kenar marjı korundu mu)?
2. [ ] Ekranda hiçbir yerde içi boş `[]` emoji/glif hatası yok mu (tüm ikonlar SVG mi)?
3. [ ] Altyazılar 2-4 kelimelik dinamik mikro-sayfalar halinde sese göre yaylanarak mı akıyor?
4. [ ] Harita sahnesi 3D izometrik eğik açıyla (`/map-route` & Vox stili), kameranın aracı takip ettiği ve neon rotanın aktığı şekilde mi kurgulandı?
5. [ ] Alt 380 piksellik Instagram UI alanı temiz bırakıldı mı?
6. [ ] Konuşma hızı 170-195 WPM aralığında ve cümle araları ölü boşluksuz (max 0.25s) mu?
7. [ ] Ham kamera önü (talking-head) kurgusuysa: ses **-14 LUFS** normalize edildi mi ve render öncesi **Kesim Listesi (Cut-List)** kullanıcı onayından geçti mi?

---

## 🎙️ 5. KAMERA ÖNÜ (TALKING-HEAD) HAM VİDEO KURGU PROTOKOLÜ
*(social-media-skills/video-editing-skill metodolojisinden uyarlanmıştır)*

Kodla sıfırdan animasyon üretmek yerine, kullanıcının kameraya konuştuğu ham kayıtlar (YouTube rehberleri, yüzlü Reels, kurs/podcast çekimleri) kurgulanacağında şu **5 adımlı yerel FFmpeg/Whisper akışını** uygula:

1. **Kelime Bazlı Transkript & Hata Tespiti:** Ham videodan Whisper ile kelime zaman damgalı transkript çıkar. Uzun sessizlikleri (>0.45s), dolgu seslerini (*"ııı", "eee", "şey"*), takılmaları ve **bozuk tekrarları (retake — yalnızca son temiz çekimi koru)** işaretle.
2. **Zorunlu Kesim Listesi Onay Kapısı (Cut-List Gate):** Hiçbir FFmpeg kesim/render işlemine geçmeden önce çıkarılacak zaman aralıklarını ve toplam kazanılan süreyi tablo olarak kullanıcıya sunup **onay al**.
3. **Jump-Cut Maskeleme (Akıllı Punch-In):** Arka arkaya yapılan sert kesimlerde görsel sıçramayı gizlemek için kesim noktalarında mikro ölçekleme (%108–%112 crop/punch-in) veya B-roll/ekran görüntüsü geçişi öner.
4. **Yayın Standardı Ses Temizliği & Normalizasyon:** Arka plan gürültüsü temizliği (highpass/afftdn) + **`loudnorm` ile -14 LUFS** (True Peak `-1.5 dBTP`) ses seviyesi sabitlemesi uygula.
5. **Çoklu Çıktı Paketi:** Kurgulanan ana videoyla birlikte zaman damgalı **`.srt` altyazı dosyası** (2-4 kelimelik kinetik bölünmeye hazır) ve uzun videolarda **YouTube Bölüm Zaman Damgaları (Chapters)** üret.

---

## 🚀 6. ÜRÜN LANSMANI & DEMO VİDEO PROTOKOLÜ (`/brag` & `latent-spaces/brag`)

SaaS, homelab projesi veya açık kaynak araç lansmanı için (Product Hunt, X/Twitter video lansmanı, GitHub README video demosu):

1. **30 Saniyelik Hızlı Hook (0-5s):** Problemi canlı terminal hatası veya hantal arayüz acısıyla göster.
2. **"Before/After" Çözüm Flaşlaması (5-15s):** Yeni sistemin (GölgeSiber / Remotion / Next.js) sıfır gecikmeyle nasıl çalıştığını Split-Screen veya hızlı Punch-In ile göster.
3. **Özellik Fırtınası (Feature Storm 15-25s):** 3-4 kilit avantajı `NullMotion` yaylanma eğrileriyle fırlat (Kartlar 6 kare stagger ile akar).
4. **Güçlü Call to Action (25-30s):** Canlı URL, GitHub repo yıldız çağrısı ve net son kart. Arkada `-14 LUFS` bas davul ve whoosh ses efekti.
