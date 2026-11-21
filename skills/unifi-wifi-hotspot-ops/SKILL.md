---
name: unifi-wifi-hotspot-ops
description: >-
  Self-hosted UniFi OS Server (CT 107) Wi-Fi AP management (U6-Pro, U6+), RF channel/roaming
  optimization, L3 set-inform adoption, Dalaman 5651 External Captive Portal, and read-only
  drift/newcomer audits. Use when configuring UniFi Wi-Fi, hotspots, or Integration API
  (X-API-KEY). Do NOT use for OPNsense firewall/VLAN rules (use opnsense-proxmox-secops), CT 107
  Proxmox lifecycle (use proxmox-ve-ops), or WAN/502 outages (use homelab-network-troubleshoot).
---

# 📡 UniFi Wi-Fi, L3 Multi-Site & 5651 Hotspot Operasyon Becerisi

Bu beceri; **t3chnaztea/unifi-skills**, **Servosity/msp-skills (`unifi-network`)**, **colindickson/unifi**, **enuno/unifi-mcp-server** ve **brianbell-x/Unifi-MCP** en iyi pratiklerini **GölgeSiber (`LXC 107`) + Dalaman Airport Suites** hibrit UniFi mimarisine özel olarak birleştirir.

> **Kritik Mimari & Kapsam Sınırı:** Bu ağda **UDM Pro / UniFi Gateway YOKTUR.** Routing, NAT, DHCP ve VLAN arası firewall kuralları daima **OPNsense (`VM 101` → `opnsense-proxmox-secops`)** üzerindedir. UniFi yalnızca **Access Point, SSID-VLAN eşlemesi, Wi-Fi RF/roaming, L3 Adoption ve 5651 Misafir Hotspot / Captive Portal** katmanını yönetir.

---

## 🔒 0. Güvenlik Kapıları, Yedekleme ve API Disiplini

1. **İşlem Öncesi `.unf` Yedeği Zorunludur:** SSID, VLAN profili, Inform Host veya site ayarı değiştirmeden önce `Settings -> System -> Backups -> Download Backup` ile güncel `.unf` yedeğini al (`03-Storage_and_Backups/Unifi_Backups/`).
2. **Full-Object PUT Disiplini (`t3chnaztea` Altın Kuralı):** UniFi yerel REST API'sinde `PUT` çağrıları eksik bırakılan alanları varsayılana sıfırlayabilir veya mevcut ayarları silebilir. Her değişiklikte **önce `GET` ile tam nesneyi oku**, yalnızca hedef alanı güncelle ve tam nesneyle `PUT` gönder (onay kapısından sonra).
3. **Modern Kimlik Doğrulama (`X-API-KEY`):** UniFi Network 9.x+ resmi Integration API'sinde cookie/şifre yerine ortam değişkeninde tutulan **`X-API-KEY`** kullan; hiçbir API anahtarı, site parolası, SSH parolası veya misafir TC/telefon verisi loglara ya da yanıtlara yazılmaz (`[MASKED]`).
4. **`LXC 107` Güç & RAM Kuralı:**
   - Fethiye tekil Wi-Fi kullanımında `CT 107 (10.10.10.107:11443)` RAM tasarrufu (2 GB) için kapalı durabilir; AP bağımsız çalışır.
   - **Kritik Uyarı:** `Dalaman_Airport_Suites` **5651 External Captive Portal (`Authorize Guest`)** canlıya alındığında `CT 107` artık kapalı bırakılamaz — misafir kimlik doğrulaması için **7/24 açık** tutulmalıdır (32 GB RAM bütçesinde `proxmox-ve-ops` ile koordine et).

---

## 🧭 1. GölgeSiber Çift Şube UniFi Mimarisi

- **Merkez Controller:** `LXC 107 (unifi-os-server)` — `10.10.10.107/24` (VLAN 10 MGMT), Web UI: `https://10.10.10.107:11443` / `https://unifi.secops-domain.example.com` (NPM/NPMplus reverse proxy + AdGuard Split-DNS).
- **Şube 1 — Fethiye Data Center:** `UniFi U6-Pro AP` (`10.50.50.135`, VLAN 50 WIFI) → `Netgear GSS108E` Trunk → `vmbr2` → `OPNsense VM 101` (L3 Inform TCP `8080` kuralı).
- **Şube 2 — Dalaman (`Dalaman_Airport_Suites`):** Yerinde sunucu yok; tek `UniFi U6+` AP doğrudan internet üzerinden Fethiye merkeze L3 Inform ile bağlanır.

---

## 🌐 2. L3 Adoption (`set-inform`) & 5651 Dalaman Misafir Hotspot Protokolü

