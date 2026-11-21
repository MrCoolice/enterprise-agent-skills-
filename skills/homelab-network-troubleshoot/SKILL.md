---
name: homelab-network-troubleshoot
description: >-
  Read-only-first 6-step live network & service diagnostics across Client -> VLAN/UniFi ->
  OPNsense (VM 101) -> AdGuard (CT 109) -> NPM/NPMplus (CT 106/104) -> Cloudflare -> LXC/VM. Use
  when debugging live outages, DNS failures, 502/503/504 errors, TLS issues, VLAN drops, or
  pfctl/tunnel problems. Do NOT use for static OPNsense config.xml audits (use
  opnsense-proxmox-secops) or Proxmox VM/ZFS/PBS tasks (use proxmox-ve-ops).
---

# 🩺 Homelab & Veri Merkezi Canlı Ağ Arıza Giderme Becerisi

Bu beceri; **CacinieP/network-troubleshoot-skill** metodolojisini **GölgeSiber Veri Merkezi** canlı trafik zincirine uyarlar. Tahmin yürütmek yerine **önce salt-okunur tanı, sonra kök neden açıklaması, ardından geri alınabilir çözüm** disiplinini zorunlu kılar.

> **Kapsam Sınırı:** Bu beceri **canlı bağlantı, DNS, SSL/TLS, Reverse Proxy (502/504), VLAN erişimi ve Cloudflare Tunnel arızalarını teşhis eder.** Statik OPNsense `config.xml` güvenlik denetimi ve yeni VLAN tasarımı için `opnsense-proxmox-secops`, Proxmox VM/ZFS/PBS operasyonları için `proxmox-ve-ops` kullanılır.

---

## 🔒 0. Teşhis Güvenlik Kuralları (Kırmadan Teşhis)

1. **Önce Salt-Okunur (Read-Only First):** Durum değiştirmeden önce yalnızca hedefli, salt-okunur tanı komutları (`dig`, `curl -Iv`, `ss`, `nc -zv`, `journalctl`, OPNsense `Live View`) çalıştır/öner.
2. **Güvenliği Kapatarak "Çözüm" Yasaktır:** SSL/TLS hatalarında `curl -k`, `NODE_TLS_REJECT_UNAUTHORIZED=0`, `git config --global http.sslVerify false` veya firewall'da `Pass * to *` gibi güvensiz geçici yolları asla kalıcı çözüm olarak önerme.
3. **Onaysız Durum Değişikliği Yok:** Kullanıcı onayı olmadan sistem proxy ayarlarını, VPN/tünel konfigürasyonunu, firewall kurallarını veya DNS resolver ayarlarını değiştirme.
4. **Gizlilik:** Log ve `curl` çıktılarındaki Bearer token, cookie, Cloudflare tunnel secret, API key veya kişisel IP bilgilerini asla düz metin olarak yanıta taşıma (`[MASKED]`).

---

## 🧭 1. GölgeSiber Canlı Trafik Zinciri (Katmanlı İz Sürme Haritası)

Bir servis açılmadığında körlemesine aramak yerine hatayı şu **7 durak** arasında izole et:

```text
[1] İstemci / Yerel OS (Windows/Linux/Mobil - Proxy, VPN, Hosts, DNS Cache)
  ➔ [2] Katman 2 (Netgear GSS108E Switch 10.10.10.239 / UniFi U6-Pro 10.50.50.135 / vmbr2 Trunk)
  ➔ [3] DNS Çözümleme (AdGuard Home CT 109: 10.40.40.109 ➔ OPNsense Unbound Split DNS)
  ➔ [4] L3 & Firewall (OPNsense VM 101: 192.168.1.5 — VLAN kuralları, Alias, NAT, CrowdSec)
  ➔ [5] Kenar & Tünel (Cloudflare Edge WAF/SSL veya cloudflared Zero Trust Tunnel)
  ➔ [6] Ters Vekil (NPM CT 106: 10.10.10.106 veya NPMplus CT 104: 10.10.10.120 + CrowdSec Bouncer)
  ➔ [7] Hedef Servis (VLAN 10/20/30/40 içindeki hedef VM/LXC portu ve systemd/Docker servisi)
```

