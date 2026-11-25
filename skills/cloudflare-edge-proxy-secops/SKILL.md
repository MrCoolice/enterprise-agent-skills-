---
name: cloudflare-edge-proxy-secops
description: >
  Cloudflare Edge, WAF, Zero Trust Tunnel, NPMplus (CT 106/104), CrowdSec LAPI, and CF-Connecting-IP operations. Use for Cloudflare DNS/WAF/tunnels and reverse proxy hosts.
---

# 🌐 Cloudflare Edge, Zero Trust, NPMplus & CrowdSec SecOps Becerisi

Bu beceri; resmi **cloudflare/skills** ve resmi **crowdsecurity/crowdsec-skill** (WAF/AppSec/Bouncer) standartlarını **GölgeSiber kenar güvenlik & ters vekil katmanına** (`Cloudflare Edge/Zero Trust` → `OPNsense CrowdSec LAPI` → `LXC 104 NPMplus / LXC 106 NPM`) özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **Cloudflare DNS/WAF/Zero Trust Tunnel, NPM/NPMplus ters vekil konfigürasyonu ve CrowdSec bouncer/AppSec senaryoları** içindir. OPNsense `config.xml`/VLAN tasarımı için `opnsense-proxmox-secops`, canlı 502/SSL/DNS arıza teşhisi için `homelab-network-troubleshoot`, Proxmox LXC/snapshot işlemleri için `proxmox-ve-ops` kullanılır.

---

## 🔒 0. Gizlilik ve Sıfır Kesinti Kuralları

1. **Kimlik Bilgisi Hijyeni:** Cloudflare API Token, `cloudflared` tunnel credential JSON, CrowdSec LAPI Bouncer key, NPMplus admin parolası ve Origin Private Key asla yanıta veya repoya düz metin yazılmaz (`[MASKED]`).
2. **En Az Yetkili Cloudflare Token:** Global API Key kullanma; yalnızca gereken zone ve yetkiye (örn. `Zone:DNS:Edit`, `Zone:Firewall Services:Read`) daraltılmış Scoped API Token kullan.
3. **Kırmadan Geçiş (FAZ 0):** Reverse proxy host, WAF kuralı veya Cloudflare SSL modu değiştirmeden önce mevcut proxy konfigürasyonunu yedekle (`LXC 104/106` snapshot + `Acil_Kurtarma` ham yedeği) ve yeni kuralı önce `Log / Managed Challenge` modunda gözlemle.

---

## 🧭 1. GölgeSiber Kenar & Ters Vekil Mimarisi

- **Kenar Kalkanı:** Cloudflare Edge (Proxied DNS + WAF + DDoS) ve dışa port açmadan yönetim erişimi için **`cloudflared` Zero Trust Tunnel** (MFA/TOTP zorunlu).
- **Ters Vekil Geçişi (`VLAN 20 - WEB`):**
  - Mevcut: `LXC 106 (NPM)` — `10.10.10.106:81`
  - Hedef / Yeni Nesil: `LXC 104 (NPMplus)` — **`10.10.10.120`** (Alpine 3.24 + Docker, Admin `:81`, GoAccess canlı analitik `https://10.10.10.120:91`, HTTP/3 QUIC, ModSecurity WAF).
- **Merkezi CrowdSec LAPI:** `OPNsense VM 101` (`10.10.10.1:8080`, `WEB_VLAN -> This Firewall 8080`) ⟷ `crowdsec-npmplus-bouncer`.
- **Çekirdek Proxy Servisleri:** `hotel-suites.example.com` (`10.10.10.116:80`), `secops-domain.example.com` (`10.10.10.104`), `ecommerce.example.com` (`10.10.10.113`), `nc.secops-domain.example.com` (`10.10.30.103`), `matomo.secops-domain.example.com` (`10.10.30.106:80`), `unifi.secops-domain.example.com` (`10.10.10.107:11443`).

---

## ☁️ 2. Cloudflare DNS, SSL/TLS, WAF & Zero Trust Standartları
*(Resmi `cloudflare/skills` karar ağaçlarından uyarlanmıştır)*

