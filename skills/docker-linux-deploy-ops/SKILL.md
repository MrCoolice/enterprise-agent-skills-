---
name: docker-linux-deploy-ops
description: >-
  Debian 13 LXC/VM application layer, Docker Compose hardening, systemd units, logrotate/TBW
  protection, and zero-downtime GitHub-to-LXC deployment (CT 115, CT 116, CT 104, CT 108). Use
  when writing Dockerfiles, compose.yaml, systemd services, or deploy/rollback pipelines. Do NOT
  use for Proxmox host/ZFS/PBS (use proxmox-ve-ops), Nextcloud occ (use
  nextcloud-selfhosted-ops), or WordPress WP-CLI (use wordpress-woocommerce-ops).
---

# 🐳 Docker Compose, Debian 13 `systemd` & GitHub → LXC Deployment Becerisi

Bu beceri; resmi **docker/skills** (`docker-compose-patterns` ve konteyner güvenliği), **peterbamuhigire/linux-skills**, **HermeticOrmus/linux-sysadmin-skills** ve **mukul975/Anthropic-Cybersecurity-Skills** standartlarını **GölgeSiber LXC/VM uygulama katmanına** uyarlar.

> **Kapsam Sınırı:** Bu beceri **VM/LXC içindeki Linux/Debian 13 yönetimi, Docker Compose sertleştirme, `systemd` servis tasarımı ve GitHub → LXC canlıya alma (deploy)** içindir. Proxmox host/qm/pct/ZFS/PBS için `proxmox-ve-ops`, Nextcloud `occ` için `nextcloud-selfhosted-ops`, WordPress/WP-CLI için `wordpress-woocommerce-ops` kullanılır.

---

## 🔒 0. Gizlilik, Kaynak Tavanı ve TBW Koruma Kuralları

1. **Sırlar Asla İmajda veya Git'te Olmaz:** `.env`, API token, veritabanı şifresi ve SSH anahtarları `.gitignore` ve `.dockerignore` içinde dışlanır; sunucuda `chmod 600` ile yalnızca ilgili servis kullanıcısına okunur tutulur.
2. **32 GB RAM & WD Red SSD TBW Koruması (`pvenew` Kısıtı):**
   - Her Docker konteynerinde ve `systemd` servisinde **bellek/CPU tavanı zorunludur** (tek bir sızıntı `OOM-Killer` tetiklemesin).
   - Docker log sürücüsünde **her zaman `max-size` + `max-file` rotasyonu** tanımlanır; `journald` için `SystemMaxUse=150M` ve geçici cache/session yazımları mümkünse `tmpfs` üzerinde tutulur ki ZFS SSD aşınması (TBW) önlensin.
3. **Deploy Öncesi Rollback Garantisi:** Canlıya almadan önce mevcut çalışan commit hash'i (`git rev-parse --short HEAD`) not edilir; büyük sürümde önce `proxmox-ve-ops` ile LXC snapshot (`vmstate=0`) alınır.

---

## 🗺️ 1. GölgeSiber Proje ⟷ LXC Deployment Haritası

| Proje | Yerel (`Windows`) | Repo | Hedef LXC & IP | Yığın / Servis |
| :--- | :--- | :--- | :--- | :--- |
| **GolgeSiber-v3** | `C:\Projects\golgesiber-v3` | `admin_user/golgesiber-v3` | `CT 115` (`10.10.10.104`) | Next.js 16 + React 19 + TS + SQLite/Prisma (`systemd` / PM2) |
| **Dalaman Suites** | `C:\Projects\booking-whatsapp-bot` | `admin_user/booking-whatsapp-bot` | `CT 116` (`10.10.10.116`) | FastAPI + Baileys (`/opt/dalaman-suite/app`, `dalaman-suite.service`, `dalaman-gateway.service`) |
| **GolgeKitabeviWP** | `C:\Projects\golgekitabevi-wp` | `admin_user/golgekitabevi-wp` | `CT 113` (`10.10.10.113`) | WordPress / PHP 8.4-FPM (`/var/www/html/wordpress`) |
| **Dashboard** | `C:\Projects\golgesiber-dashboard` | `admin_user/golgesiber-dashboard` | `CT 108` (`10.10.10.101`) | Node.js |
| **NPMplus** | — | Alpine 3.24 + Docker | `CT 104` (`10.10.10.120`) | Docker Compose (`NPMplus` + `CrowdSec Bouncer` + `GoAccess`) |

