---
name: audiophile-music-curator
description: >
  Autonomous music library curation, 500x500 ID3v2.3 cover embedding, LRCLIB synced lyrics, 13-genre routing, and automotive FAT32/MBR USB mirror sync for Opel IntelliLink and Nextcloud.
---

# Audiophile Music Curator & Automotive Library Ops

Bu skill; yerel ve bulut tabanlı müzik kütüphanelerinin (`Nextcloud\Music`), araç içi bilgi-eğlence sistemlerinin (özellikle **Opel IntelliLink R4.0**) ve odyofil koleksiyonlarının kusursuz şekilde yönetilmesi, indirilmesi, etiketlenmesi ve senkronize edilmesi için tasarlanmış yüksek verimli (token-saver) operasyon rehberidir.

---

## 1. Hızlı Komutlar (Slash Commands)

| Komut | Açıklama |
| :--- | :--- |
| `/music-sync` | Nextcloud ile bağlı olan USB belleği (`CORSA_MUZIK`) ayna modunda senkronize eder. |
| `/music-add <sorgu / link>` | Şarkıyı/albümü indirir, 500x500 kapak ve sözleri gömer, 13 klasörden en uygununa yerleştirir. |
| `/music-audit` | Kütüphaneyi tarar; eksik kapak, eksik söz, mükerrer şarkı ve dosya adı hatalarını raporlar. |
| `/music-recommend` | Mevcut kütüphanenin tür/ruh hali ağırlıklarına göre yeni parça ve sanatçı önerileri sunar. |

---

## 2. Otomobil & Donanım Standartları (Opel IntelliLink Kriterleri)

IntelliLink R4.0 ve benzeri araç multimedya üniteleri katı donanım kurallarına sahiptir. Bu kuralların dışına çıkıldığında ünite *"Desteklenmeyen USB Aygıtı"* hatası verir:

1. **MBR Bölüntü Tablosu:** Disk kesinlikle **GPT olamaz**. Mutlaka **MBR (Master Boot Record)** olarak ilklendirilmelidir (`diskpart -> clean -> convert mbr`).
2. **FAT32 Dosya Sistemi:** USB bellek <= 32 GB olmalı ve `FAT32` formatında biçimlendirilmelidir. Varsayılan hacim etiketi: `CORSA_MUZIK`.
3. **Kapak Görseli Kuralı:** Maksimum **500x500 piksel**, kare, JPEG formatında ve **ID3v2.3 `APIC`** tag'i olarak gömülmelidir (ID3v2.4 veya aşırı büyük/progressive JPEG'ler ekranda siyah kalır).
4. **Şarkı Sözü:** `USLT` (Unsynchronized Lyrics) veya LRCLIB senkronize tag formatında eklenir.
5. **Karakter Güvenliği:** Dosya ve klasör adlarında Türkçe karakterler korunabilir; ancak `:`, `*`, `?`, `"`, `<`, `>`, `|` gibi geçersiz karakterler ve çift boşluklar mutlaka temizlenmelidir.
6. **Yol Uzunluğu:** Dosya yolu uzunluğu araç hafızasını korumak için 128 karakteri geçmemelidir.

---

## 3. 13 Tematik Kategori Matrisi

Kütüphane aşağıdaki 13 odaklı klasör yapısına göre kategorize edilir:

| No | Klasör Adı | Tanım & Temsili Sanatçılar |
| :---: | :--- | :--- |
| `01` | `01_POWER_ENERGY` | Hızlı, tempolu parçalar (HammerFall, Five Finger Death Punch, Arch Enemy). |
| `02` | `02_DARK_MELANCHOLY` | Melankoli & Hüzün (Katatonia, Anathema, Mad Season, Alice in Chains, Portishead). |
| `03` | `03_EPIC_FANTASY` | Senfonik & Epik Metal (Blind Guardian, Nightwish, Avantasia, Savatage, Demons & Wizards). |
| `04` | `04_SOFT_CHILL` | Akustik & Gece Sürüşü (Dire Straits, Pink Floyd, Gary Moore, Camel, Chris Rea, Frank Sinatra). |
| `05` | `05_TURKCE_ROCK_RAP` | Türkçe Rock / Rap Klasikleri (Pentagram, Şebnem Ferah, Cem Karaca, Sagopa Kajmer, Hayko Cepkin). |
| `06` | `06_DOOM_GOTHIC_METAL` | Doom, Death & Gothic (My Dying Bride, Draconian, Paradise Lost, Tiamat, Amorphis). |
| `07` | `07_ROCK_HEAVY_METAL` | Heavy Metal & 90s Rock (Iron Maiden, Black Sabbath, Judas Priest, Therapy?, Saxon, Bruce Dickinson). |
| `08` | `08_SYNTH_ELECTRO_POP` | Retro Pop & Dans (Army of Lovers, Nero, Madcon, Empire of the Sun). |
| `09` | `09_FILM_OYUN_SOUNDTRACK`| Film & Oyun Müzikleri (Metal Gear Solid, 28 Days Later, The Hobbit, Escape from L.A.). |
| `10` | `10_KARISIK` | Marşlar ve Özel Tarihi Kayıtlar. |
| `11` | `11_SYNTHWAVE_OUTRUN` | Retrowave & Outrun (Kavinsky, The Midnight, FM-84, GUNSHIP, Dance With the Dead). |
| `12` | `12_CYBERPUNK_DARK_TECHNO`| Cyberpunk & Midtempo (Gesaffelstein, Rezz, Carpenter Brut, Perturbator, Daniel Deluxe). |
| `13` | `13_ANADOLU_PSYCHEDELIC` | Anadolu Pop/Rock & Psychedelic (Derindekiler, Berrin Keskin, Altın Gün, Derya Yıldırım, Erkin Koray). |

---

## 4. Güvenlik ve Ayna Senkronizasyon Protokolü

* **50-Parça Taban Kilidi (Floor Guard):** Kaynak dizindeki (`Nextcloud\Music`) parça sayısı 50'nin altına düşerse USB senkronizasyonu acil olarak durdurulur ve USB üzerindeki hiçbir dosya silinmez (boş klasör veya senkronizasyon kopması koruması).
* **Araç Sistem Dosyası Koruması:** USB kökündeki `System Volume Information`, `asisconfig.xml` ve aracın oluşturduğu önbellek dosyaları asla silinmez.
* **Tarih Toleransı:** FAT32 dosya sisteminin 2 saniyelik zaman damgası çözünürlüğü nedeniyle, dosya boyutu eşit ve zaman farkı <= 2 saniye ise kopyalama atlanır (gereksiz flaş bellek yazımını ve aşınmasını önler).

---

## 5. Komut Satırı & Script Entegrasyonları

Skill içerisindeki yardımcı Python modülleri:

```bash
# 1. Kütüphaneyi tara ve raporla (eksik kapak/söz tespiti)
python scripts/audit_library.py

# 2. Eksik 500x500 kapakları (iTunes/Deezer/YT) ve sözleri (LRCLIB) göm
python scripts/embed_metadata.py "C:\Users\MrCoolice\Nextcloud\Music"

# 3. USB belleğe ayna senkronizasyonu yap
python scripts/sync_usb.py
```

Masaüstünde tek tıkla çalıştırmak için `CORSA USB Esitle.lnk` -> `C:\Users\MrCoolice\Music\USB_Esitle.bat` kısayolu yapılandırılmıştır.
