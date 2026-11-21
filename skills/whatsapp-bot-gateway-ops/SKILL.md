---
name: whatsapp-bot-gateway-ops
description: >-
  Dual-mode WhatsApp bot gateway engineering for booking-whatsapp-bot (CT 116, FastAPI) via
  WhatsAppProvider Adapter: Mode A (Baileys stability, anti-ban, CPU circuit breaker, E2EE
  recovery) and Mode B (Meta Cloud API, HMAC webhooks, 24h window/templates). Use when building,
  stabilizing, or migrating the WhatsApp bot. Do NOT use for STR pricing/listings (use
  str-revenue-listing-master), Telegram bots (use telegram-bot-alerting-ops), or LXC ops (use
  proxmox-ve-ops).
---

# 💬 WhatsApp Bot Gateway & Resmi Meta Cloud API Mühendislik Becerisi

Bu beceri; **bellopushon/whatsapp-cloud-api**, **davepoon/buildwithclaude (`whatsapp-automation`)** ve multi-device gateway kararlılık kalıplarını **Dalaman Airport Suites (`booking-whatsapp-bot` — `CT 116`, modüler FastAPI `core/`, `services/`, `routers/`)** mimarisine özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **WhatsApp gateway stabilitesi, kişisel numara ban koruması, FastAPI adapter mimarisi, webhook güvenliği ve Resmi Meta Cloud API geçişi** içindir. Oda fiyatlama/OTA komisyon/misafir metin dili için `str-revenue-listing-master`, LXC/yedekleme için `proxmox-ve-ops`, 502/DNS/SSL arızası için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik, Güvenlik ve İzolasyon İlkeleri

1. **Sıfır Düz Metin Sır:** Baileys `auth_info` / `creds.json` oturum dosyaları, Meta `Permanent System User Token`, `APP_SECRET`, `VERIFY_TOKEN`, İyzico API key'leri ve misafir pasaport/TC/telefon (KVKK/KBS) verileri asla loglara, git deposuna veya yanıtlara düz metin yazılmaz (`[MASKED]`).
2. **Panel Bağımsızlığı (Blast-Radius İzolasyonu):** WhatsApp gateway'i kopsa, oturumu düşse veya durdurulsa bile **FastAPI Web/Muhasebe/Rezervasyon paneli etkilenmemelidir.** Gateway çağrıları daima asenkron kuyruk / kısa timeout ile izole edilir.
3. **Adapter Pattern Zorunluluğu (`WhatsAppProvider`):** FastAPI `services/` ve `routers/` katmanı doğrudan Baileys veya Meta HTTP çağrısı yapmaz; tek bir soyut arayüz (`send_text`, `send_image`, `send_template`, `health_check`) üzerinden konuşur. Böylece **Mod A (Kişisel Hat/Gateway) ➔ Mod B (Resmi Meta Cloud API)** geçişi tek bir adapter değişimiyle sıfır kesintiyle yapılır.

---

## ⚙️ 1. Mod A: Canlı Kişisel Hat & Baileys Gateway Kararlılığı (Mevcut Sistem)

Kişisel numara üzerinden çalışan `booking-whatsapp-bot` gateway'inde en büyük 2 risk **%99 CPU reconnect döngüsü** ve **kişisel numara kısıtlaması (ban)**dır. Her kod değişikliği veya bakımda şu 4 kuralı zorunlu uygula:

1. **%99 CPU Sonsuz Döngü Koruması (Circuit Breaker):**
   - Bağlantı kopunca anında `while(true)` yeniden bağlanma yasaktır.
   - **Exponential Backoff** (`5s → 15s → 45s → 120s`, maks `5` deneme) + `DisconnectReason.loggedOut` (401) durumunda yeniden bağlanmayı durdurup yeni QR/Pairing Code iste.
   - `systemd` servisinde mutlaka kaynak tavanı tanımla: `CPUQuota=50%`, `MemoryMax=512M`, `Restart=on-failure`, `RestartSec=15s`, `StartLimitBurst=5`.
2. **Kişisel Numara Anti-Ban Hijyeni:**
   - **Toplu/Soğuk Mesaj Yasağı:** Kişisel hattan asla toplu reklam/kampanya yayını yapılmaz; yalnızca gerçek rezervasyon/misafir akışı ve iç personel grubu bildirimi gönderilir.
   - **İnsan Benzeri Tempo (Jitter & Rate Limit):** Ardışık mesajlar arasında rastgele `3–8 sn` gecikme, dakikada düşük üst sınır ve tekrarlanan hata durumunda kuyruğu duraklatma.
