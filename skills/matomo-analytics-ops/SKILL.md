---
name: matomo-analytics-ops
description: >-
  Self-hosted Matomo analytics (CT 114, matomo.secops-domain.example.com) Reporting API queries, JS
  tracking & KVKK privacy audits for secops-domain.example.com, hotel-suites.example.com, and
  ecommerce.example.com. Use when pulling traffic, landing pages, referrers, conversions, or
  auditing Matomo tracking. Do NOT use for writing SEO articles (use seo-content-master), LXC
  ops (use proxmox-ve-ops), or 502 debugging (use homelab-network-troubleshoot).
---

# 📊 Matomo Analytics & Veri İstihbaratı Uzman Becerisi

Bu beceri; **AgriciDaniel/claude-seo (`seo-matomo`)** ve **enuno/claude-command-and-control (`matomo-api`)** standartlarını **GölgeSiber self-hosted Matomo (`LXC 114` — `https://matomo.secops-domain.example.com`)** altyapısına özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **Matomo Reporting/Tracking API veri analizi, dönüşüm/trafik istihbaratı ve takip kodu/KVKK doğrulaması** içindir. Makale yazımı için `seo-content-master`, LXC/ZFS/yedekleme için `proxmox-ve-ops`, 502/SSL/DNS arızası için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik, Token Güvenliği ve Salt-Okunur Varsayılanı

1. **Kimlik Bilgisi Hijyeni:** `MATOMO_API_TOKEN` (`token_auth`) asla markdown, script veya URL loglarına düz metin yazılmaz; ortam değişkeni (`MATOMO_URL`, `MATOMO_API_TOKEN`, `MATOMO_SITE_ID`) veya yalnızca kullanıcıya okunabilir (`chmod 600`) yerel config dosyasından okunur.
2. **POST Gövdesi Kuralı:** `token_auth` değerini URL query string (`?token_auth=...`) yerine **HTTP `POST` body** içinde gönder ki ters vekil (NPM/NPMplus) ve tarayıcı loglarına sızmasın.
3. **Salt-Okunur Öncelik:** Varsayılan olarak yalnızca veri okuma (`*.get*`) metotlarını kullan; yeni hedef (`Goals.addGoal`), site veya kullanıcı oluşturan yazma çağrıları için önce açık kullanıcı onayı al.

---

## 🧭 1. GölgeSiber Matomo Altyapı Bağlamı (`LXC 114`)

- **Kurumsal Adres:** `https://matomo.secops-domain.example.com` (`LXC 114`, `10.10.30.106:80`, VLAN 30 CLOUD).
- **Ters Vekil & Gerçek Ziyaretçi IP'si:** Cloudflare Proxied → NPM (`10.10.10.106`) / NPMplus (`10.10.10.120`).
  - *Kritik Kontrol:* Reverse proxy değişiminde (NPM → NPMplus) `/opt/matomo/config/config.ini.php` içindeki `trusted_proxies[]` ve `proxy_client_headers[]` (`HTTP_CF_CONNECTING_IP` / `HTTP_X_FORWARDED_FOR`) güncel değilse tüm ziyaretçiler proxy IP'si gibi görünür — analitik sapma görürsen ilk bunu kontrol et.
- **Takip Edilen Ana Varlıklar:** `secops-domain.example.com`, `hotel-suites.example.com`, `ecommerce.example.com`.

---

## 🔌 2. Matomo Reporting API Kalıpları & Sık Yapılan Tuzaklar

### A. Temel Sorgu Şablonu (Güvenli POST)
```bash
curl -sS -X POST "${MATOMO_URL}/index.php" \
  -d "module=API" \
  -d "method=VisitsSummary.get" \
  -d "idSite=${MATOMO_SITE_ID}" \
  -d "period=range" \
  -d "date=last30" \
  -d "format=JSON" \
  -d "token_auth=${MATOMO_API_TOKEN}"
```

