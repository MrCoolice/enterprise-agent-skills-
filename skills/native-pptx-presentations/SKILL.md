---
name: native-pptx-presentations
description: >-
  Native editable PowerPoint (.pptx) slide deck studio (python-pptx / PptxGenJS) converting
  Markdown, PDF, DOCX, or URLs into real PowerPoint shapes, OOXML charts/tables, corporate
  templates, and speaker notes. Use when creating editable .pptx workshops, training slides
  (08-Egitim_Kaynaklari), or partner decks. Do NOT use for PDF/EPUB books (use
  technical-book-publishing), SVG/PNG diagrams (use editorial-architecture-diagrams), or videos
  (use video-director-engine).
---

# 📊 Native PowerPoint (.pptx) Sunum & Eğitim Destesi Stüdyosu (`ppt-master`)

Bu beceri; **`hugohe3/ppt-master`** mimarisini GölgeSiber Veri Merkezi, `08-Egitim_Kaynaklari/`, **OPNsense 2026 Kitap** seminerleri ve **Dalaman Airport Suites** iş ortağı sunumlarına uyarlayarak, ham belgelerden (Markdown, PDF, DOCX, URL veya konu özeti) **%100 yerel ve sonradan düzenlenebilir `.pptx` sunumları** üretir.

> **Kapsam Sınırı:** Bu beceri **yerel düzenlenebilir `.pptx` slayt desteleri** içindir. Matbaa/PDF/EPUB kitap dizgisi için `technical-book-publishing`, bağımsız yüksek çözünürlüklü `.svg`/`.png`/HTML teknik mimari diyagramlar için `editorial-architecture-diagrams`, kod tabanlı video/Reels prodüksiyonu için `video-director-engine` kullanılır.

---

## 🎯 1. Temel İlke: Ekran Görüntüsü Değil, Gerçek Düzenlenebilir `.pptx` Nesneleri

1. **Sıfır Düzleştirme (No Flattened Slide Images):** Slaytları tek parça PNG olarak çizip PowerPoint'e yapıştırmak **yasaktır**. Başlıklar, metin kutuları, kartlar, oklar, tablolar ve veri grafikleri (**native OOXML Bar/Line/Pie Charts**) PowerPoint, LibreOffice Impress veya `CT 100 (OnlyOffice)` içinde sonradan tek tıkla düzenlenebilir yerel nesneler olarak üretilir.
2. **Üretim Motoru Seçimi:**
   - **Python ekosistemi (varsayılan):** `python-pptx` (+ grafik verisi için native `CategoryChartData` / `XyChartData`, karmaşık diyagram gömümü için 300 DPI `.png`).
   - **Node.js / TypeScript ekosistemi:** `PptxGenJS` (web/Next.js içi dinamik `.pptx` indirme gereken senaryolarda).
3. **Mevcut Kurumsal Şablon Koruma:** Kullanıcının elinde hazır bir `.pptx` şablonu (Slide Master / Layout) varsa sıfırdan stil uydurmak yerine doğrudan o şablonun layout ve tema renkleri üzerine yaz.

---

## 🎨 2. Anti-Slop 16:9 Widescreen Slayt Tasarım Hijyeni

1. **Tuval & Güvenli Marj:** Standart `16:9` (`13.333" × 7.5"`). Dört kenardan en az `0.6"` güvenli boşluk bırak; hiçbir nesne kenara yapışmaz veya taşmaz.
2. **1 Slayt = 1 Ana İddia (Zero Wall-of-Text):**
   - Slayt üzerinde paragraf yığını kesinlikle yasaktır.
   - En fazla **3–5 kısa madde** (madde başı ≤10–12 kelime) veya **1 büyük KPI/grafik + 1 vurgu cümlesi** kullan.
   - Uzun açıklamalar, komut detayları ve anlatım metni daima slaytın **Konuşmacı Notları (Speaker Notes)** alanına yazılır.
