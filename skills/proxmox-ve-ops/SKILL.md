---
name: proxmox-ve-ops
description: >
  Proxmox VE (pvenew) VM/LXC lifecycle (qm/pct), ZFS pool & SSD TBW protection, FAZ 0 snapshots, PBS (VM 102) backup audits, and PVE REST API automation.
---

# 🖥️ Proxmox VE, ZFS, PBS & API Operasyon Uzman Becerisi

Bu beceri; **eddygk/proxmox-ops**, **Servosity/msp-skills**, **Redth/homelab-assist**, **hanseo0507/proxmox-api-skill** ve **Getty/skills** en iyi pratiklerini **GölgeSiber Veri Merkezi (`pvenew`)** mimarisine özel olarak birleştirir.

> **Kapsam Sınırı:** Bu beceri **sanallaştırma yaşam döngüsü, depolama/ZFS/TBW, PBS yedek doğrulama ve PVE REST API** operasyonlarını yönetir. OPNsense `config.xml`/VLAN güvenlik denetimi için `opnsense-proxmox-secops`, canlı ağ/DNS/502 arıza teşhisi için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik, Güvenlik Kapıları ve GölgeSiber Altın Kuralları

### A. 3 Kademeli Operasyon Güvenlik Kapısı (Safety Gates)
1. **Salt-Okunur (Read-Only):** `qm list`, `pct list`, `zpool status`, `pvesm status`, `smartctl`, API `GET` çağrıları — doğrudan önerilebilir/çalıştırılabilir.
2. **Geri Alınabilir (Reversible):** Start/stop/shutdown, snapshot (RAM hariç), servis yeniden başlatma — etki notu ve varsa asenkron **UPID** takibiyle yapılır.
3. **Yıkıcı / Kritik (Destructive):** VM/LXC silme, disk genişletme/bölümleme, ZFS pool değişikliği, snapshot rollback, `/etc/pve/` (`pmxcfs`) manuel müdahalesi — **önce açık kullanıcı onayı + FAZ 0 yedek/snapshot zorunludur.**

### B. `pvenew` Donanım & Kaynak Koruma Kısıtları
- **Tek Node + 32 GB RAM Bütçesi:** Yeni VM/LXC planlarken toplam RAM tahsisini 32 GB sınırına göre kontrol et; uyku/arşiv servislerinin (`CT 100`, `VM 102`, `CT 105`, `CT 107`, `VM 112`) RAM payını hesaba kat.
- **SSD TBW & Ömür Koruması (`HDD_Havuz` ZFS Mirror — 2x WD Red SA500):**
  - Gereksiz disk yazımı üreten işlemlerden (sürekli debug loglama, gereksiz swap, sık tam RAM snapshot) kaçın.
  - **Snapshot Kuralı:** Çalışan bellek durumunu saklamak şart değilse **asla `vmstate=1` (Include RAM) kullanma**; VM'i dondurur ve diskte yüksek I/O + TBW yükü oluşturur.
- **Gizlilik:** Gerçek parola, `PVEAPIToken` secret, rclone/OpenSSL arşiv anahtarı veya özel SSH anahtarını asla düz metin olarak yanıta yazma (`[MASKED]`).

---

## ⚙️ 1. Günlük VM & LXC Yaşam Döngüsü (`qm` / `pct`)

Önce oku, sonra müdahale et (*Read first, then act*):