### B. En Sık Kullanılan Analiz Metotları
| Analiz Amacı | Matomo API Metodu | Kullanım Alanı |
| :--- | :--- | :--- |
| **Genel Trafik Özeti** | `VisitsSummary.get` | Ziyaret (`nb_visits`), tekil ziyaretçi, hemen çıkma oranı (`bounce_rate`), ortalama süre |
| **Giriş Sayfaları (SEO)** | `Actions.getEntryPageUrls` (`flat=1&filter_limit=25`) | En çok trafik çeken & yüksek bounce oranlı landing page'ler |
| **Çıkış & Sayfa Performansı** | `Actions.getPageUrls`, `Actions.getExitPageUrls` | Kullanıcıyı kaybeden sayfalar ve içerik derinliği |
| **Organik & Yönlendirme Kaynakları** | `Referrers.getAll`, `Referrers.getSearchEngines`, `Referrers.getWebsites` | Google/Keşfet, sosyal medya ve yönlendirme kanalı payları |
| **Cihaz & Ülke Dağılımı** | `DevicesDetection.getType`, `UserCountry.getCountry` | Mobil/masaüstü oranı (Keşfet & `hotel-suites.example.com` turist dağılımı) |
| **Hedef & Dönüşüm (CRO)** | `Goals.get`, `Events.getCategory` | WhatsApp tıklaması, rezervasyon formu, affiliate/kitap tıklamaları |

### C. Kritik Matomo Tuzakları (GA4 ile Karıştırma!)
1. **Terminoloji Farkı:** Matomo GA4'teki *"Sessions / Events"* yerine **`Visits` (Ziyaret)** ve **`Actions` (Eylem: sayfa görüntüleme, indirme, dış link, özel olay)** kullanır; raporlarda bu ayrımı doğru adlandır.
2. **Tarih & Periyot Uyumu:** İki tarih arası (`2026-10-01,2026-10-31`) veya `last30` sorgularken `period=range` kullan; `period=day` + `date=last30` günlük zaman serisi (30 ayrı gün) döndürür.
3. **Düz Liste (`flat=1`):** `Actions.getPageUrls` varsayılan olarak klasör ağacı döndürür; tek tek URL kıyaslamak için `flat=1` parametresini ekle.

---

## 🛡️ 3. Takip Kodu (`matomo.php`) & KVKK / Performans Denetimi

Web sitelerinde (`secops-domain.example.com`, `hotel-suites.example.com`, `ecommerce.example.com`) Matomo entegrasyonu denetlenirken şu **5 noktayı** kontrol et:
1. **Tek Kurumsal Uç Nokta:** Eski `matomo.d8el.dedyn.io` referansı yerine `//matomo.secops-domain.example.com/` kullanılıyor mu?
2. **KVKK & Çerezsiz İzleme:** Gereksiz çerez yükü olmadan IP maskeleme (2 bayt anonymization) ve `disableCookies` / rıza uyumu doğru mu?
3. **Core Web Vitals Etkisi:** `matomo.js` script'i `async` / `defer` ile yükleniyor mu, LCP'yi bloke etmiyor mu?
4. **Dönüşüm Olayları (Event Tracking):** Kritik CTA'lar (WhatsApp rezervasyon butonu, telefon tıklaması, form gönderimi, dış link) `trackEvent` ile ölçülüyor mu?
5. **Kendi Trafiğini Hariç Tutma:** Admin/ofis trafiği veya `Uptime Kuma` bot taramaları raporu şişiriyor mu?

---

## 🔗 4. SEO & Büyüme Geri Besleme Döngüsü (Cross-Skill Handoff)

Matomo verisini ham sayı olarak bırakma; ilgili uzman beceriye aksiyon olarak bağla:
- **Yüksek trafik + yüksek bounce (>%70) veya düşen trendli blog sayfaları** → `seo-content-master` (Mod B: Quick Wins / BLUF ve CTR güncellemesi) için hedef URL listesi çıkar.
- **Yüksek mobil çıkış / yavaş sayfa metrikleri** → `web-quality-modern-guidance` için LCP/mobil UX denetim listesi ver.
- **Dalaman Suites (`hotel-suites.example.com`) ülke/cihaz/WhatsApp dönüşüm hunisi** → `str-revenue-listing-master` için dil/pazar önceliği öner.

---

## 📋 5. Standart Analitik Rapor Formatı

1. **Yönetici Özeti (BLUF):** Dönem, `idSite`, toplam ziyaret, organik pay ve 1 cümlelik ana bulgu.
2. **Performans Tablosu:** En iyi 5 ve acil iyileştirme gerektiren 5 sayfa/kanal (Ziyaret | Bounce | Ort. Süre | Dönüşüm).
3. **Öncelikli 3 Aksiyon:** Doğrudan uygulanabilir SEO, CRO veya teknik takip önerisi.