---

## 🏷️ 2. Hata Sınıflandırma Matrisi (Belirti → Kök Neden → Hedefli Test)

| Belirti / Hata Kodu | Olası Kök Neden | İlk Salt-Okunur Teşhis Komutu / Kontrolü |
| :--- | :--- | :--- |
| **`ENOTFOUND` / `NXDOMAIN` / `ERR_NAME_NOT_RESOLVED`** | AdGuard blokajı, OPNsense Unbound Split DNS eksikliği, yerel DNS cache veya yanlış resolver | `nslookup <domain> 10.40.40.109` ve `nslookup <domain> 192.168.1.5` (AdGuard Query Log kontrolü) |
| **`ECONNREFUSED`** | Hedef VM/LXC kapalı (ör. uyku modundaki `CT 100` / `VM 102`), servis çökmüş veya yanlış port | `pct status <ID>` / `qm status <ID>`, hedef içinde `ss -tulpn`, `systemctl status <servis>` |
| **`ETIMEDOUT` / `ECONNRESET`** | OPNsense VLAN arası `Block IC_AGLAR` kuralı, eksik alias, CrowdSec IP banı, yanlış VLAN tag (Switch/vmbr2) | OPNsense `Firewall -> Log Files -> Live View` (hedef/kaynak IP filtrele), `cscli decisions list`, `nc -zv -w 3 <IP> <PORT>` |
| **`HTTP 502 / 503 / 504` (Bad Gateway / Timeout)** | NPM/NPMplus upstream IP/port uyumsuzluğu (`10.10.10.105` vs `.106`/`.120`), Cloudflare Tunnel kopması veya backend uyuyor | NPM/NPMplus container logu, `cloudflared` servis durumu, proxy üzerinden `curl -Iv http://<backend-ip>:<port>` |
| **`CERT_HAS_EXPIRED` / `UNABLE_TO_VERIFY_LEAF_SIGNATURE` / `SSL_ERROR`** | Let's Encrypt yenileme hatası, Cloudflare SSL modu uyumsuzluğu (`Flexible` vs `Full Strict`), yanlış saat (NTP) | `openssl s_client -connect <host>:443 -servername <host> < /dev/null 2>/dev/null \| openssl x509 -noout -dates -issuer -subject` |
| **İç Ağdan Açılmıyor, Dışarıdan Açılıyor (veya tersi)** | Split DNS / Host Override eksikliği veya NAT Reflection (Hairpin NAT) sorunu | İçeriden `dig +short <domain>` (dış IP mi iç IP mi dönüyor?); Unbound Host Override kontrolü |
| **Git / Docker / Paket Yöneticisi Zaman Aşımı** | Yerel proxy ortam değişkeni (`HTTP_PROXY`), MTU/PPPoE parçalanması (MSS clamping), IPv6 fallback veya AdGuard engeli | `env \| grep -i proxy`, `curl -4 -Iv <url>` vs `curl -6 -Iv <url>`, `ping -M do -s 1464 <hedef>` |

---

## 🔄 3. Zorunlu 6 Adımlı Arıza Giderme Döngüsü

Bir ağ/servis arızası bildirildiğinde şu 6 adımı sırayla uygula:

