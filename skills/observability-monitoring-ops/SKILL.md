---
name: observability-monitoring-ops
description: >-
  Observability, Uptime Kuma (CT 110) monitors & sleep maintenance windows, GoAccess
  (10.10.10.120:91), AdGuard telemetry, Grafana/Prometheus/Loki dashboards, TBW log budgets, and
  blameless incident postmortems (RCA). Use when designing monitors, SLOs, PromQL/LogQL, or
  postmortems. Do NOT use for Telegram bot code (use telegram-bot-alerting-ops), live outage
  debugging (use homelab-network-troubleshoot), or Matomo marketing metrics (use
  matomo-analytics-ops).
---

# 📡 Gözlemlenebilirlik, İzleme Panelleri, Metrik & Postmortem Becerisi

Bu beceri; **prometheus/prometheus-mcp** yerleşik runbook'ları, resmi **grafana/mcp-grafana** desenleri ve SRE gözlemlenebilirlik standartlarını **GölgeSiber NOC (`CT 110 Uptime Kuma`, `GoAccess`, `AdGuard`, `Proxmox/ZFS` metrikleri)** mimarisine uyarlar.

> **Kapsam Sınırı:** Bu beceri **izleme kapsamı, Uptime Kuma bakım pencereleri, Grafana/Prometheus metrik-dashboard tasarımı, log saklama/TBW bütçesi ve olay sonrası analiz (Postmortem/RCA)** içindir. Telegram bot/script kodu için `telegram-bot-alerting-ops`, canlı arıza teşhisi için `homelab-network-troubleshoot`, web trafik/SEO analitiği için `matomo-analytics-ops` kullanılır.

---

## 🔒 0. Gizlilik, Alarm Hijyeni ve TBW Kuralları

1. **Sır Maskeleme:** Uptime Kuma API anahtarları, Grafana/Prometheus Bearer token'ları, `/metrics` Basic Auth parolaları ve dış IP logları asla düz metin paylaşılmaz (`[MASKED]`).
2. **SSD TBW & 32 GB RAM Bilinçli Telemetri (`pvenew`):**
   - Prometheus/Loki veya yeni izleme ajanı eklerken **`scrape_interval` (min `30s`–`60s`)** ve **retention (`15d`–`30d`)** sınırlarını dar tut; gereksiz yüksek kardinaliteli metriklerin `HDD_Havuz` SSD ömrünü tüketmesine izin verme.
   - Yeni izleme servisi açmadan önce 32 GB RAM bütçesinde kalıcı yer olduğunu doğrula (`proxmox-ve-ops`).

---

## 🧭 1. GölgeSiber 4 Katmanlı Telemetri Envanteri

1. **Uptime Kuma (`CT 110` — `10.10.10.110:3001`, VLAN 10 MGMT):**
   - OPNsense `seq=2841` istisna kuralı ile tüm iç VLAN'ları (`IC_AGLAR`) denetler.
   - **Zorunlu Bakım Pencereleri (Yanlış Alarm Kalkanı):**
     - `PBS Gece Uykusu`: `19:15 – 09:55` (`VM 102`)
     - `OnlyOffice Gece Uykusu`: `00:00 – 08:30` (`CT 100`)
   - **Kritik İzleme Kapsamı:** Dış web siteleri (HTTP 200 + **SSL 14 gün kala uyarı**), `Nextcloud`, `NPM/NPMplus`, `OPNsense Gateway`, `PBS`, `AdGuard DNS Port 53` ve `booking-whatsapp-bot` `/health` ucu.
2. **NPMplus GoAccess (`https://10.10.10.120:91`):** Gerçek zamanlı HTTP 4xx/5xx sıçramaları, bot taramaları ve bant genişliği anomalileri.
3. **AdGuard Home (`CT 109` — `10.40.40.109`):** DNS gecikmesi, engelleme oranı ve iç ağda anormal sorgu atan (compromised/noisy) istemci tespiti.
4. **Proxmox / ZFS / Host Nöbetçileri:** `daily-health-check.sh`, `ZED`, `OOM-Killer`, `CPU >= 75°C`, `CrowdSec 21:00`.

---

## 📈 2. Metrik, PromQL & Grafana Dashboard Tasarım Standartları
*(Resmi `grafana/mcp-grafana` & `prometheus/prometheus-mcp` kurallarından uyarlanmıştır)*

1. **Altın Sinyaller (USE + RED):**
   - **Altyapı (USE):** CPU/Load, RAM + OOM baskısı, **ZFS ARC & SSD Wearout/Sıcaklık**, Disk Doluluk (>%80 uyarı, >%90 kritik), Ağ paket düşmesi.
   - **Web / API Servisleri (RED):** İstek hızı (**R**ate), HTTP 5xx/4xx hata oranı (**E**rrors), p95 yanıt gecikmesi (**D**uration).
2. **Uptime Kuma → Prometheus Köprüsü:** Uptime Kuma'nın yerleşik `/metrics` ucu (API key korumalı) Prometheus tarafından çekilerek Grafana'da tek bir *"GölgeSiber Cyberpunk NOC"* panelinde birleştirilebilir.
3. **Alert Yorgunluğu Önleme (Actionable-Only Kuralı):**
   - Bir alarm aksiyon gerektirmiyorsa **alarm değil, dashboard grafiğidir.**
   - Her alarmda mutlaka `for:` bekleme süresi (örn. `for: 3m` — anlık 10 saniyelik mikro dalgalanmayı susturur) ve **Runbook linki** bulunur.
   - Bildirim iletim kuralları ve cooldown politikası `telegram-bot-alerting-ops` ile hizalanır.

---

## 📝 3. Olay Sonrası Analiz (Blameless Postmortem / RCA) Şablonu

Gerçek bir kesinti, disk arızası (örn. `SSD_Havuz` yanması) veya servis çökmesi çözüldükten sonra kalıcı kurumsal hafıza için şu 5 maddelik kısa RCA çıkarılır:
1. **Özet & Etki:** Hangi servis/VLAN etkilendi, başlangıç–bitiş süresi (MTTR) ne kadar?
2. **Zaman Çizelgesi:** İlk alarm anı → teşhis → müdahale → doğrulama.
3. **Kök Neden (5 Whys):** Yüzeydeki belirti değil, altta yatan gerçek sebep.
4. **Ne İyi Çalıştı / Nerede Kör Nokta Vardı?** (Hangi alarm erken uyardı, hangisi eksikti?)
5. **Kalıcı Önleyici Aksiyonlar:** Yeni Uptime Kuma monitörü, bakım penceresi, limit veya otomasyon görevi.

---

## 📋 4. Standart Gözlemlenebilirlik Çıktı Formatı

1. **Kapsam & Kör Nokta Tespiti:** Hangi servis/metrik izleniyor, hangisi eksik veya gürültülü?
2. **Konfigürasyon / Sorgu:** Uptime Kuma monitör/bakım penceresi ayarı, PromQL/LogQL sorgusu veya `journalctl` analiz komutu.
3. **Doğrulama & TBW Etkisi:** Test alarmı, yanlış pozitif kontrolü ve RAM/disk yazım etkisi özeti.
