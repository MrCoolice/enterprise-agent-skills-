---
name: str-revenue-listing-master
description: >-
  Short-Term Rental (STR) revenue management, competitor nightly-rate benchmarking, OTA
  commission parity (Airbnb, Booking.com, direct), listing optimization, and multilingual guest
  copy for hotel-suites.example.com. Use when pricing nights, optimizing OTA listings, or
  drafting guest templates. Do NOT use for WhatsApp bot FastAPI/Baileys/Meta Cloud API
  engineering (use whatsapp-bot-gateway-ops) or Matomo traffic queries (use
  matomo-analytics-ops).
---

# 🏨 Dalaman Airport Suites — STR Gelir, Fiyatlandırma ve İlan Optimizasyonu Becerisi

Bu beceri; **msg2ai/vacationrental-team-skills** çoklu rol mimarisi ile **OpenBnB / AirROI** rakip fiyatlandırma metodolojisini **`hotel-suites.example.com`**, **Airbnb** ve **Booking.com** kanallarına özel olarak birleştirir.

---

## 📊 1. Rakip Analizi & Dinamik Fiyatlandırma Motoru (Comps Analysis)

Fiyat belirleme veya dönem değerlendirmesi istendiğinde şu adımları uygula:

1. **Canlı Veri Çekme (Eğer `openbnb` MCP aktifse):**
   - `airbnb_search` aracıyla **Dalaman / Ortaca / Muğla** bölgesinde aynı oda sayısı (`1+1`, `2+1` vb.), aynı misafir kapasitesi ve hedef tarihler için en az **10–15 rakip ilanı** çek.
   - Rakiplerin **gecelik fiyatını**, **temizlik ücretini**, **minimum konaklama süresini**, **puanını (rating)** ve **yorum sayısını** tablolaştır.
   - **Medyan (Ortanca) Fiyat**, **Alt %25** ve **Üst %25 (Premium)** bantlarını hesapla.

2. **Kanal Bazlı Net Gelir Eşitliği (OTA Commission Parity):**
   Misafirin ödediği toplam fiyat ile senin eline geçen net tutarı eşitlemek için şu formülü kullan:
   - **Doğrudan Web Sitesi (`hotel-suites.example.com`):** Baz Net Fiyat ($P_{net}$) — %0 OTA komisyonu. *(Misafire %8–10 doğrudan rezervasyon indirimi vererek hem misafire kazandır hem de komisyonsuz daha yüksek net gelir elde et!)*
   - **Airbnb:** Komisyon yapısına göre (Split Fee ~%3 ev sahibi veya Host-Only ~%15) net geliri koruyacak şekilde fiyatlandır.
   - **Booking.com:** Ortalama %15–%18 komisyon (+ Genius/tercihli program varsa ek pay) nedeniyle, eline aynı net tutarın geçmesi için Booking liste fiyatını `P_net / (1 - komisyon_orani)` formülüyle yukarı ayarla.

3. **Dalaman Lokasyonuna Özel Sezon & Talep Çarpanları:**
   - **Yüksek Sezon (Haziran – Eylül):** Minimum konaklama 2–3 gece, hafta sonu +%15–20, erken rezervasyon indirimi sınırlı.
   - **Omuz Sezon (Nisan – Mayıs / Ekim):** Esnek 1 gece (havalimanı transit/gece uçuşu yolcuları için çok yüksek talep!), normal taban fiyat.
   - **Kış / Düşük Sezon (Kasım – Mart):** Haftalık (%15–20) ve Aylık (%30–40) uzun konaklama indirimleri + uçuş ekibi / iş seyahati / dijital göçebe vurgusu.
   - **Son Dakika (Son 72 Saat Boşluk Doldurma):** Boş kalacak geceye %15–25 kademeli indirim ("0 TL kazanmaktansa değişken maliyeti kurtar").

---

## ✨ 2. İlan & Dönüşüm Optimizasyonu (Listing CRO)

Bir Airbnb veya Booking.com ilanı iyileştirileceğinde şu 4 alanı denetle:

1. **Başlık Optimizasyonu (İlk 50 Karakter Kuralı):**
   - Mobilde kesilmeden en güçlü USP'yi (Unique Selling Proposition) ver:
     - *Örnek (EN):* `5 Min to DLM Airport | Pool, Fast WiFi & Balcony`
     - *Örnek (TR):* `Dalaman Havalimanı 5 Dk | Havuzlu & Fiber WiFi Suit`
2. **İlk 5 Fotoğraf Kuralı (Tıklama Oranı - CTR):**
   - 1. Fotoğraf: En aydınlık, geniş açılı ana yaşam alanı veya havuz/balkon manzaralı "Hero" kare.
   - 2–5. Fotoğraflar: Yatak odası, modern mutfak/banyo, havuz/site alanı, havalimanına yakınlık/otopark kolaylığı.
3. **Açıklama Yapısı (Tarayıcı Dostu Format):**
   - **Hemen Üstte (3 Madde):** Havalimanına uzaklık (dk/km), 7/24 Self Check-in kolaylığı, yüksek hızlı WiFi / klima / otopark.
   - **Bölümler:** Mekan Detayı → Konum & Plajlara Mesafe (Sarıgerme, İztuzu, Göcek) → Misafir Erişimi → Doğrudan İletişim/Web Avantajı.
4. **Booking.com & Airbnb Puan Yükseltme (Review Recovery):**
   - En çok puan kırdıran 3 alan (*Temizlik, Check-in İletişimi, Konum/Ulaşım Tarifi*) için önleyici rehber metinleri hazırla.

---

## 💬 3. Misafir İletişimi & Operasyon Şablonları (Çok Dilli: TR / EN / DE / RU)

Talep edildiğinde şu 4 kritik temas noktası için kopyala-yapıştır mesajlar üret:
1. **Anında Rezervasyon Karşılama:** Uçuş saatini sorma (Dalaman havalimanı geliş/gidiş saati erken/geç check-in planlaması için), transfer/taksi bilgisi.
2. **Check-in Öncesi (24 Saat Kala):** Google Maps pini, kapı/kutu şifresi, WiFi adı/şifresi, yakındaki market/restoran önerisi.
3. **Konaklama Ortası (1. Gece Sonrası Nabız Yoklama):** *"Her şey yolunda mı, eksiğiniz var mı?"* — sorun varsa yorumlara yansımadan çöz!
4. **Check-out & 5 Yıldız / 10 Puan Daveti:** Teşekkür + nazik değerlendirme ricası + bir sonraki gelişte `hotel-suites.example.com` üzerinden doğrudan rezervasyonda indirim hatırlatması.

---

## 📋 4. Standart Çıktı Formatı

Kullanıcı analiz veya fiyat önerisi istediğinde şu yapıda yanıt ver:
1. **Mevcut Durum & Rakip Özeti (BLUF):** Bölgedeki fiyat bandı ve en hızlı iyileştirme fırsatı.
2. **Kanal Fiyatlandırma Tablosu:** Doğrudan Site vs Airbnb vs Booking.com önerilen gece fiyatları ve net kazanç karşılaştırması.
3. **Aksiyon Planı:** Hemen uygulanacak başlık, fotoğraf, kural veya mesaj değişiklikleri.
