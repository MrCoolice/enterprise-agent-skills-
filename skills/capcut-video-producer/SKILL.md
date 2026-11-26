---
name: capcut-video-producer
description: Autonomous local CapCut Desktop draft producer for vertical 9:16 Reels/TikTok/Shorts, targeting 100% FREE templates, effects, transitions, and generating instant 1-click export alerts.
---

# CapCut Video Producer (GölgeSiber & Dalaman Yerel Video Üretim Motoru)

Bu beceri, **CapCut Desktop (Windows & Windows Store sürümleri)** uygulamasını harici bir render ve kurgu motoru olarak kullanarak; çizgi roman panellerini, görsel sahneleri ve sesleri sıfır maliyetle, doğrudan yerel GPU donanım hızlandırmasıyla yüksek kaliteli dikey (9:16) Reels/TikTok/Shorts videolarına dönüştürür.

---

## 🎯 1. Altın Kurallar ve Kalite Standartları

1. **%100 ÜCRETSİZ (FREE) KATMAN İLKESİ:**
   - Asla CapCut Pro, ücretli şablon veya filigranlı geçiş kullanılmaz.
   - Kullanıcı dışa aktarırken asla ödeme duvarına veya filigran uyarısına takılmaz.

2. **PANEL DÜZENİ VE AKILLI KIRPMA STANDARDI:**
   - Çizgi roman ve karikatür görselleri körlemesine 4'e bölünmez!
   - Çizgi romanın kaç panelden oluştuğu (2 panel mi, 3 panel mi, 4 panel mi) görsel üretim isteminden ve gutter (panel boşluğu) çizgilerinden tespit edilir.
   - 2 panelli dikey çizgi romanlarda görüntü tam ortadan (`h / 2`) bölünerek **2 Sahne** (Üst Panel: Problem/Çile, Alt Panel: Çözüm/Rahatlama) olarak kurgulanır. Yanlış bölme işlemi karakterlerin kafa ve bacaklarının kesilmesine yol açar.

3. **ÇİFT ALTYAZI (TEXT CLASH) YASAĞI:**
   - Görselin içinde halihazırda konuşma balonları, tabelalar veya Türkçe diyaloglar varsa, alttan ikinci bir harici altyazı katmanı **eklenmez**.
   - Görseldeki esprilerin ve metinlerin üstü asla harici metin kutularıyla örtülmez.
   - Harici altyazı yalnızca tamamen metinsiz/sessiz görseller kullanıldığında eklenir.

4. **9:16 DİKEY ÇERÇEVELEME & AKILLI DOLGU:**
   - Kare veya 1:1 / 4:3 oranındaki paneller 9:16 dikey tuvale yerleştirilirken çiğ siyah boşluk bırakılmaz.
   - Sahnenin kendi renk tonuna uygun (örneğin gece sahnelerinde gece mavisi degrade, sıcak iç mekanlarda altın sarısı/ahşap degrade veya görselin bulanıklaştırılmış arka planı) dolgu uygulanır.

5. **YEREL MAĞAZA (STORE) VE CİHAZ PARMAK İZİ UYUMU:**
   - CapCut 9.3+ Windows Store sürümü için `draft_content.json` ve `draft_meta_info.json` dosyalarında cihaz parmak izi (`device_id`, `mac_address`, `app_id: 359289`, `engine: 191.0.0`) tam eşleşmelidir.
   - Yardımcı dosyalar (`timeline_layout.json`, `draft_biz_config.json`, `attachment_pc_common.json`) eksiksiz klasörde bulunmalıdır.

6. **FFMPEG VE YEREL GPU KULLANIMI:**
   - CapCut'ın kendi iç motorundaki FFmpeg (`%LOCALAPPDATA%\CapCut\Apps\*\ffmpeg.exe`) veya CapCut masaüstü GPU hızlandırıcısı kullanılır.
   - Kullanıcıya her üretim sonrası 1 tıkla dışa aktarım yönergesi sunulur.

---

## 🎬 2. Standart 2 Panelli Karikatür Reels Akış Şablonu

| Sahne | Kaynak Panel | Süre | Kamera / Efekt | Ses / Ritim |
| :--- | :--- | :--- | :--- | :--- |
| **Sahne 1 (Problem)** | Üst Panel (Havalimanı Çilesi) | 0.0 - 4.5 sn | Yavaşça karaktere doğru yaklaşma (Zoom In) | Hafif gergin / komik fon |
| **Geçiş (Transition)**| Ara Kesit | 4.5 sn | Parlama (Flash / White Dissolve) | Geçiş efekti sesi |
| **Sahne 2 (Çözüm)** | Alt Panel (Otel Huzuru) | 4.5 - 9.0 sn | Genişten odaya doğru ferah açılma | Rahatlatıcı / neşeli tatil melodisi |

---

## 🚨 3. Standart Dışa Aktarım Uyarı Formatı

```markdown
> [!IMPORTANT]
> ### 🎬 CapCut Projeniz Hazır! Dışa Aktarmak İçin 2 Adım:
> 1. Masaüstünüzdeki **CapCut** uygulamasını açın.
> 2. Projeler listesinde ilk sırada yer alan **`[Proje_Adı]`** projesine tıklayın.
> 3. Sağ üst köşedeki mavi **"Dışa Aktar" (Export)** butonuna basarak videonuzu kaydedin!
```
