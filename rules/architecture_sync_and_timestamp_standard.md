# 📐 Architecture Synchronization & Timestamp Standard

Bu kural, GölgeSiber altyapısı veya bağlı projelerde (`golgesiber.com`, `dalamanairportsuites.com`, `golgekitabevi.com`) herhangi bir altyapı değişikliği yapıldığında zorunludur.

## 🎯 Zorunlu Güncelleme Tetikleyicileri
Bir yapay zeka ajanı aşağıdaki değişikliklerden herhangi birini gerçekleştirdiğinde:
1. **Yeni Servis/Konteyner Eklendiğinde/Silindiğinde:** Proxmox LXC (CT), Docker servisi veya sanal makine (VM).
2. **Ağ & Port Değişikliklerinde:** NPMplus reverse proxy yönlendirmeleri, OPNsense NAT/VLAN kuralları, AdGuard yönlendirmeleri.
3. **Veritabanı / Kasa / Ödeme Akışlarında:** Yeni tablo, Stripe/PayTR/Iyzico veya STR Kasa payı kuralı eklendiğinde.
4. **Harici API Entegrasyonlarında:** Baileys, Meta Cloud API, OTA (Airbnb/Booking) veya Sahafburada bağlantıları değiştiğinde.

## 📝 Yapılması Gerekenler
1. `ARCHITECTURE.md` dosyasındaki ilgili Mermaid diyagramını güncelle.
2. `last_updated` alanına güncel ISO-8601 zaman damgasını koy (Örn: `2026-11-27T12:32:00+03:00`).
3. Dosyayı hem yerel depolara hem de Nextcloud Collectives altına senkronize et.
4. Değişikliği `docs(arch): update architecture topology and timestamp` mesajıyla GitHub'a commit edip pushla.
