---
name: capcut-video-producer
description: Autonomous local CapCut Desktop draft producer for vertical 9:16 Reels/TikTok/Shorts, targeting 100% FREE templates, effects, transitions, and generating instant 1-click export alerts.
---

# CapCut Video Producer (GölgeSiber & Dalaman Yerel Video Üretim Motoru)

Bu beceri, **CapCut Desktop (Windows)** uygulamasını harici bir render ve kurgu motoru olarak kullanarak; çizgi roman panellerini, görsel sahneleri, altyazıları ve geçişleri sıfır maliyetle, doğrudan yerel GPU donanım hızlandırmasıyla yüksek kaliteli dikey (9:16) Reels/TikTok/Shorts videolarına dönüştürür.

---

## 🎯 1. Temel Prensipler ve Altın Kurallar

1. **%100 ÜCRETSİZ (FREE) KATMAN HEDEFİ:**
   - Asla ücretli veya Pro filigranlı (CapCut Pro) geçiş, şablon, ses veya efekt eklenmez.
   - Sadece ücretsiz standart efektler (Ken Burns / Zoom Pan, Fade In/Out, temel metin kutuları, telifsiz sesler) kullanılır.
   - Kullanıcı dışa aktarırken asla "Pro'ya Geçin" ödeme duvarına takılmaz.

2. **YEREL ÇALIŞMA DİZİNİ:**
   - CapCut masaüstü projeleri doğrudan şu dizinde oluşturulur:
     `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\<Proje_Adi>_<ZamanDamgasi>\`
   - Gerekli 2 ana dosya:
     - `draft_content.json` (Zaman çizelgesi, tuval boyutu 1080x1920, katmanlar, süreler)
     - `draft_meta_info.json` (Proje başlığı, kimlik bilgileri, son değiştirilme tarihi)

3. **FFMPEG BAĞIMSIZLIĞI:**
   - Kullanıcının terminalinde FFmpeg kurulu olmasa dahi CapCut masaüstü projesi anında hazır hale getirilir.
   - Render ve GPU kodlamasını (Nvidia NVENC / Intel QSV / AMD VCE) bizzat CapCut masaüstü uygulaması kullanıcı adına yapar.

4. **KULLANICIYA ZORUNLU DIŞA AKTARIM UYARISI (1-CLICK EXPORT ALERT):**
   - Taslak oluşturulduktan sonra kullanıcıya net bir görsel uyarı kutusu verilir.
   - Kullanıcı CapCut'ı açar, ana sayfada beliren hazır projeye tıklar ve sağ üstteki **"Dışa Aktar" (Export)** butonuna basarak MP4'ü alır.

---

## 📐 2. CapCut Taslak Proje Mimarisi

Bir proje dizini şu yapıda oluşturulmalıdır:

```
com.lveditor.draft/
└── Proje_Adi/
    ├── draft_content.json    # Canvas (1080x1920, 9:16, 30fps), materials (images, texts), tracks (video, audio)
    └── draft_meta_info.json   # Proje adı, draft_id, create_time
```

### Zaman Birimi (Microseconds):
- CapCut zaman çizelgesinde süreler **mikrosaniye** cinsindendir:
  - 1 saniye = `1,000,000` mikrosaniye
  - 8 saniye = `8,000,000` mikrosaniye

---

## 🎬 3. Standart Ücretsiz Efekt & Şablon Seti

| Kategori | Serbest/Ücretsiz Efekt | Kullanım Amacı |
| :--- | :--- | :--- |
| **Kamera Hareketi** | Ken Burns (Yavaşça Yakınlaş / Zoom In) | Hareketsiz çizgi roman panelini canlı videoya dönüştürme |
| **Geçişler** | Fade In (Karararak Giriş), Dissolve | Sahneler arası yumuşak akış |
| **Metin** | Bold Sans, Sarı/Beyaz Vurgulu Altyazı | Reels için dikkat çekici Türkçe başlıklar |
| **Çözünürlük** | 1080x1920 (9:16 Dikey) | Instagram Reels, TikTok, YouTube Shorts |

---

## 🚨 4. Dışa Aktarım Uyarı Formatı (Zorunlu Çıktı Şablonu)

Taslak oluşturulduğunda kullanıcıya mutlaka aşağıdaki biçimde bildirim sunulmalıdır:

```markdown
> [!IMPORTANT]
> ### 🎬 CapCut Projeniz Hazır! Dışa Aktarmak İçin 2 Adım:
> 1. Masaüstünüzdeki **CapCut** uygulamasını açın.
> 2. Ana sayfada ilk sırada yer alan **`[Proje_Adı]`** projesine tıklayın ve sağ üstteki mavi **"Dışa Aktar" (Export)** butonuna basın.
> *Tüm şablonlar ve efektler %100 ÜCRETSİZ olarak ayarlanmıştır, herhangi bir ödeme duvarı çıkmaz.*
```