1. **Durum ve Envanter Kontrolü:**
   - VM'ler: `qm list`, `qm config <VMID>`, `qm status <VMID> --verbose`
   - LXC'ler: `pct list`, `pct config <CTID>`, `pct df <CTID>`
   - Guest Agent IP keşfi (`agent: 1` aktif VM'lerde): `qm guest cmd <VMID> network-get-interfaces`
2. **Temiz Kapatma ve Bakım Farkındalığı:**
   - Zorla `stop` yerine her zaman `qm shutdown` / `pct shutdown` tercih et.
   - `VM 102 (PBS)` veya `CT 100 (OnlyOffice)` üzerinde işlem yaparken **Uptime Kuma (`CT 110`) bakım pencerelerini** ve **`pbs-power-scheduler.sh` aktif `vzdump` kilidini** bozma; PBS'i asla aktif `vzdump` sürerken kapatma.
   - Yeni VM/LXC açılırken `pve-interactive-bot.py` (`@your_noc_alert_bot`) ve `Uptime Kuma` envanterine eklenmesini hatırlat.

---

## 💾 2. Depolama, ZFS Sağlığı ve Uçtan Uca Disk Büyütme

### A. Depolama & ZFS Sağlık Kontrolü (`HDD_Havuz`, `local`, `local-lvm`, `Acil_Kurtarma_120G`)
- Havuz ve alan durumu: `zpool status -x`, `zpool list`, `zfs list -o name,used,avail,refer,compressratio`, `pvesm status`
- Thin-pool & NVMe kontrolü: `lvs -a` (thin-pool doluluğu %80'i geçerse acil uyarı ver).
- SSD aşınma & sıcaklık: `smartctl -A /dev/<disk>` (`Media_Wearout_Indicator` / `Percentage Used` ve sıcaklık kontrolü).

### B. Uçtan Uca Disk Büyütme Protokolü (Hypervisor + Guest)
Disk büyütme tek komutla bitmez; her zaman şu sırayı ver ve **önce snapshot al**:
1. **Hypervisor:** `qm resize <VMID> scsi0 +10G` (veya LXC için `pct resize <CTID> rootfs +5G` — LXC genelde dosya sistemini otomatik büyütür).
2. **Guest Bölümleme (VM içinde):**
   - GPT yedek başlığını onar ve bölümü genişlet: `parted /dev/sda print` → `Fix` → `parted /dev/sda resizepart <NO> 100%` (veya `growpart /dev/sda <NO>`).
3. **LVM (varsa):** `pvresize /dev/sda<NO>` → `lvextend -l +100%FREE /dev/<vg>/<lv>`
4. **Dosya Sistemi:** `resize2fs /dev/<device>` (ext4) veya `xfs_growfs /` (XFS), ardından `df -h` ile doğrula.

---

## 🛡️ 3. Salt-Okunur PVE & PBS Yedek Doğrulama Denetimi
*(Servosity/msp-skills doğrulama metodolojisinden uyarlanmıştır)*

Bir yedekleme görevinin "yeşil" görünmesi gerçek geri dönüş garantisi değildir. Yedek sağlığı sorulduğunda şu **4 katmanı çapraz kontrol et**:

1. **Zamanlama Kapsamı (`/etc/pve/jobs.cfg`):** Çalışan her üretim VM/LXC (`101, 103, 106/104, 108, 109, 110, 113, 114, 115, 116`) aktif bir yedek işine dahil mi?
2. **Gerçek Arşiv & Verify Durumu (`PBS_BackUp` / `VM 102`):** Yalnızca yedek dosyasının varlığına değil, PBS üzerinde **Verify (doğrulama) durumunun başarılı ve güncel** olmasına bak.
3. **`vzdump` Görev Logları:** Son çalışmalarda uyarı, kilit zaman aşımı veya atlanan guest var mı? (`pbs-power-scheduler.sh` uyku penceresi çakışması kontrolü).
4. **Host Konfigürasyon Hibrit Yedeği:** `/usr/local/bin/pve-hybrid-backup.sh` ve `pbs-hybrid-backup.sh` çıktılarının (`/var/lib/pve-cluster/config.db` + `/etc/proxmox-backup/`) AES-256 şifreli olarak Nextcloud ve Mega'ya 30 gün retention ile aktığını doğrula.

**Çıktı Kuralı:** Denetim sonunda her misafir (VM/LXC) için net bir **"Doğrulanmış Geri Dönüş Noktası Kararı"** tablosu ver (`VMID | Görev | Son Yedek | Verify Durumu | Karar: Sağlam / Eksik / Riskli`).

---

## 🔌 4. Proxmox REST API & En Az Yetki (Least Privilege) Standartları
*(Redth/homelab-assist & hanseo0507/proxmox-api-skill kalıplarından uyarlanmıştır)*

Proxmox API otomasyonu veya harici izleme entegrasyonu kurulurken:
1. **Şifre Yerine Privilege-Separated API Token Kullan:**
   ```bash
   # Salt-okunur denetim / izleme için (önerilen varsayılan)
   pveum user add auditor@pve
   pveum user token add auditor@pve readonly --privsep 1
   pveum acl modify / --tokens 'auditor@pve!readonly' --roles PVEAuditor
   ```
   - *Önemli Not:* PVE, standart dizin/NFS/CIFS depolarındaki (`local`, `Acil_Kurtarma_120G`) yedek dosyalarını listelemek için `PVEAuditor` yetkisini tek başına yeterli görmez; gerekiyorsa yalnızca ilgili depoya özel daraltılmış rol (`Datastore.Audit` / `VM.Backup`) tanımla. PBS tarafında **`Audit`** rolü tam salt-okunur yeterlidir.
2. **Kimlik Bilgisi Hijyeni:** Token secret'ı asla koda veya markdown'a gömme; ortam değişkeni (`PVE_HOST`, `PVE_TOKEN_ID`, `PVE_TOKEN_SECRET`) veya OS secret store kullan.
   - Header biçimi: `Authorization: PVEAPIToken=USER@REALM!TOKENNAME=SECRET-UUID`
3. **Asenkron Görev (UPID) Takibi:** Mutating API çağrıları (`POST`/`PUT`/`DELETE`) işlem bitmeden **UPID** döndürür. İşlemi bitmiş sayma; `GET /nodes/pvenew/tasks/{upid}/status` ve `/log` üzerinden `status == "stopped"` ve `exitstatus == "OK"` doğrula.

---

## 📋 5. Standart Operasyon Çıktı Formatı

Her Proxmox operasyon, bakım veya yedekleme talebinde yanıtı şu net yapıda sun:
1. **Risk & Ön Koşul (FAZ 0):** İşlem sınıfı (Read-Only / Reversible / Destructive), snapshot/yedek gereksinimi, RAM/TBW ve uyku penceresi etkisi.
2. **Adım Adım Komutlar / API Akışı:** Doğrudan `pvenew` üzerinde uygulanabilir, yorumlu komutlar.
3. **Doğrulama & Geri Dönüş (Rollback):** İşlemin başarıyla tamamlandığını kanıtlayan kontrol komutu ve sorun halinde geri alma adımı.
