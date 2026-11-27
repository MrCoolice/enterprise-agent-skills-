---
name: audiophile-music-curator
description: >
  Autonomous music library curation, 500x500 ID3v2.3 cover embedding, LRCLIB synced lyrics, 15-genre routing, zero-duplicate guard, and automotive FAT32/MBR USB mirror sync for Opel IntelliLink and Nextcloud.
---

# Audiophile Music Curator & Automotive Library Ops

Bu skill; yerel ve bulut tabanlı müzik kütüphanelerinin (`Nextcloud\Music`), araç içi bilgi-eğlence sistemlerinin (özellikle **Opel IntelliLink R4.0**) ve odyofil koleksiyonlarının kusursuz şekilde yönetilmesi, indirilmesi, ses seviyesi dengelenmesi (-14 LUFS), etiketlenmesi, mükerrer önleme (deduplication) filtrelemesi, akıllı kademeli model kullanımı ($0 Local-First & Graceful Fallback) ve senkronize edilmesi için tasarlanmış yüksek verimli operasyon rehberidir.

---

## 1. Hızlı Komutlar (Slash Commands)

| Komut | Açıklama |
| :--- | :--- |
| `/music-sync` | Nextcloud ile bağlı olan USB belleği (`CORSA_MUZIK`) ayna modunda senkronize eder. |
| `/music-add <sorgu / link>` | Şarkıyı/albümü kütüphaneyi tarayıp mükerrer kontrolü yaparak 320k MP3 kalitesinde indirir, 500x500 kapak ve sözleri gömer, uygun klasöre atar. |
| `/music-normalize` | Kütüphaneyi EBU R128 (-14 LUFS) standardına göre tarar; arabada kısık veya aşırı patlayanları dengeler. |
| `/music-audit` | Kütüphaneyi tarar; eksik kapak, eksik söz, mükerrer şarkı ve dosya adı hatalarını raporlar. |
| `/music-recommend` | Kütüphanede ZATEN BULUNAN parçaları hariç tutarak sadece yeni ve taze öneriler sunar (Varsa yerel Ollama, yoksa bedava fallback). |

---

## 2. Ses Mühendisliği & Akustik Standartları (Audiophile Grade)

Otomobil kabini (65-72 dB yol gürültüsü) ve ev ses sistemleri için uygulanan katı ses standartları:

1. **Bitrate ve İndirme Standardı:**
   - **Hedef Kalite:** **320 kbps CBR** (Constant Bitrate) veya **VBR V0**.
   - **Taban Kuralı:** Kütüphaneye kesinlikle **192 kbps altı ses dosyası kabul edilmez**. Mümkün olan en yüksek kaliteli stüdyo master veya Vevo/Topic akışı tercih edilir.
2. **Ses Seviyesi & Dinamik Dengeleme (-14 LUFS / EBU R128):**
   - **Hedef Entegre Ses Şiddeti (Integrated Loudness):** **-14.0 LUFS** (Otomotiv, Spotify ve Apple Music küresel yayın standardı).
   - **True Peak Sınırı:** **-1.5 dBFS** (Araç DAC ünitesinde inter-sample clipping ve dijital distorsiyonu önler).
   - **Cerrahi Koruma Kuralı:** Zaten sağlıklı ses aralığında olan (-18 ile -9 LUFS arası) parçaların dijital orijinalliğine dokunulmaz. Yalnızca arabada yol gürültüsünde kaybolan (< -18 LUFS) veya kulak patlatan (> -9 LUFS) parçalar dengelenir.

---

## 3. Otomobil & Donanım Standartları (Opel IntelliLink Kriterleri)

IntelliLink R4.0 ve benzeri araç multimedya üniteleri katı donanım kurallarına sahiptir:

