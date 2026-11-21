---
name: telegram-bot-alerting-ops
description: >-
  Telegram bot engineering, NOC alerting, and interactive command operations for @your_noc_alert_bot
  (pve-interactive-bot.py, telegram-send.sh, ZED/OOM/CPU/SSH/CrowdSec watchers) and Dalaman
  staff alerts. Use when building/hardening Python/Bash Telegram bots, inline approvals, or
  alert cooldowns. Do NOT use for WhatsApp/Meta Cloud API bots (use whatsapp-bot-gateway-ops),
  Proxmox ZFS/PBS lifecycle (use proxmox-ve-ops), or live 502 debugging (use
  homelab-network-troubleshoot).
---

# 🤖 Telegram Bot Mühendisliği & NOC Alarm Operasyon Becerisi

Bu beceri; **nyxandro/telegram-bot-development-skill**, **serejaris/telegram-skills** (ham HTTP Bot API) ve **howardpen9** kalıplarını **GölgeSiber Veri Merkezi (`@your_noc_alert_bot` + 7 nöbetçi betik)** ve **Dalaman Suites iç operasyon ekibi bildirimleri** için birleştirir.

> **Kapsam Sınırı:** Bu beceri **Telegram Bot API geliştirme (Python/Bash ham HTTP), iki yönlü komuta güvenliği, alarm yorgunluğunu önleme ve bildirim hatları** içindir. WhatsApp/Meta Cloud API için `whatsapp-bot-gateway-ops`, Proxmox/ZFS/PBS operasyonları için `proxmox-ve-ops`, canlı ağ arızası için `homelab-network-troubleshoot` kullanılır.

---

## 🔒 0. Gizlilik ve Komuta Güvenliği (Sıfır Yetkisiz Erişim)

1. **Token & Chat ID Hijyeni:** BotFather HTTP API Token'ı ve gerçek `CHAT_ID` değerleri asla blog taslaklarına, markdown dosyalarına veya git depolarına düz metin yazılmaz; yalnızca `chmod 600` izinli ortam dosyalarından (`/etc/golgesiber/telegram.env` vb.) okunur.
2. **Sıkı `ALLOWED_CHAT_IDS` Kuralı:** `pve-interactive-bot.py` gibi sunucu komutu çalıştıran her bot, gelen her `update` için ilk satırda `effective_chat.id` ve `effective_user.id` değerlerini sabit izin listesiyle doğrular; yetkisiz çağrıları sessizce reddedip loglar.
3. **Yıkıcı Komutlarda Zorunlu Inline Onay:** `/shutdown <ID>`, `/reboot <ID>` veya servis yeniden başlatma komutları tek mesajla hemen çalışmaz; **`InlineKeyboardMarkup` (`✅ Onayla` / `❌ İptal` — 30 sn süreli)** onay kapısından geçer.
4. **Shell Injection Yasağı:** Telegram'dan gelen `<ID>` parametresi asla `os.system(f"qm start {arg}")` ile çalıştırılmaz; mutlaka `re.fullmatch(r"\d{3,4}", arg)` doğrulaması + `subprocess.run(["qm", "start", vmid], shell=False, timeout=30)` kullanılır.

---

## ⚡ 1. Hafif Ham HTTP Bildirim Standardı (`telegram-send.sh` / Cron / Hook)
*(serejaris/telegram-skills framework-less HTTP deseninden uyarlanmıştır)*

`pvenew` üzerindeki nöbetçiler (`daily-health-check.sh`, `zed-telegram.sh`, `pve-oom-watcher.sh`, `vzdump-hook-telegram.sh`, `telegram-ssh-login.sh`, `check-cpu-temp.sh`, `crowdsec-daily-report.sh`) için ağır kütüphane kurmadan şu standartları zorunlu uygula:

1. **Bloklama Koruması (`--max-time`):** Her `curl` çağrısında `--connect-timeout 5 --max-time 10` kullan; Telegram API yavaşlasa veya internet kopsa bile `vzdump` ya da `cron` işi asla askıda kalmaz.
2. **`Markdown` Yerine `HTML` Parse Mode:** Eski `parse_mode=Markdown` sunucu adlarındaki alt çizgi (`HDD_Havuz`, `pve_backup`) yüzünden sessizce `HTTP 400` verir. Daima **`parse_mode=HTML`** kullan ve dinamik çıktılarda `<`, `>`, `&` karakterlerini escape et (`html.escape()`).
3. **4096 Karakter Sınırı & Tekil Mesaj:** Uzun çıktılar (`zpool status`, log özeti) `4000` karakterde bölünmeli veya dosya (`sendDocument`) olarak gönderilmelidir.