---

## 🐳 2. Üretim Docker & `compose.yaml` Sertleştirme Standartları
*(Resmi `docker/skills` desenlerinden uyarlanmıştır)*

1. **İmaj & Build Hijyeni:**
   - `:latest` yerine sabit sürüm etiketi (`node:22-alpine`, `python:3.12-slim`) ve **multi-stage build** kullan.
   - Konteyneri asla `root` çalıştırma (`USER nonroot`), `cap_drop: [ALL]` uygula ve sadece gereken yetkiyi (`NET_BIND_SERVICE` vb.) geri ver; `security_opt: [no-new-privileges:true]` ekle.
2. **`compose.yaml` Zorunlu Sağlık & Limit Bloğu:**
   ```yaml
   restart: unless-stopped
   read_only: true
   tmpfs: ["/tmp"]
   deploy:
     resources:
       limits: { cpus: "1.5", memory: 512M }
   logging:
     driver: json-file
     options: { max-size: "10m", max-file: "3" }
   healthcheck:
     test: ["CMD-SHELL", "curl -fsS http://127.0.0.1:8000/health || exit 1"]
     interval: 30s
     timeout: 5s
     retries: 3
   ```
3. **Ağ İzolasyonu:** Veritabanı veya iç servis portlarını asla `0.0.0.0` üzerinden dışa açma; yalnızca dahili Compose ağı veya `127.0.0.1:<port>` bağla.

---

## ⚙️ 3. Debian 13 `systemd` Sertleştirme & Sıfır Kesintili GitHub → LXC Deploy

### A. `systemd` Servis Sertleştirme Şablonu
FastAPI (`dalaman-suite.service`), Node.js (`golgesiber-v3`) veya Python daemon'ları için:
- `User=<uygulama_kullanicisi>`, `EnvironmentFile=/etc/golgesiber/<app>.env` (`chmod 600`)
- `Restart=on-failure`, `RestartSec=10s`, `StartLimitIntervalSec=300`, `StartLimitBurst=5`
- `MemoryMax=512M`, `CPUQuota=75%`
- Sandbox korumaları: `NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectSystem=strict`, `ReadWritePaths=/opt/<app>/data`

### B. Güvenli GitHub → LXC Canlıya Alma Akışı (6 Adım)
1. **Yerel Doğrulama (Windows):** Test / lint / build (`npm run build` veya `python -m py_compile`) → `git status` (sır/çöp dosya yok) → `git commit` → `git push origin main`.
2. **Hedef LXC Ön Kontrol:** `pct enter <CTID>` → `git rev-parse --short HEAD` (geri dönüş hash'i kaydet) ve `df -h` / `free -m` kontrolü.
3. **Temiz Kod Çekme:** `git fetch origin && git pull --ff-only origin main` (canlıda kirli merge çatışması oluşturma).
4. **Veritabanı Yedeği, Bağımlılık & Build:**
   - SQLite/Prisma projelerinde (`CT 115`, `CT 116`) migrasyon öncesi tutarlı sıcak yedek al (`sqlite3 <db>.db ".backup '<db>_pre_deploy.db'"`) ve ardından **`npx prisma migrate deploy`** çalıştır *(üretimde asla `db push --force-reset` kullanma!)*.
   - Lockfile değiştiyse `npm ci && npx prisma generate && npm run build` veya `venv/bin/pip install -r requirements.txt` (Next.js'te eski `.next` kesintisini önlemek için build bitmeden servisi durdurma!).
5. **Kontrollü Yeniden Başlatma:** `systemctl daemon-reload && systemctl restart <servis>` → `systemctl is-active <servis>`.
6. **Canlı Sağlık Doğrulama:** `curl -fsS http://127.0.0.1:<port>/health` + `journalctl -u <servis> -n 30 --no-pager`. Hata varsa 10 saniyede `git checkout <eski_hash>` + restart ile geri dön.

---

## 📋 4. Standart Deployment Çıktı Formatı

1. **Hedef LXC & Risk:** Konteyner ID/IP, RAM/TBW tavanı ve geri dönüş (rollback) commit/snapshot noktası.
2. **Uygulanabilir Dosya / Komutlar:** Sertleştirilmiş `compose.yaml`, `systemd` unit veya adım adım deploy komutları.
3. **Doğrulama:** Healthcheck, `systemctl status`, `docker ps` / `journalctl` çıktısı ve rollback komutu.
