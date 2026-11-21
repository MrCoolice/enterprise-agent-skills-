---
name: nextcloud-selfhosted-ops
description: >-
  Self-hosted Nextcloud (VM 103, nc.secops-domain.example.com) occ maintenance, PHP/Redis/APCu/cron tuning,
  config.php trusted_proxies, OnlyOffice (CT 100) JWT/sleep troubleshooting, and
  WebDAV/Collectives/Deck automation. Use when running occ commands, repairing Nextcloud, or
  integrating OnlyOffice/WebDAV. Do NOT use for VM 103 Proxmox/ZFS/PBS ops (use proxmox-ve-ops),
  502 debugging (use homelab-network-troubleshoot), or OPNsense rules (use
  opnsense-proxmox-secops).
---

# ☁️ Nextcloud Self-Hosted Operasyon, `occ` Bakım & WebDAV Becerisi

Bu beceri; resmi **nextcloud/nextcloud-skills** (üretim sunucusu/`occ` bakımı), **AlexMili/nextcloud-skill** ve **keithvassallomt/openclaw-nextcloud** en iyi pratiklerini **GölgeSiber Veri Merkezi (`VM 103: nc.secops-domain.example.com` + `CT 100: OnlyOffice`)** mimarisine özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **Nextcloud uygulama içi `occ` yönetimi, `config.php`/PHP/Redis/cron optimizasyonu, OnlyOffice entegrasyonu ve WebDAV/Collectives/Deck API otomasyonu** içindir. `VM 103` snapshot/disk/PBS yedeği için `proxmox-ve-ops`, 502/DNS/SSL kesintisi için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik, Yedekleme ve Bakım Güvenliği

1. **Kimlik Bilgisi Hijyeni:** Nextcloud App Password'ları (`rclone`, WebDAV, SMTP), veritabanı parolaları, OnlyOffice `JWT_SECRET` ve `config.php` salt/secret değerleri asla loglara, dokümanlara veya yanıtlara düz metin yazılmaz (`[MASKED]`).
2. **Büyük Değişiklik Öncesi FAZ 0 Kuralı:** Nextcloud sürüm yükseltme, veritabanı şema dönüşümü veya toplu `files:scan` öncesi mutlaka:
   - `VM 103` için Proxmox snapshot (`vmstate=0`) + güncel `config.php` yedeği alınır,
   - Bakım modu açılır (`occ maintenance:mode --on`), işlem bitince kapatılır (`--off`).
3. **Doğru Kullanıcıyla `occ` Çalıştırma:** `occ` komutları **asla `root` ile doğrudan çalıştırılmaz** (dosya izinlerini bozar); daima web sunucusu kullanıcısıyla (`sudo -u www-data php /var/www/nextcloud/occ ...`) çalıştırılır.

---

## 🧭 1. GölgeSiber Nextcloud Altyapı Bağlamı (`VM 103` + `CT 100`)

- **Ana Sunucu:** `VM 103 (NextCloud)` — `10.10.30.103` (VLAN 30 CLOUD), `4 vCPU / 8 GB RAM / 100 GB` (`HDD_Havuz`), Kurumsal URL: `https://nc.secops-domain.example.com`.
- **Ofis Motoru:** `CT 100 (OnlyOffice)` — `10.10.30.108` (VLAN 30 CLOUD). **Kritik Uyku Kuralı:** `00:00 – 08:30` arası gece uykusundadır; bu saatlerde belge açma hatası görülürse önce `CT 100` uyku durumu kontrol edilir (`/start 100`).
- **Ters Vekil & Gerçek IP Uyumu:** Cloudflare + NPM (`10.10.10.106`) → NPMplus (`10.10.10.120`). Proxy geçişinde `/var/www/nextcloud/config/config.php` içindeki `trusted_domains`, `trusted_proxies`, `overwrite.cli.url` ve `overwriteprotocol => 'https'` alanları senkron tutulmalıdır.
- **Aktif Temel Uygulamalar:** `Collectives` (ana bilgi üssü), `GroupFolders`, `Two-Factor MFA`, `rclone WebDAV` (`ProxmoxHostBackups` hedefi).

---