```bash
# Güvenli ham HTTP gönderim kalıbı (token ortam dosyasından gelir)
curl -fsS --connect-timeout 5 --max-time 10 \
  -X POST "https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage" \
  -d "chat_id=${TG_CHAT_ID}" \
  -d "parse_mode=HTML" \
  -d "disable_web_page_preview=true" \
  --data-urlencode "text=${MESSAGE}" >/dev/null
```

---

## 🐍 2. İki Yönlü Komuta Botu Mimarisi (`pve-interactive-bot.py`)
*(nyxandro/telegram-bot-development-skill & howardpen9 kurallarından uyarlanmıştır)*

1. **Long Polling vs Webhook Seçimi:**
   - `pvenew` iç ağında dışarıya port açmamak için **Long Polling** (outbound HTTPS — Cloudflare/OPNsense port açma gerektirmez!) tercih edilir.
   - Public webhook kullanılacaksa mutlaka `secret_token` (`X-Telegram-Bot-Api-Secret-Token` başlığı) doğrulanır.
2. **Canlı Durum Güncelleme (Edit-in-Place):** Uzun süren komutlarda (`/saglik`, `/start 102`) önce *"⏳ İşleniyor..."* gönder, sonuç gelince `editMessageText` ile aynı mesajı güncelle (sohbet kirliliği önlenir).
3. **`systemd` Dayanıklılığı:** `Restart=on-failure`, `RestartSec=10s`, `MemoryMax=128M`, `CPUQuota=25%` + ağ geçici koptuğunda exponential backoff.
4. **Rate-Limit Kuralları:** Telegram bireysel sohbette ~1 msg/sn, gruplarda 20 msg/dk sınırı uygular; `429 Too Many Requests` dönünce yanıttaki `retry_after` süresi kadar bekle.

---

## 🔔 3. Alert Yorgunluğunu Önleme & NOC / Dalaman Entegrasyonu

1. **Önem Derecesi Etiketleri & Cooldown:**
   - `🔴 KRİTİK` (ZED disk düşmesi, OOM-Killer, CPU ≥ 75°C, `vzdump` hatası): Anında gönder + aynı alarm için **15–30 dk cooldown** (`/tmp/tg_cooldown_<key>`) koy ki dakikada 10 spam atmasın.
   - `🟡 BİLGİ / ÖZET` (Sabah 08:30 sağlık brifingi, Akşam 21:00 CrowdSec raporu): Sessiz bildirim (`disable_notification=true`) opsiyonu kullan.
2. **Uptime Kuma Uyku Penceresi Uyumu:** `VM 102 (PBS)` ve `CT 100 (OnlyOffice)` planlı uyku saatlerinde yanlış alarm üretilmemesi için hem Uptime Kuma bakım penceresi hem de özel script'ler aynı takvime sadık kalır.
3. **Dalaman Suites İç Operasyon Köprüsü (WhatsApp Mod B Uyumu):** Resmi Meta WhatsApp Cloud API gruplara mesaj atmadığı için temizlik/erken giriş/Cold Brew ekip bildirimleri ayrı bir Telegram operasyon grubuna (`chat_id` negatif `-100...`) gönderilir ve `whatsapp-bot-gateway-ops` ile koordine edilir.

---

## 📋 4. Standart Mühendislik Çıktı Formatı

1. **Bot Rolü & Güvenlik Kontrolü:** Salt bildirim (raw HTTP) vs iki yönlü komuta (`ALLOWED_CHAT_IDS`, inline onay, `shell=False`).
2. **Uygulanabilir Kod / Betik:** `HTML` parse mode, timeout, cooldown ve ortam değişkenli temiz betik veya Python modülü.
3. **Test & `systemd` Doğrulama:** Dry-run mesaj testi, `journalctl -u <servis>` ve hata/rate-limit kontrolü.
