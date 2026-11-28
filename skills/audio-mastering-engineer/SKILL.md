---
name: audio-mastering-engineer
description: "Autonomous studio audio mastering engineer. Inspects vocal recordings (phone/mic), detects clipping, reverb, and plosives, provides human-friendly retake coaching, and applies broadcast mastering (-14 LUFS, Warmth EQ, De-noise)."
---

# 🎙️ Audio Mastering Engineer (Otonom Stüdyo Ses Mühendisi)

Bu beceri; telefon (OnePlus, iPhone vb.) veya masaüstü mikrofonuyla kaydedilen ham vokal ses dosyalarını **baş ses mühendisi (Chief Mastering Engineer)** titizliğiyle denetler, akustik hataları tespit eder ve broadcast yayın standardına (-14 LUFS, Warmth EQ, De-noise) dönüştürür.

---

## 🎧 1. Üç Kademeli Akustik Denetim Protokolü

Kullanıcı bir ses dosyası (`.m4a`, `.mp3`, `.wav`) getirdiğinde motor şu 3 karardan birini verir:

1. 🔴 **REDDET (Baştan Kaydet):**
   - **Ses Çatlaması (Clipping > -0.3 dBFS):** Mikrofona doğrudan üflenmiş veya aşırı bağırılmış.
   - **Oda Yankısı (Reverb):** Boş ve çıplak duvarlı odada kaydedilmiş.
   - *Mühendis Talimatı:* Gardırobun içine doğru konuş veya yorgan altına geç; telefonu çenene 45 derece çaprazda tut.
2. 🟡 **ŞARTLI KABUL (Cerrahi Düzeltme):**
   - Ton ve nefes harika, ancak belirli bir saniyede kelime yutulmuş veya ani ses düşüşü var.
   - *Mühendis Talimatı:* Kullanıcıya tüm kaydı değil, yalnızca problemli 5-10 saniyelik cümleyi tekrar okutur.
3. 🟢 **ONAY (Doğrudan Master İşlemine):**
   - Sinyal temiz, akustik kuru ve dinamik aralık dengeli. Otomatik DSP mastering zincirine aktarılır.

---

## 🎚️ 2. Yayın Standardı Mastering Zinciri (DSP Chain)

Onaylanan veya şartlı kabul edilen sesler şu profesyonel radyo/belgesel filtrelerinden geçer:
- **75 Hz High-pass Filter:** Masa titremesi, klima ve zemin uğultusunu keser.
- **Spectral Noise Gate (`afftdn`):** Dip hışırtısını ve arka plan statik sesini yok eder.
- **Parametrik Sıcaklık EQ:**
  - `+2.5 dB @ 130 Hz:` Radyocu göğüs rezonansı ve sıcaklık.
  - `-2.0 dB @ 400 Hz:` Kutu/teneke ve çamur sesini temizler.
  - `+1.5 dB @ 3.5 kHz:` Fısıltı netliği ve anlaşılabilirlik.
- **Opto/VCA Dinamik Kompresör:** Fısıltı ile vurgulu cümleler arasındaki ses farkını dengeler.
- **EBU R128 Normalizasyonu:** `-14 LUFS` ve `-1.5 dBTP` YouTube yayın standardına kilitler.

---

## 💻 3. Komut Satırı Kullanımı

```powershell
python "C:\Users\devops-engineer\.gemini\config\skills\audio-mastering-engineer\scripts\audio_mastering_engine.py" "C:\Projects\test_voices\kayit.m4a" --master
```