## 🛠️ 2. Üretim `occ` Bakım, Sağlık ve Performans Protokolü
*(Resmi `nextcloud/nextcloud-skills` operasyon standartlarından uyarlanmıştır)*

### A. Salt-Okunur Sağlık & Uyarı Taraması (Önce Oku)
```bash
sudo -u www-data php /var/www/nextcloud/occ status
sudo -u www-data php /var/www/nextcloud/occ setupchecks
sudo -u www-data php /var/www/nextcloud/occ app:list
sudo -u www-data php /var/www/nextcloud/occ background-job:list --limit=10
```

### B. Sürüm Sonrası & Rutin Onarım Komutları (Onaylı)
- Eksik veritabanı indeksleri ve sütun onarımları:
  `sudo -u www-data php /var/www/nextcloud/occ db:add-missing-indices`
  `sudo -u www-data php /var/www/nextcloud/occ db:add-missing-columns`
  `sudo -u www-data php /var/www/nextcloud/occ db:add-missing-primary-keys`
  `sudo -u www-data php /var/www/nextcloud/occ maintenance:repair --include-expensive`
- **Performans & Bellek Hijyeni (`8 GB RAM` + SSD TBW koruması):**
  - Arka plan işleri daima **System Cron** (`*/5 * * * * www-data php -f /var/www/nextcloud/cron.php`) ile çalışmalı (AJAX cron kullanma).
  - Yerel önbellek için `APCu` (`memcache.local`), dağıtık kilit/oturum için `Redis` (`memcache.locking`) aktif tutulmalı; gereksiz önizleme (preview) şişmesini önlemek için `preview_max_x/y` ve `jpeg_quality` sınırlandırılmalı.
  - `files:scan` tüm sunucuda körlemesine (`--all`) değil, yalnızca gereken kullanıcı/klasör yolunda (`--path="/kullanici/files/Klasor"`) çalıştırılmalı.

---

## 🔗 3. OnlyOffice (`CT 100`) & WebDAV / Collectives / Deck Otomasyonu
*(AlexMili/nextcloud-skill & keithvassallomt/openclaw-nextcloud desenlerinden uyarlanmıştır)*

1. **OnlyOffice Entegrasyon Kontrolü:**
   - Hem Nextcloud hem OnlyOffice tarafında `JWT_SECRET` eşleşmeli ve `Authorization` başlığı ters vekilde (NPM/NPMplus) düşürülmemelidir.
   - İç ağ (Split-DNS) üzerinden `nc.secops-domain.example.com` ve OnlyOffice birbirine geçerli SSL sertifikasıyla ulaşabilmelidir.
2. **Güvenli API & WebDAV Erişimi:**
   - Otomasyonlar (`rclone`, betikler, harici araçlar) için ana hesap parolası **asla kullanılmaz**; her servis için ayrı, iptal edilebilir **App Password** (`Settings -> Security -> Devices & sessions`) üretilir.
   - Standart uç noktalar:
     - **WebDAV (Dosyalar / Collectives):** `https://nc.secops-domain.example.com/remote.php/dav/files/<USER>/`
     - **CalDAV / CardDAV (Takvim, Görevler, Kişiler):** `https://nc.secops-domain.example.com/remote.php/dav/`
     - **OCS / Notes / Deck API:** `OCS-APIRequest: true` + `Accept: application/json` başlıkları zorunludur.
   - `Collectives` klasörü yerel dosya izleyici (`watcher.py`) ve masaüstü Nextcloud istemcisiyle senkron olduğu için toplu dosya silme/yeniden adlandırma öncesi çakışma (`conflicted copy`) riskini kontrol et.

---

## 📋 4. Standart Operasyon Çıktı Formatı

1. **Ön Koşul & Risk:** `VM 103` snapshot / `maintenance:mode` gereksinimi ve `CT 100` uyku penceresi kontrolü.
2. **Adım Adım `occ` / `config.php` / API Komutları:** Daima `www-data` ile, yorumlu ve geri alınabilir komutlar.
3. **Doğrulama:** `occ status`, `occ setupchecks`, `nextcloud.log` kontrolü ve bakım modunun kapalı (`maintenance: false`) olduğunun teyidi.
