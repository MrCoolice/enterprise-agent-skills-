---
name: code-security-audit
description: >
  Adversarial 6-phase source-code security audit and vulnerability hunting (confirmed/rejected) for Next.js, FastAPI, PHP, and Python codebases.
---

# 🔬 Kaynak Kod Güvenlik Denetimi (Adversarial Code Audit — Cloudflare Metodolojisi)

Bu beceri; Cloudflare'ın açık kaynak yaptığı **`cloudflare/security-audit-skill`** (6 fazlı, kapsam güdümlü ve çürütme doğrulamalı güvenlik açığı keşif motoru) metodolojisini **GölgeSiber yazılım projelerine** (`golgesiber-v3`, `booking-whatsapp-bot`, `golgekitabevi-wp`, `pve-interactive-bot.py`) uyarlar.

> **Altın İlke:** Bir yapay zekâ şüphesi **asla doğrudan "güvenlik açığı" olarak raporlanmaz.** Kaynak kod yolu satır satır izlenmeden, güven sınırı (trust boundary) kanıtlanmadan ve aksini ispatlama (adversarial disproving) denemesi başarısız olmadan hiçbir bulgu `confirmed` (doğrulandı) sayılmaz.

> **Kapsam Sınırı:** Bu beceri **uygulama kaynak kodu güvenlik denetimi (SAST / mantık & yetki açıkları)** içindir. OPNsense `config.xml`/VLAN denetimi için `opnsense-proxmox-secops`, Cloudflare WAF/NPMplus/CrowdSec için `cloudflare-edge-proxy-secops`, canlı kesinti teşhisi için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Denetim Güvenlik & Gizlilik Sınırları

1. **Salt-Okunur & Ağsız Keşif (Offline-First):** Denetim sırasında canlı sistemlere izinsiz aktif sömürü (exploit) veya ağ taraması yapılmaz; analiz tamamen kaynak kod, konfigürasyon ve şema üzerinden yürütülür.
2. **Sır Maskeleme:** Kodda tesadüfen bulunan API anahtarı, `.env` sırrı, JWT secret, şifre veya token'lar asla rapora düz metin kopyalanmaz (`[REDACTED]` + dosya:satır referansı verilir).
3. **Bağımsız Durum Takibi (Büyük Repolarda):** Geniş denetimlerde bağlam kaymasını önlemek için bulgular kalıcı yerel dosyalara (`architecture.md`, `coverage-ledger.json`, `findings.json`, `REPORT.md`) işlenir.

---

## 🧭 1. Cloudflare 6 Fazlı Güvenlik Denetim Hattı

Bir depo, PR veya kritik modül denetimi istendiğinde şu **6 fazı sırayla** uygula:

### Faz 1: Keşif & Güven Sınırı Haritası (Reconnaissance)
- Mimariyi, giriş noktalarını (HTTP API, Server Actions, Webhooks, CLI/Telegram komutları, dosya yüklemeleri, cron), kimlik doğrulama sınırlarını ve veri depolarını (SQLite/Prisma, MySQL/WP, dosya sistemi) haritala.
- İncelenecek tüm modülleri kapsam defterine (`coverage-ledger`) böl ki kritik hiçbir dosya atlanmasın.

### Faz 2: Kapsam Odaklı Açık Avı (Coverage-Led Hunting)
Her birim için **girdi → doğrulama → işlem → çıktı** veri akışını izle; özellikle GölgeSiber yığınına özgü yüksek riskli sınıfları tara:
- **Next.js 16 / React 19 / Prisma (`golgesiber-v3` & 22+ Siber Araç):** Server Action auth eksikliği, RSC → Client hassas alan sızıntısı, IP/URL/DNS araçlarında **SSRF** (RFC1918/169.254/loopback erişimi), **ReDoS**, **Command Injection**, `proxy.ts` bypass, `$queryRawUnsafe`.
- **FastAPI / Baileys / İyzico (`booking-whatsapp-bot`):** Kasa/muhasebe uçlarında eksik oturum/rol kontrolü (**IDOR / Broken Auth**), İyzico/Meta webhook **HMAC imza eksikliği** veya replay (idempotency yokluğu), KBS pasaport yüklemesinde path traversal / açık web dizini, `uploads/receipts/` dosya tipi sahteciliği.
- **WordPress / PHP (`golgekitabevi-wp`):** `golge-*` ve `stats-ajax` uçlarında eksik `check_ajax_referer()`, eksik `current_user_can()`, `$wpdb->prepare()` olmadan SQL birleştirme, `esc_html/esc_attr` eksikliği (XSS), rate-limit aşımı.
- **Python / Bash Botları (`pve-interactive-bot.py` & nöbetçiler):** `ALLOWED_CHAT_IDS` atlatma, `shell=True` / `os.system` komut enjeksiyonu, regexsiz `VMID` parametresi, token log sızıntısı.

