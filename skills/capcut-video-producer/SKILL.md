---
name: capcut-video-producer
description: Autonomous local CapCut Desktop draft producer for vertical 9:16 Reels/TikTok/Shorts, targeting 100% FREE templates, effects, transitions, and generating instant 1-click export alerts.
---

# CapCut Video Producer (GölgeSiber & Dalaman Yerel Video Üretim Motoru)

Bu beceri, **CapCut Desktop (Windows & Windows Store 9.3+ sürümleri)** uygulamasını harici bir render ve kurgu motoru olarak kullanarak; çizgi roman panellerini, görsel sahneleri, altyazıları, ses efektlerini ve geçişleri sıfır maliyetle, doğrudan yerel GPU donanım hızlandırmasıyla yüksek kaliteli dikey (9:16) Reels/TikTok/Shorts videolarına dönüştürür.

---

## 🎯 1. Altın Kurallar ve Kalite Standartları

1. **%100 ÜCRETSİZ (FREE) KATMAN İLKESİ:**
   - Asla CapCut Pro, ücretli şablon veya filigranlı geçiş kullanılmaz.
   - Kullanıcı dışa aktarırken asla ödeme duvarına veya filigran uyarısına takılmaz.

2. **15 SANİYELİK 5-BEAT DİNAMİK RİTİM STANDARDI (Anti-Slayt):**
   - 15 saniyelik videolarda asla 1-2 durağan resim kullanılmaz. İdeal ritim **5 sahnedir (her biri ~2.5-3 sn)**.
   - Kadrajlar monoton olamaz: Aşırı Yakın Çekim (Macro Close-up), Orta Çekim (Medium) ve Geniş Açı (Wide) ardışık sıralanır.
   - Kamera hareketleri: Panikte Crash Zoom/Shake, Çözümde Slow Pull-out uygulanır.

3. **SFX (SES EFEKTLERİ) KATMANI:**
   - Fon müziği tek başına yetersizdir; çizgi filmi canlandıran SFX katmanıdır (Bavul gıcırtısı, yutkunma, saat tıkırtısı, ding aydınlanma sesi, yatağa zıplama sesi).

4. **ÇİFT ALTYAZI (TEXT CLASH) YASAĞI:**
   - Çizimde konuşma balonu veya tabela varsa harici altyazı basılmaz.
   - Görseldeki esprilerin ve metinlerin üstü asla harici metin kutularıyla örtülmez.

5. **YEREL MAĞAZA (STORE) VE CİHAZ PARMAK İZİ UYUMU:**
   - CapCut 9.3+ Windows Store sürümü için `draft_content.json` ve `draft_meta_info.json` dosyalarında cihaz parmak izi (`device_id`, `mac_address`, `app_id: 359289`, `engine: 191.0.0`) tam eşleşmelidir.
   - Yardımcı dosyalar (`timeline_layout.json`, `draft_biz_config.json`, `attachment_pc_common.json`) eksiksiz klasörde bulunmalıdır.

6. **FFMPEG VE YEREL GPU KULLANIMI:**
   - CapCut'ın kendi iç motorundaki FFmpeg (`%LOCALAPPDATA%\CapCut\Apps\*\ffmpeg.exe`) veya CapCut masaüstü GPU hızlandırıcısı kullanılır.

---

## 🎬 2. 15 Saniyelik 5-Beat Karikatür Reels Kurgu Mimarisi

```
Zaman Çizelgesi (15 Saniye = 15,000,000 µs):

[ Kanal 1 - Video Sahneleri ]
|-- Sahne 1 (0-3s) --|-- Sahne 2 (3-6s) --|-- Sahne 3 (6-9s) --|-- Sahne 4 (9-12s) --|-- Sahne 5 (12-15s) --|
       (Macro Close-up)       (Medium Shot)          (Twist/Tabela)         (Wide Shot)            (Hero CTA)
[ Geçişler ]
                     [Parlama Flash]       [Parlama Flash]      [Parlama Flash]       [Parlama Flash]
[ Kanal 2 - SFX (Ses Efektleri) ]
|-- Rüzgar/Gasp --|   |-- Tıkırtı --|      |-- Ding/Chime --|   |-- Poof/Bounce --|   |-- Şık Kapanış --|
[ Kanal 3 - Fon Müziği (%40 Ses) ]
|================================= Ritmik Akustik / Lo-Fi Tatil Melodisi ================================|
```

---

## 🚨 3. Standart Dışa Aktarım Uyarı Formatı

```markdown
> [!IMPORTANT]
> ### 🎬 CapCut Projeniz Hazır! Dışa Aktarmak İçin 2 Adım:
> 1. Masaüstünüzdeki **CapCut** uygulamasını açın.
> 2. Projeler listesinde ilk sırada yer alan **`[Proje_Adı]`** projesine tıklayın.
> 3. Sağ üst köşedeki mavi **"Dışa Aktar" (Export)** butonuna basarak videonuzu kaydedin!
```
