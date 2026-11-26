---
name: audiophile-music-curator
description: >
  Autonomous music library curation, 500x500 ID3v2.3 cover embedding, LRCLIB synced lyrics, 13-genre routing, and automotive FAT32/MBR USB mirror sync for Opel IntelliLink and Nextcloud.
---

# Audiophile Music Curator & Automotive Library Ops

Bu skill; yerel ve bulut tabanlı müzik kütüphanelerinin (`Nextcloud\Music`), araç içi bilgi-eğlence sistemlerinin (özellikle **Opel IntelliLink R4.0**) ve odyofil koleksiyonlarının kusursuz şekilde yönetilmesi, indirilmesi, ses seviyesi dengelenmesi (-14 LUFS), etiketlenmesi ve senkronize edilmesi için tasarlanmış yüksek verimli (token-saver) operasyon rehberidir.

---

## 1. Hızlı Komutlar (Slash Commands)

| Komut | Açıklama |
| :--- | :--- |
| `/music-sync` | Nextcloud ile bağlı olan USB belleği (`CORSA_MUZIK`) ayna modunda senkronize eder. |
| `/music-add <sorgu / link>` | Şarkıyı/albümü 320k MP3 kalitesinde indirir, 500x500 kapak ve sözleri gömer, uygun klasöre atar. |
| `/music-normalize` | Kütüphaneyi EBU R128 (-14 LUFS) standardına göre tarar; arabada kısık veya aşırı patlayanları dengeler. |
| `/music-audit` | Kütüphaneyi tarar; eksik kapak, eksik söz, mükerrer şarkı ve dosya adı hatalarını raporlar. |
| `/music-recommend` | Mevcut kütüphanenin tür/ruh hali ağırlıklarına göre yeni parça ve sanatçı önerileri sunar. |

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

## 4. 13 Tematik Kategori Matrisi

Kütüphane aşağıdaki 13 odaklı klasör yapısına göre kategorize edilir:

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

---

## 5. Güvenlik ve Ayna Senkronizasyon Protokolü

* **50-Parça Taban Kilidi (Floor Guard):** Kaynak dizindeki (`Nextcloud\Music`) parça sayısı 50'nin altına düşerse USB senkronizasyonu acil olarak durdurulur ve USB üzerindeki hiçbir dosya silinmez.
* **Araç Sistem Dosyası Koruması:** USB kökündeki `System Volume Information`, `asisconfig.xml` ve aracın oluşturduğu önbellek dosyaları asla silinmez.
* **Tarih Toleransı:** FAT32 dosya sisteminin 2 saniyelik zaman damgası çözünürlüğü nedeniyle, dosya boyutu eşit ve zaman farkı <= 2 saniye ise kopyalama atlanır.

---

## 6. Komut Satırı & Script Entegrasyonları

```bash
# 1. Kütüphaneyi tara ve raporla (eksik kapak/söz/mükerrer tespiti)
python scripts/audit_library.py

# 2. Akıllı Ses Seviyesi Dengeleme (-14 LUFS cerrahi düzeltme)
python scripts/normalize_audio.py

# 3. Eksik 500x500 kapakları ve sözleri göm
python scripts/embed_metadata.py "C:\Users\MrCoolice\Nextcloud\Music"

# 4. USB belleğe ayna senkronizasyonu yap
python scripts/sync_usb.py
```

---

---

## 7. Akıllı Model Yönlendirme & Sıfır Token Protokolü (Token-Saver)

Bu skill deterministik Python scriptlerine (`audit_library.py`, `normalize_audio.py`, `embed_metadata.py`, `sync_usb.py`) dayandığından, **Gemini Pro ana kotasını asla tüketmez**:
1. **Hafif Alt Ajan Zorunluluğu:** Müzik kütüphanesini tarama, düzenleme veya USB senkronizasyonu komutları verildiğinde ajan, görevi arka planda `Model: flash_lite` veya `Model: flash` olarak çalıştırır.
2. **Kategori Sınıflandırması:** Yeni eklenen parçanın 13 kategoriden hangisine gideceği sorusu, yerel `qwen-coder-14b` (RTX 4070) veya `groq-gpt-oss-120b` üzerinden 0.5 saniyede $0 maliyetle çözülür.
3. **Komut Çıktıları:** Script logları filtrelenerek kullanıcıya yalnızca tamamlanan işlem özeti sunulur (token israfı engellenir).

## 8. Master Kaynak & Kalıcı Silme Kuralı (Single Source of Truth)

1. **Dinamik Ana Merkez & Taşınabilirlik:** Kütüphane varsayılan olarak yerel `Nextcloud/Music` veya işletim sisteminin varsayılan `Music` klasörünü otomatik tanır. Başka kullanıcılar veya farklı sürücüler (örneğin `D:\Muziklerim`) ortam değişkeni (`AUDIOPHILE_MUSIC_DIR`), `config.json` veya menüdeki `[4]` seçeneği ile tek tıkla kendi kaynak dizinlerini belirleyebilirler.
2. **Kalıcı Silme İlkesi (No Zombie Files):** Kullanıcı kaynak klasöründen bir şarkıyı sildiğinde, o şarkı kalıcı olarak silinmiş kabul edilir. Hiçbir otonom işlem, yükseltme scripti veya aracı silinen parçaları asla tekrar indiremez, geri getiremez veya diriltemez.
3. **USB Ayna Silme (True Mirror Sync):** `/music-sync` veya `sync_usb.py` çalıştırıldığında, kaynakta silinmiş olan tüm dosyalar USB bellekten de otomatik olarak kaldırılır (`orphan file cleanup`). Böylece USB bellek her zaman kaynak kütüphane ile %100 birebir aynı kalır.
4. **Onaysız İndirme Yasağı:** Ajan, kullanıcı açıkça isim/bağlantı verip *"ekle"* demedikçe kendi inisiyatifiyle hiçbir yeni parça indiremez.