3. **E2EE / `Bad MAC` & Oturum Kalıcılığı (`store/auth/`):**
   - Oturum kimlik dizini yalnızca kalıcı yerel diskte (`chmod 600`) tutulur; container restart'ında silinmez.
   - `Bad MAC` / şifreleme senkron bozulmasında tüm oturumu körlemesine silmeden önce yalnızca bozuk peer session kaydını temizle veya kontrollü yeniden eşleştir.
4. **Sessiz Ölüm Önleme (`@your_noc_alert_bot` Alarmı):**
   - Gateway `loggedOut`, `401` veya 5 ardışık reconnect hatasına düştüğünde Telegram (`@your_noc_alert_bot`) üzerinden anlık uyarı fırlat (`Uptime Kuma` `/health` ucuyla birlikte izle).

---

## 🏛️ 2. Mod B: Hedef Resmi Meta WhatsApp Cloud API & Geçiş Planı
*(bellopushon/whatsapp-cloud-api & davepoon kurallarından uyarlanmıştır)*

Kurumsal hatta (Netgsm `0252`/`0850` sesli OTP) veya **Meta Coexistence** (mevcut WhatsApp Business App + Cloud API eşzamanlı çalışma) modeline geçildiğinde:

1. **API & Token Standardı:**
   - Uç nokta: `https://graph.facebook.com/v21.0/<PHONE_NUMBER_ID>/messages`
   - Geçici 24 saatlik token yerine **Business Manager → System User (Permanent Token)** kullan; yalnızca `whatsapp_business_messaging` ve `whatsapp_business_management` yetkileri ver.
2. **FastAPI Webhook Güvenliği & Idempotency:**
   - `GET /webhook`: `hub.mode == "subscribe"` ve sabit zamanlı (`hmac.compare_digest`) `hub.verify_token` doğrulaması → `hub.challenge` döndür.
   - `POST /webhook`: Ham gövde (raw body) üzerinde `X-Hub-Signature-256` HMAC-SHA256 imzasını `APP_SECRET` ile **zorunlu doğrula**; geçersiz imzayı `403` ile reddet.
   - **Hızlı 200 OK + Idempotency:** Meta tekrar gönderim (retry) yapar; gelen `messages[0].id` (`wamid.*`) değerini SQLite/cache'te saklayıp aynı mesajı ikinci kez işleme, ağır işleri (`BackgroundTasks`) arka planda çalıştır.
3. **24 Saat Pencere & Şablon Kategorisi Kuralları:**
   - **Misafirin başlattığı konuşmalar (Service — 24 saat penceresi):** Ücretsiz ve serbest metin/interaktif buton (`reply buttons`, `list messages`) gönderilebilir.
   - **24 saat dışı işletme başlatımlı mesajlar:** Yalnızca Meta onaylı **Template** ile gönderilebilir. Karşılama/Wi-Fi, KBS hatırlatma ve konaklama uzatma akışlarını **`UTILITY`** kategorisinde (promosyon dili eklemeden) onayla ki gereksiz `MARKETING` ücretine düşmesin.

---

## 🏨 3. Dalaman Suites Bot İş Akışları & Teknik Kısıtlar

`booking-whatsapp-bot` içindeki 4 çekirdek teknik akış her iki modda da (Baileys & Meta API) aynı `WhatsAppProvider` üzerinden çalışmalıdır:
1. **KBS (Emniyet Kimlik Bildirimi):** KVKK uyumlu tek kullanımlık, süreli form linki — pasaport görseli kalıcı açık dizinde tutulmaz.
2. **Dinamik VIP Barkod (`CT-DLM-VIP10`):** Görsel bellekten/geçici dizinden gönderilip temizlenir (disk şişmesi/TBW önlenir).
3. **İyzico Ödeme Linki (`Erken Giriş`, `Geç Çıkış`, `Cold Brew`, `Fast Track`):** Ödeme durumu webhook/callback ile doğrulanmadan personel grubuna "ödendi" bildirimi atılmaz.
4. **İç Operasyon / Temizlik Grubu Bildirimi:** Not: Resmi Meta Cloud API **WhatsApp gruplarına doğrudan mesaj göndermez**; Mod B'ye geçildiğinde iç personel bildirimi otomatik olarak bireysel WhatsApp mesajına veya Telegram grubuna yönlendirilmelidir!

---

## 📋 4. Standart Mühendislik Çıktı Formatı

1. **Aktif Mod & Risk Özeti:** Mod A (Baileys/Kişisel Hat) veya Mod B (Meta Cloud API) seçimi, ban/CPU/KVKK riski.
2. **Modüler Değişiklik Planı:** `core/` / `services/` / `routers/` ayrımını koruyan `WhatsAppProvider` uyumlu kod veya konfigürasyon.
3. **Doğrulama & Geri Dönüş:** `/health` testi, CPU/log kontrolü (`journalctl -u ...`), webhook imza testi veya geri alma adımı.