### Faz 3: Adversarial Aday Doğrulama (Çürütme Kapısı)
Faz 2'den çıkan her bulgu yalnızca bir **Aday (Candidate)**dır. Her adayı taze gözle **çürütmeye çalış**:
- Üst katmanda (proxy, middleware, Zod şeması, ORM parametreleştirme, rol kontrolü) bunu engelleyen gerçek bir savunma var mı?
- Saldırganın gerçekten kontrol edebildiği bir kaynak (source) bu tehlikeli hedefe (sink) kesintisiz ulaşıyor mu?
- Çürütülürse **`rejected`** olarak elenir; yalnızca kodda kanıtlanamayan harici ortam şartına bağlıysa **`needs_validation`** olarak ayrılır.

### Faz 4 & 5: Yapılandırılmış Kayıt & Bağımsız Kod Doğrulaması
Her onaylanan bulgu şu kanıt alanlarını **eksiksiz** taşımalıdır:
- **Durum:** `confirmed` | `needs_validation` | `rejected`
- **Önem Derecesi:** `Kritik (🔴)` | `Yüksek (🟠)` | `Orta (🟡)` | `Düşük (🟢)`
- **Kanıt Zinciri:** Tam dosya yolu + satır numaraları (`dosya.ts:42 -> servis.ts:88`) + gerçek sömürü ön koşulları (varsayım yok!).

### Faz 6: Hedef-Bağımsız Aksiyon Raporu
Çıktıyı şu net yapıda sun:
1. **Yönetici Özeti (BLUF):** Taranan kapsam, toplam `confirmed` / `needs_validation` / `rejected` sayısı ve en acil 3 risk.
2. **Doğrulanmış Bulgular Tablosu:** ID | Önem | Dosya:Satır | Güven Sınırı | Etki | Durum.
3. **Detaylı Kanıt & Minimal Düzeltme Yaması:** Her `confirmed` bulgu için kesin kök neden, güvenli kod yaması ve regresyon test önerisi (`pytest` / unit test).
4. **Doğrulama Gerektirenler (`NEEDS-VALIDATION`):** Canlı ortamda (ör. NPMplus/Cloudflare/izinler) manuel teyit gerektiren maddeler.

---

## 🛡️ 2. OWASP Cheat Sheet Serisi Kural Matrisi (`OWASP/CheatSheetSeries`)

Her kod denetiminde endüstri standardı **OWASP Cheat Sheet** maddeleri karşılaştırma referansı (baseline) olarak alınır:

1. **SSRF Prevention:** Dış URL/IP çeken araçlarda (`golgesiber-v3` network toolları) RFC1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), link-local (169.254.0.0/16) ve loopback (127.0.0.1) IP'lerine doğrudan DNS çözümlemesi öncesi/sonrası bloklama kuralı.
2. **Session Management & JWT:** Algoritma (`none`) zafiyeti kontrolü, `HttpOnly; Secure; SameSite=Lax/Strict` çerez bayrakları ve JWT secret entropi seviyesi.
3. **REST Security & Input Validation:** Zod/Pydantic şema denetimi, JSON payload boyut sınırı ve CORS başlıklarının asla `Access-Control-Allow-Origin: *` ile kimlik bilgisi (credentials) taşımaması.
4. **SQL Injection Defense:** Ham string birleştirme yasağı; Prisma parametrik sorgular (`$queryRaw` tagged template) ve WP-CLI `$wpdb->prepare` zorunluluğu.
5. **Cryptographic Storage:** Şifreler için `Argon2id` veya `bcrypt` (min 12 cost) ve hassas API token'ları için AES-256-GCM.

---

## 🔍 3. OSINT & Kimlik/Yüzey Güvenliği Denetimi

1. **Sherlock Profil & Sızıntı Avcısı (`sherlock-project/sherlock`):** Sistem yöneticisi veya şirket kullanıcı adlarının 400+ platformda açıkta olup olmadığını denetleyerek sosyal mühendislik ve hedefli kimlik avı yüzeyini haritalama.
2. **Kablosuz Ağ & Hotspot Güvenliği (`derv82/wifite2` & UniFi Köprüsü):** Misafir ve operasyonel Wi-Fi ağlarında zayıf WPA2-PSK, açık WPS PIN ve PMKID sızıntılarını test ederek kurumsal VLAN izolasyonunu doğrula (Detaylar: `unifi-wifi-hotspot-ops`).