---

## 9. Hızlı İndeks (.library_index.json) & Silinenler Kara Listesi (Tombstones)

Kullanıcının kütüphanesini her seferinde baştan taramamak, silme işlemlerini anında algılamak ve token tasarrufu sağlamak için iki yerel takip dosyası kullanılır:

1. **`.library_index.json` (Hafif İndeks Önbelleği):**
   - Kütüphane kökünde yer alır. Tüm kategorilerin parça sayılarını, dosya yollarını, boyutlarını ve temiz isimlerini önbellekte tutar.
   - Analiz ve öneri işlemlerinde disk taramasını atlayarak **0.001 saniyede** doğrudan indeksten okunur.
   - `python scripts/index_manager.py` komutu ile milisaniyeler içinde güncellenir.

2. **`silinenler_kara_liste.txt` (Kalıcı Silinenler & Tombstone Defteri):**
   - Kullanıcı müzik klasöründen bir şarkıyı sildiğinde, sistem önceki indeks ile mevcut durumu karşılaştırarak silinen parçayı anında tespit eder ve bu deftere kaydeder.
   - **Asla Tekrar Önermeme Garantisi:** `/music-recommend` veya öneri motorları bu kara listeyi okur; kullanıcının daha önce beğenmeyip sildiği parçaları **asla bir daha önermez ve indirmez**.
   - **Kullanıcı Kalıcı Yasaklı Sanatçılar:** `Demir Demirkan`, `Bulutsuzluk Özlemi`, `Nirvana` kesinlikle ve kalıcı olarak yasaklanmıştır; asla önerilmez ve indirilmez.
   - **USB Ayna Temizliği:** `/music-sync` bu listeyi kullanarak arabadaki USB bellekte kalan öksüz parçaları saniyeler içinde temizler.


---

## 10. Corsa Station (Masaüstü Menü İstasyonu & Otomatik MBR/FAT32 USB Formatı)

Kullanıcının hiçbir parametre veya komut satırı ezberlemesine gerek kalmadan tek tıkla kullanabileceği interaktif Windows istasyonudur:

1. **Masaüstü Başlatıcı:** `C:\Users\MrCoolice\Desktop\Corsa_Muzik_Merkezi.bat` (veya kütüphane kökündeki `Corsa_Muzik_Merkezi.bat`)
2. **Menü Seçenekleri:**
   - `[1] Hızlı Eşitleme`: Mevcut `CORSA_MUZIK` belleğine sadece yeni ve güncellenen parçaları kopyalar; kaynakta silinenleri USB'den kaldırır.
   - `[2] Sıfırdan USB Hazırla & Formatla`: Yeni veya bozuk USB bellekleri güvenle tespit eder; Opel IntelliLink uyumlu **MBR** ve **FAT32** formatı atar, etiketini `CORSA_MUZIK` yapar ve kütüphaneyi doldurur.
   - `[3] Kütüphane Sağlığı & USB Boyut Karşılaştırması`: Kaynak boyutu ile takılı USB'nin boş alanını kıyaslar; Opel IntelliLink R4.0 için **Min 16 GB / İdeal 32 GB** kapasite rehberini sunar.
   - `[4] Kütüphane Klasörünü Ayarla / Değiştir`: Kullanıcının kendi bilgisayarındaki müzik klasörünü (`D:\Muziklerim` vb.) seçmesini ve kalıcı olarak kaydetmesini sağlar.
   - `[5] Çıkış`: Programı kapatır.
3. **Klavye Dinleyicisi:** `msvcrt.getch()` ile herhangi bir tuşa basıldığı anda beklemeden ana menüye döner.

---

## 11. Taşınabilirlik & Çoklu Kullanıcı Yapılandırması (Multi-User Portability)

GitHub deposundan projeyi indiren farklı kullanıcılar için kütüphane yolu 4 kademeli dinamik çözümleme (`library_config.py`) ile belirlenir:

1. **Kademe 1 (Ortam Değişkeni):** `AUDIOPHILE_MUSIC_DIR` veya `CORSA_MUSIC_DIR` tanımlıysa doğrudan o yol kullanılır.
2. **Kademe 2 (`config.json`):** Kullanıcı menüden `[4]` seçeneği ile klasör belirlediğinde yol yerel `config.json` içine yazılır ve hatırlanır.
3. **Kademe 3 (Otomatik Algılama):**
   - `~/Nextcloud/Music` (Nextcloud kullanıcıları için)
   - `~/Music/Corsa-Library`
   - `~/Music` (Standart Windows/macOS/Linux kullanıcı müzik dizini)
4. **Kademe 4 (Varsayılan):** Kullanıcının işletim sistemi müzik klasörü (`~/Music`). Hiçbir hardcoded kullanıcı adı veya dosya yolu kısıtlaması bulunmaz.