1. **Topla (Collect):** Tam hata mesajını, başarısız komutu/URL'yi, istemcinin hangi VLAN/ağda olduğunu (LAN, Wi-Fi, Mobil 4G/5G, VPN) ve son yapılan değişikliği netleştir.
2. **Sınıflandır (Classify):** Yukarıdaki matrise göre hatayı tek bir ana kategoriye ayır (`DNS`, `L2/VLAN`, `Firewall/CrowdSec`, `Proxy/502`, `SSL/TLS`, `Cloudflare Tunnel`, `Backend`).
3. **Teşhis Et (Diagnose):** En az sayıda, salt-okunur komutla trafik zincirini ortadan bölerek (binary search: önce backend → sonra NPM/NPMplus → sonra OPNsense/AdGuard → sonra Cloudflare) arızalı halkayı yakala.
4. **Açıkla (Explain):** Çözüm önermeden önce **çıktının ne anlama geldiğini ve kesin kök nedeni** 2-3 cümlede açıkla.
5. **Öner (Advise):** Geri alınabilir çözüm seçeneklerini sun (ör. kural silmek yerine önce `Disable`, servis değiştirmeden önce yedek/snapshot). Onay sonrası uygula.
6. **Doğrula (Verify):** İlk başarısız olan komutu/isteği tekrar çalıştırarak (`curl -Iv`, `nslookup`, `Live View`, Uptime Kuma) sorunun kalıcı olarak çözüldüğünü kanıtla.

---

## 🔥 4. OPNsense (`VM 101`) Canlı Salt-Okunur Teşhis & MVC API Kalıpları
*(danielrosehill/Opnsense-Mgmt-Plugin, richardnixon25 ve lucamarien salt-okunur desenlerinden uyarlanmıştır)*

Sorun OPNsense katmanında izole edildiğinde, konfigürasyon değiştirmeden önce yalnızca **salt-okunur** SSH veya OPNsense 26.7+ MVC REST API kontrolleri uygula:

1. **PF State, Kural ve Paket Akışı (SSH Salt-Okunur):**
   - Aktif bağlantı tablosu: `pfctl -ss | grep <hedef-ip>`
   - Canlı blok logları: `tcpdump -n -e -ttt -i pflog0 host <hedef-ip>`
   - Arayüz & VLAN/ARP/DHCP durumu: `ifconfig`, `arp -an`, `netstat -rn`, `wg show` (WireGuard peer handshake ve trafik sayacı), `pluginctl -s` (servis durumu).
2. **CrowdSec & Unbound Hızlı Kontrol:**
   - Yanlış pozitif IP banı: `cscli decisions list`, `cscli alerts list -l 10`
   - Unbound servis/çözümleme: `drill @127.0.0.1 <domain>` veya Web GUI `Services -> Unbound DNS -> Reporting`.
3. **OPNsense 26.7+ MVC Salt-Okunur REST API (Gelecekteki MCP / Otomasyon Hazırlığı):**
   - Her zaman **sadece okuma yetkili** özel bir API kullanıcısı (`System -> Access -> Users`) ile HTTP `GET` uç noktalarını kullan; anahtarları düz metin loglama:
     - Gateway durumu: `GET /api/routes/gateway/status`
     - Firewall canlı log/alias: `GET /api/diagnostics/firewall/log`, `GET /api/firewall/alias/searchItem`
     - Unbound / WireGuard / Arayüzler: `GET /api/unbound/service/status`, `GET /api/wireguard/service/show`, `GET /api/diagnostics/interface/getArp`
   - *Kural:* İleride canlı OPNsense MCP sunucusu (`lucamarien/opnsense-mcp-server` vb.) bağlandığında da varsayılan mod kesin **Read-Only** kalır; yazma/kural değişikliği öncesi daima **FAZ 0 Proxmox Snapshot** alınır.

---

## 📋 5. Standart Teşhis Raporu Formatı

1. **Belirti & Sınıf:** Hata kodu + etkilenen trafik zinciri halkası.
2. **Salt-Okunur Tanı Adımları:** Kopyalanıp çalıştırılacak hedefli kontrol komutları.
3. **Kök Neden Analizi:** Çıktılara dayalı kesin teşhis.
4. **Geri Alınabilir Çözüm & Doğrulama:** Uygulanacak düzeltme + başarı doğrulama testi.