3. **Tipografi & Boşluk Zemini:**
   - **Ana Başlık:** `28–36 pt` (kalın, kısa aksiyon başlığı — *"OPNsense VLAN'ları"* yerine *"VLAN Segmentasyonu Yatay Hareketi %90 Keser"*).
   - **Gövde / Kart Metni:** En az `16–18 pt`; dipnot/kaynak en az `11–12 pt`.
   - **Nefes Payı:** Slayt alanının en az **`%30`–`%35`'i** boş bırakılır; her slaytı birbirinin aynısı madde listesi yapma (2 sütun karşılaştırma, KPI ızgarası, zaman çizelgesi, mimari görsel + 3 çıkarım düzenlerini değiştir).
4. **Sıfır Bozuk Emoji (`[]`) & Net Kontrast:** Sunum metinlerinde hedef sistemde kare `[]` çıkabilecek ham unicode emojiler yerine temiz vektör ikonlar (SVG → yüksek DPI PNG) veya yerel PowerPoint şekilleri kullan; WCAG AA kontrastını koru.

---

## 🏛️ 3. GölgeSiber Hazır Sunum Profilleri

| Profil | Kullanım Alanı | Zemin & Renk Paleti | Tipografi & Görsel Dil |
| :--- | :--- | :--- | :--- |
| **A. Siber / Teknik Eğitim (Koyu)** | `08-Egitim_Kaynaklari/`, konferans, teknik demo | `#020617` (`Slate-950`) zemin, `#0F172A` kartlar, `#38BDF8` Cyan / `#10B981` Zümrüt vurgu | Temiz sans-serif + kod bloklarında monospace; koyu tema diyagramlar |
| **B. OPNsense 2026 & Workshop (Aydınlık)** | Kitap lansmanı, projektör/salon eğitimi, PDF dağıtım | `#F8FAFC` / `#FFFFFF` zemin, `#0F172A` metin, `#D94F2A` OPNsense turuncusu vurgu | Yüksek projektör okunabilirliği; `editorial-architecture-diagrams` Mod A diyagramları |
| **C. Dalaman Suites / İş & Yatırımcı** | İş ortağı, otel/acente, gelir & strateji sunumları | `#FAF8F5` sıcak traverten zemin, `#1B2A4A` lacivert + `#B89352` sıcak altın vurgu | Editoryal başlıklar, `str-revenue-listing-master` KPI tabloları ve temiz gelir grafikleri |

---

## 🔄 4. 4 Aşamalı Üretim Akışı & Opsiyonel Sesli Anlatım

1. **Aşama 1 — Kaynak Çözümleme & İskelet Onayı (Outline Gate):**
   - Verilen Markdown/PDF/URL/konuyu inceleyip slayt listesini (**Slayt No • Aksiyon Başlığı • Düzen Tipi • Görsel/Grafik • Tek Cümlelik Mesaj**) tablo halinde sun.
   - Uzun destelerde (`>8` slayt) koda geçmeden önce kullanıcıdan iskelet onayı al.
2. **Aşama 2 — Programatik `.pptx` Üretimi:**
   - Tekrar çalıştırılabilir, temiz bir Python (`python-pptx`) veya Node (`PptxGenJS`) betiğiyle `.pptx` dosyasını oluştur.
   - Her slayta sunucunun okuyabileceği doğal Türkçe **Konuşmacı Notları (`slide.notes_slide`)** ve tutarlı slayt numarası/alt bilgi ekle.
3. **Aşama 3 — Görsel Taşma & Hizalama QA Kapısı:**
   - Teslim öncesi mümkünse LibreOffice (`soffice --headless --convert-to pdf`) + sayfa görüntüsü ile slaytları görsel olarak kontrol et:
     - [ ] Metin kutusu taşması veya şekil üst üste binmesi sıfır mı?
     - [ ] Tüm grafik/tablolar PowerPoint'te düzenlenebilir yerel nesneler mi?
     - [ ] Bozuk emoji kutusu `[]` yok mu ve font boyutları en az `16pt` mi?
     - [ ] Slaytlar arası düzen çeşitliliği (monoton madde yığını yok) sağlandı mı?
4. **Aşama 4 — Opsiyonel Sesli Sunum / Video Köprüsü:**
   - Kullanıcı *"Sesli sunuma/videoya çevir"* derse, her slaydın **Konuşmacı Notlarını** zaman damgalı seslendirme (Edge-TTS veya ElevenLabs `eleven_v4`) ve `-14 LUFS` miksaj için `video-director-engine` hattına aktar.