### A. L3 Set-Inform & Adoption Kontrolü
1. **Merkez Ön Koşulu:** OPNsense WAN'da yalnızca gerekli `TCP 8080` (mümkünse Dalaman kaynak IP / DDNS alias'ıyla kısıtlı) yönlendirmesi `10.10.10.107:8080` hedefine açık olmalıdır.
2. **AP Tarafı (`ssh ubnt@<AP-IP>`):**
   - Durum sorgula: `info` (Status: `Connected` mı, `Server Reject` mi, `Timeout` mu?)
   - L3 bağla: `set-inform http://unifi.secops-domain.example.com:8080/inform` (yerel Fethiye ağı için `http://10.10.10.107:8080/inform`).
   - *İpucu:* Adoption sırasında komutun ilk `Adopt` tıklamasından sonra bir kez daha gönderilmesi gerekebilir; ardından Controller'da `Settings -> System -> Advanced -> Inform Host` ayarının tutarlı olduğunu doğrula.

### B. 5651 Uyumlu External Captive Portal (`portal.hotel-suites.example.com`)
1. **SSID Kurulumu:** `Dalaman_Airport_Suites` sitesi altında `Open` + `Guest Hotspot (External Portal Server)` + **Client Device Isolation** (misafirler birbirini göremesin) aktif olmalıdır.
2. **Pre-Authorization Allowances (Ön İzinler):** Yalnızca portal sunucusu (`portal.hotel-suites.example.com`), gerekli DNS/NTP ve (gerekliyse) SMS/kimlik doğrulama uç noktalarına erişim ver; geniş internet erişimini `Authorize Guest` gelene kadar kapalı tut.
3. **Kimlik & 5651 Kriptografik Log Bütünlüğü:**
   - Yerli misafir: MERNIS TC doğrulama; yabancı turist: SMS OTP.
   - Doğrulama sonrası `IP, MAC, Tarih/Saat, Süre` kaydı 5651 zaman damgalı kasaya (Nextcloud/PBS) yazıldıktan sonra UniFi API üzerinden `Authorize Guest` (örn. 24 saat, hız limiti uygulanmış) tetiklenir; yetki sonrası `hotel-suites.example.com` karşılama sayfasına yönlendirilir.

---

## 📶 3. Wi-Fi RF, Kanal Planlama & Roaming Standartları
*(t3chnaztea & enuno optimizasyon kurallarından uyarlanmıştır)*

- **2.4 GHz:** Yalnızca `20 MHz` kanal genişliği ve çakışmayan `1 / 6 / 11` kanalları; gücü `Low/Medium` tut (istemcileri 5 GHz'e doğal yönlendir).
- **5 GHz:** Ev/butik otel ortamında `40 MHz` veya temiz spektrumda `80 MHz`; DFS kanal radar düşüşü yaşanıyorsa non-DFS kanallara (`36–48`, `149–161`) sabitle.
- **Güvenlik & İzolasyon:** Kurumsal/ev SSID'lerinde `WPA2/WPA3` + `PMF Optional/Required` (eski IoT cihazlarında PMF uyumluluğunu kontrol et); Misafir/IoT SSID'lerinde L2 Client Isolation + OPNsense tarafında RFC1918 blokajı (`opnsense-proxmox-secops`).
- **Auto-Optimize / Nightly Channel Optimization:** İstemci kopmalarına yol açabileceği için körlemesine açık bırakma; önce RF taraması (`RF Scan`) yapıp manuel temiz kanal seç.

---

## 🔍 4. Salt-Okunur Drift & Yeni Cihaz (Newcomer) Denetimi
*(Servosity/msp-skills unifi-network metodolojisinden uyarlanmıştır)*

Ağ sağlığı veya güvenlik denetimi istendiğinde (ileride `unifimcp.com` veya `Servosity` Read-Only MCP bağlandığında da aynı mantıkla):
1. **Config Drift (Ayar Sapması):** Son doğrulanan duruma göre değişen SSID, VLAN etiketi, RF gücü, portal ayarı veya AP firmware sürümünü raporla.
2. **Newcomer (Yeni Katılan Cihazlar):** Son 7 günde Fethiye veya Dalaman ağlarına ilk kez bağlanan bilinmeyen MAC/cihazları listele.
3. **AP Sağlık Karnesi:** Her AP için `Uptime`, `Connected Clients`, `TX Retries (>%15 uyarı)`, `Channel Utilization (>%60 uyarı)` ve `L3 Inform` durumunu özetle.

---

## 📋 5. Standart Operasyon Çıktı Formatı

1. **Hedef Şube & Ön Koşul:** Fethiye (`U6-Pro`) / Dalaman (`Dalaman_Airport_Suites`), `CT 107` çalışma durumu ve `.unf` yedek kontrolü.
2. **Adım Adım Uygulama (UniFi UI / SSH / API):** Net menü yolu veya salt-okunur/onaylı komutlar.
3. **Doğrulama & Sınır Kontrolü:** `info` / istemci bağlantı testi / 5651 portal testi ve gerekiyorsa OPNsense (`opnsense-proxmox-secops`) eşleştirme notu.