1. **SSL/TLS Altın Kuralı:** Asla `Flexible` bırakma (redirect loop ve şifresiz iç bacak riski). Her zaman **`Full (Strict)`** + geçerli Let's Encrypt (DNS-01 / HTTP-01) veya 15 yıllık Cloudflare Origin Sertifikası kullan.
   - *Not:* Let's Encrypt HTTP-01 yenilemesinde sorun çıkarsa geçici `DNS Only` yerine kalıcı **Cloudflare DNS-01 API Token** doğrulamasına geç.
2. **Zero Trust Access & `cloudflared`:**
   - Proxmox (`8006`), OPNsense GUI, Uptime Kuma (`3001`), NPMplus (`81`) ve GoAccess (`91`) gibi yönetim panelleri **asla doğrudan internete açılmaz**; yalnızca VLAN 10 MGMT, WireGuard VPN veya **Cloudflare Zero Trust Access (e-posta + TOTP/MFA politikası)** arkasından erişilir.
3. **WAF & Cache Kuralları:**
   - WordPress (`ecommerce.example.com`) için `/wp-login.php` ve `/xmlrpc.php` uçlarında Managed Challenge / Rate Limit uygula; `/wp-admin/*` ve `nc.secops-domain.example.com` dinamik API yollarını cache dışı (`Bypass Cache`) tut.
   - Gerçek ziyaretçi IP'si için `CF-Connecting-IP` başlığı NPMplus → Nextcloud (`trusted_proxies[]`) ve Matomo (`proxy_client_headers[]`) zincirinde tutarlı aktarılmalıdır.

---

## 🛡️ 3. CrowdSec Bouncer, AppSec WAF & NPMplus Operasyonları
*(Resmi `crowdsecurity/crowdsec-skill` desenlerinden uyarlanmıştır)*

1. **Bouncer & LAPI Sağlık Kontrolü (Salt-Okunur):**
   - `cscli bouncers list` (NPMplus bouncer `valid` ve son çekim zamanı güncel mi?)
   - `cscli metrics` (parsing/bucket/bouncer istatistikleri), `cscli decisions list` (aktif banlar), `cscli collections list`.
2. **Yanlış Pozitif (False Positive) Önleme:**
   - **Zorunlu Whitelist:** İç RFC1918 VLAN'lar (`10.10.10.0/24`, `10.10.10.0/24`, `10.10.30.0/24`, `10.40.40.0/24`, `192.168.1.0/24`) ve kendi statik/yönetici IP'lerin için CrowdSec parser whitelist tanımlı olmalıdır — özellikle `Uptime Kuma` (`10.10.10.110`) veya `Nextcloud` senkronizasyon istemcisinin yanlışlıkla banlanmasını önle!
   - ModSecurity / CrowdSec AppSec açılırken önce Nextcloud WebDAV (`PROPFIND`/`PUT`/`MKCOL`), OnlyOffice JWT (`Authorization` header) ve WordPress admin post'larında false positive testi yap.
3. **NPMplus Proxy Host Hijyeni:**
   - Her serviste: `Force SSL`, `HTTP/2 + HTTP/3 (QUIC)`, WebSocket gereken servislerde (`Nextcloud`, `OnlyOffice`, `Uptime Kuma`, `UniFi`, `Dalaman Bot`) **Websockets Support = ON**, `HSTS` ve temiz `X-Forwarded-For` / `X-Real-IP` başlıkları.

---

## 📋 4. Standart SecOps Çıktı Formatı

1. **Etkilenen Katman & Risk:** Cloudflare Edge / Zero Trust / NPMplus (`CT 104`) / CrowdSec LAPI.
2. **Uygulanabilir Konfigürasyon / Kural:** Adım adım Cloudflare paneli, NPMplus host ayarı veya `cscli` komutları.
3. **Doğrulama & False-Positive Testi:** `curl -Iv` header/HTTP3 testi, `cscli decisions list`, Nextcloud/Matomo gerçek IP kaydı teyidi ve geri alma planı.
