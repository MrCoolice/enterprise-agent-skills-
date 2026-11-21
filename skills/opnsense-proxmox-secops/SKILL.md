---
name: opnsense-proxmox-secops
description: >-
  Enterprise OPNsense (VM 101) static config.xml 7-layer security audits, VLAN/DMZ segmentation,
  WireGuard/NAT/Unbound hardening, and Proxmox bridge/host network hardening. Use when auditing
  OPNsense config.xml, designing VLAN/firewall architecture, or hardening WireGuard/Proxmox
  bridges. Do NOT use for daily Proxmox VM/LXC/ZFS/PBS ops (use proxmox-ve-ops) or live
  outage/502 troubleshooting (use homelab-network-troubleshoot).
---

# 🛡️ OPNsense, Proxmox & Homelab SecOps Uzman Becerisi

Bu beceri; **opnsense-audit**, **claude-network-skills** ve **08-network-security** çerçevelerinin **OPNsense + Proxmox VE + Homelab/Kurumsal Ağ** yapısına özel olarak birleştirilmiş halidir. Canlı sisteme bağlanmadan, yalnızca paylaştığınız `config.xml`, ağ şemaları, `/etc/network/interfaces` veya Proxmox VM/LXC çıktılarını analiz ederek kurumsal seviyede denetim ve mimari tasarım yapar.

> **Kapsam Sınırı:** Bu beceri **statik güvenlik denetimi, VLAN/DMZ mimarisi ve zırhlama** içindir. Günlük Proxmox VM/LXC/ZFS/PBS ve REST API operasyonları için `proxmox-ve-ops`, canlı kesinti/DNS/SSL/502 arıza teşhisi için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik ve Güvenlik Kuralı (Config Paylaşımı Öncesi)

Kullanıcı bir `config.xml` veya sistem çıktısı paylaştığında:
1. Dosyadaki **parola hash'lerini**, **WireGuard/OpenVPN private key'lerini**, **API secret'larını** ve **dinamik DNS tokenlarını** asla düz metin olarak yanıta kopyalama (gerekirse `[MASKED]` olarak özetle).
2. Eğer kullanıcı ham `config.xml` yüklemeden önce temizlemek isterse, hassas alanları maskeleyen hızlı PowerShell/Python temizlik komutu öner.

---

## 🔍 1. OPNsense `config.xml` Tam Güvenlik Denetimi (Audit Pipeline)

Bir OPNsense `config.xml` dosyası verildiğinde denetimi şu **7 katmanlı sırayla** gerçekleştir ve bulguları **Kritik (🔴) / Orta (🟡) / İyileştirme (🟢)** olarak raporla:

### Katman 1: Yönetim Düzlemi ve Erişim Sınırları (Management Plane)
- **Web GUI (`<webgui>`):** HTTP'den HTTPS'e zorunlu yönlendirme aktif mi? Port değiştirilmiş mi? GUI tüm arayüzlere mi açık, yoksa sadece `MGMT` / `LAN` VLAN'ına mı kısıtlı? WAN üzerinden GUI erişimi kesinlikle kapalı mı?
- **SSH (`<openssh>`):** Root login kapalı mı? Şifre ile giriş yerine SSH Key-Only aktif mi?
- **Kullanıcılar ve Yetkiler (`<user>`, `<group>`):** Varsayılan `root` hesabı dışında günlük yönetim hesabı var mı? API kullanıcıları `admins` grubunda mı yoksa en az yetki (Least Privilege) prensibiyle mi tanımlı?

### Katman 2: Arayüzler, VLAN Segmentasyonu ve Köprüler (`<interfaces>`, `<vlans>`)
- **İzolasyon Kontrolü:** IoT, Misafir, Sunucu/DMZ, Yönetim (MGMT) ve Güvenilir (Trusted LAN) ağları ayrı VLAN'lara bölünmüş mü?
- **WAN Koruması:** WAN arayüzünde `Block private networks` (RFC1918) ve `Block bogon networks` aktif mi? (CGNAT arkasında özel durum varsa not et.)