1. **MBR Bölüntü Tablosu:** Disk kesinlikle **GPT olamaz**. Mutlaka **MBR (Master Boot Record)** olarak ilklendirilmelidir (`diskpart -> clean -> convert mbr`).
2. **FAT32 Dosya Sistemi:** USB bellek <= 32 GB olmalı ve `FAT32` formatında biçimlendirilmelidir. Varsayılan hacim etiketi: `CORSA_MUZIK`.
3. **Kapak Görseli Kuralı:** Maksimum **500x500 piksel**, kare, JPEG formatında ve **ID3v2.3 `APIC`** tag'i olarak gömülmelidir (ID3v2.4 veya aşırı büyük/progressive JPEG'ler ekranda siyah kalır).
4. **Şarkı Sözü:** `USLT` (Unsynchronized Lyrics) veya LRCLIB senkronize tag formatında eklenir.
5. **Karakter Güvenliği:** Dosya ve klasör adlarında Türkçe karakterler korunabilir; ancak `:`, `*`, `?`, `"`, `<`, `>`, `|` gibi geçersiz karakterler ve çift boşluklar mutlaka temizlenmelidir.
6. **Yol Uzunluğu:** Dosya yolu uzunluğu araç hafızasını korumak için 128 karakteri geçmemelidir.

---

## 4. 15 Tematik Kategori Matrisi

Kütüphane aşağıdaki 15 odaklı klasör yapısına göre kategorize edilir:

| No | Klasör Adı | Tanım & Temsili Sanatçılar |
| :---: | :--- | :--- |
| `01` | `01_POWER_ENERGY` | Hızlı, tempolu parçalar (HammerFall, Five Finger Death Punch, Arch Enemy). |
| `02` | `02_DARK_MELANCHOLY` | Melankoli & Hüzün (Katatonia, Anathema, Mad Season, Alice in Chains, Portishead). |
| `03` | `03_EPIC_FANTASY` | Senfonik & Epik Metal (Blind Guardian, Nightwish, Avantasia, Savatage, Almora). |
| `04` | `04_SOFT_CHILL` | Akustik & Gece Sürüşü (Dire Straits, Pink Floyd, Gary Moore, Camel, Chris Rea, Frank Sinatra). |
| `05` | `05_TURKCE_ROCK_RAP` | Türkçe Rock / Rap Klasikleri (Kargo, Mor ve Ötesi, Duman, Hayko Cepkin, Kurban, Pentagram). |
| `06` | `06_DOOM_GOTHIC_METAL` | Doom, Death & Gothic (My Dying Bride, Draconian, Paradise Lost, Type O Negative, Tiamat). |
| `07` | `07_ROCK_HEAVY_METAL` | Heavy Metal & 90s Rock (Iron Maiden, Black Sabbath, Judas Priest, Nevermore, Testament, Saxon). |
| `08` | `08_SYNTH_ELECTRO_POP` | 80s Pop & Atomic Blonde (New Order, Depeche Mode, Alphaville, Nena, Laura Branigan). |
| `09` | `09_FILM_OYUN_SOUNDTRACK`| Film & Oyun Müzikleri (Metal Gear Solid, 28 Days Later, The Hobbit, Escape from L.A.). |
| `10` | `10_KARISIK` | Marşlar ve Özel Tarihi Kayıtlar. |
| `11` | `11_SYNTHWAVE_OUTRUN` | Retrowave & Outrun (Kavinsky, The Midnight, FM-84, GUNSHIP, Dance With the Dead). |
| `12` | `12_CYBERPUNK_DARK_TECHNO`| Cyberpunk & Midtempo (Gesaffelstein, Rezz, Carpenter Brut, Perturbator, Daniel Deluxe). |
| `13` | `13_ANADOLU_PSYCHEDELIC` | Anadolu Pop/Rock & Psychedelic (Derindekiler, Berrin Keskin, Altın Gün, Derya Yıldırım). |
| `14` | `14_GYM_WORKOUT` | Ağırlık, Power, PR, Drop-set, Yüksek Agresyon (Five Finger Death Punch, Arch Enemy, Mick Gordon). |
| `15` | `15_CYCLING_CARDIO` | Bisiklet, 120-135 BPM Akıcı Kadans, Gece & Yol Sürüşü (FM-84, The Midnight, Daniel Deluxe, Kavinsky). |

---

## 5. Mükerrer Önleme ve Parmak İzi Filtresi (Zero-Duplicate Guard)