### Katman 3: Güvenlik Duvarı Kuralları ve Mantık Analizi (`<filter>`)
- **Any-to-Any Açıkları:** `Pass * to *` şeklinde aşırı geniş izin veren kurallar var mı?
- **Yatay Hareket (Lateral Movement) Riski:** DMZ veya IoT VLAN'ından LAN/MGMT ağlarına erişimi açık bırakan eksik `Block RFC1918` kuralları var mı?
- **Gölge (Shadowed) ve Çakışan Kurallar:** Üstteki bir kural yüzünden hiç tetiklenmeyen (dead/unreachable) kuralları tespit et.
- **Kural Sıralaması ve Loglama:** Kritik `Block/Reject` kurallarında loglama açık mı? Floating kurallar yerel kuralları istemeden eziyor mu?

### Katman 4: NAT, Port Yönlendirme ve CGNAT (`<nat>`)
- **Dışa Açık Servisler (`<rule>`):** Hangi portlar internete açık? (`22`, `3389`, `8006` Proxmox GUI, `443` gibi kritik portlar doğrudan internete açık mı?)
- **Kaynak IP Kısıtlaması & Alias:** Port yönlendirmelerde `GeoIP` veya belirli kaynak IP alias'ı kullanılmış mı?
- **NAT Reflection (Hairpin NAT):** İç ağdan dış domain/IP üzerinden yerel sunucuya erişim gerekiyorsa NAT Reflection veya Split DNS doğru kurgulanmış mı?

### Katman 5: DNS, DHCP ve Ağ Hijyeni (`<unbound>`, `<dhcpd>`)
- **Unbound DNS:** DNS-over-TLS (DoT) veya DNSSEC aktif mi? Rebind protection açık mı?
- **Split DNS:** İç servisler (Proxmox, NAS, oyun sunucusu) için dış IP yerine yerel IP döndüren Host Override kayıtları var mı?
- **DHCP:** Statik IP atamaları (MAC-IP eşleşmeleri) ve NTP sunucu ayarları tutarlı mı?

### Katman 6: VPN ve Uzaktan Erişim (`<wireguard>`, `<openvpn>`, `<ipsec>`)
- **WireGuard:** Peer'ların `AllowedIPs` tanımı daraltılmış mı (`0.0.0.0/0` vs belirli subnet)? Artık kullanılmayan eski cihaz anahtarları var mı?
- **VPN Kural İzolasyonu:** VPN üzerinden bağlanan istemciler tüm iç ağa mı yoksa sadece izin verilen sunuculara mı erişebiliyor?

### Katman 7: IDS/IPS, Sertifikalar ve Yedekleme (`<suricata>`, `<cert>`, `<cron>`)
- **Sertifikalar:** Süresi dolmuş veya yakında dolacak SSL/ACME sertifikaları var mı?
- **Suricata / CrowdSec:** IDS/IPS modu (Promiscuous/IPS) doğru arayüzlerde aktif mi?
- **Otomatik Yedekleme:** Config backup (Nextcloud/Google Drive/SFTP) yapılandırılmış mı?

---

## 🖥️ 2. Proxmox VE & Homelab Ağ Mimarisi Tasarımı

Kullanıcı Proxmox `/etc/network/interfaces`, VM/LXC listesi veya ağ topolojisi paylaştığında:
1. **Linux Bridge vs OVS Analizi:** `vmbr0` (Management/LAN), `vmbr1` (VLAN-aware trunk veya izole DMZ) yapısını kontrol et.
2. **Proxmox Güvenlik Zırhlama:** Port `8006`'nın sadece yönetim VLAN'ından veya VPN üzerinden erişilebilir olmasını, 2FA/TOTP ve Fail2ban kurallarını doğrula.
3. **Çift Katmanlı Koruma:** Proxmox Host Firewall vs OPNsense VM Firewall çakışmalarını ve performans etkilerini denetle.
4. **Görselleştirme:** Mevcut veya önerilen yapıyı mutlaka net bir **Mermaid** ağ diyagramı ile çiz.

---

## 📋 3. Standart Raporlama Çıktısı

Denetim veya tasarım istendiğinde çıktıyı şu formatta sun:
1. **Yönetici Özeti (BLUF):** Genel güvenlik skoru / durum özeti (1 paragraf).
2. **Bulgular Tablosu:** Önem Derecesi | Kategori | Tespit Edilen Sorun | Risk | Çözüm Adımı.
3. **Adım Adım Düzeltme Rehberi:** OPNsense Web GUI menü yolu (`Firewall -> Rules -> ...`) ile birebir uygulanabilir talimatlar.
4. **Topoloji Şeması:** Varsa ağ segmentasyonunu gösteren Mermaid diyagramı.