Kütüphanenin bütünlüğünü korumak ve disk/hafıza israfını önlemek için şu katı kurallar uygulanır:

1. **Tavsiye Öncesi Kütüphane Taraması (Anti-Echo):**
   - Asistan veya yerel LLM müzik önerisi (`/music-recommend`) yapmadan önce kütüphanedeki tüm klasörleri tarar ve mevcut şarkıların parmak izini (normalize edilmiş Sanatçı - Başlık) çıkarır.
   - **Kütüphanede zaten var olan hiçbir şarkı ASLA yeni öneri olarak sunulamaz.** Kullanıcıya sadece kütüphanesinde bulunmayan taze cevherler tavsiye edilir.
2. **İndirme Öncesi Mükerrer Engeli (No Redundant Downloads):**
   - `/music-add` veya otomatik indirme tetiklendiğinde, hedeflenen parça adı fuzzy matching ile tüm kütüphanede taranır.
   - Eğer şarkı başka bir klasörde zaten varsa, **indirme derhal engellenir** ve kullanıcıya bildirilir: *"Bu şarkı zaten [Klasör Adı] altında mevcut, tekrar indirilmedi."*
3. **Aktivite Klasörleri Disiplini:**
   - `14_GYM_WORKOUT` ve `15_CYCLING_CARDIO` gibi amaca özel derleme klasörlerine mevcut kütüphaneden seçilen parçalar yerel olarak kopyalanabilir; ancak internetten yeni bir şarkı indirilecekse bu şarkı kütüphanenin başka hiçbir klasöründe bulunmamalıdır.

---

## 6. Akıllı Kademeli Model Hiyerarşisi ($0 Local-First & Graceful Fallback)

Asistan müzik analizi, zevk modelleme ve öneri üretirken şu 3 kademeli hiyerarşiye kesin olarak uyar:

1. **Tier 1 (Öncelikli - Varsa): Yerel RTX 4070 / Ollama (`http://127.0.0.1:11434`)**
   - Asistan önce yerel Ollama API'sini yoklar.
   - Eğer servis açıksa; kütüphane özeti doğrudan yerel **`deepseek-r1:14b`** veya **`qwen2.5-coder:14b`** modeline gönderilir. İşlem %100 yerel donanımda, sınırsız ve $0 maliyetle tamamlanır.
2. **Tier 2 (Yedek - Kapalıysa): Antigravity Bedava Alt Ajan (`flash_lite`)**
   - Eğer Ollama kapalıysa (`ConnectionRefused` vb.), sistem kesinlikle hata verip durmaz.
   - Otomatik olarak Antigravity bünyesindeki ücretsiz **`flash_lite`** alt ajanına devreder ve analizi yine $0 maliyetle bitirir.
3. **Tier 3 (Kırmızı Çizgi Kuralı): Sıfır Paralı API Garantisi**
   - Harici ücretli servisler (OpenAI, Spotify Developer API, Claude vb.) kesinlikle çağrılmaz. Her operasyon daima ücretsiz yerel veya dahili araçlarla çözülür.

---

## 7. Master Kaynak & Kalıcı Silme Kuralı (Single Source of Truth)

1. **Mutlak Ana Merkez:** `C:\Users\devops-engineer\Nextcloud\Music` kütüphanenin tek ve resmi kaynak dizinidir (Single Source of Truth).
2. **Kalıcı Silme İlkesi (No Zombie Files):** Kullanıcı `Nextcloud\Music` klasöründen bir şarkıyı sildiğinde, o şarkı kalıcı olarak silinmiş kabul edilir. Hiçbir otonom işlem silinen parçaları asla tekrar indiremez veya geri getiremez.
3. **USB Ayna Silme (True Mirror Sync):** `/music-sync` veya `sync_usb.py` çalıştırıldığında, kaynakta silinmiş olan tüm dosyalar USB bellekten de otomatik olarak kaldırılır (`orphan cleanup`).
4. **Onaysız İndirme Yasağı:** Ajan, kullanıcı açıkça isim/bağlantı verip *"ekle"* demedikçe kendi inisiyatifiyle hiçbir yeni parça indiremez.
