---
title: "GölgeSiber Dijital Ekosistem Mimari & Orkestrasyon Haritası"
version: "1.0.0"
last_updated: "2026-11-27T12:32:00+03:00"
status: "PRODUCTION_ACTIVE"
maintainer: "GölgeSiber SecOps & Prodüksiyon Masası"
sync_rule: "Her servis, port, konteyner veya API değişikliğinde bu dosya güncellenir."
---

# 🗺️ GölgeSiber Dijital Ekosistem Mimari & Orkestrasyon Haritası

> **Son Güncelleme:** `2026-11-27T12:32:00+03:00`  
> **Durum:** Canlı Üretim Ortamı (Active Production)  
> **Kapsam:** GölgeSiber Veri Merkezi (Proxmox VE), Dalaman Airport Suites (STR & Bot), GölgeKitabevi (WooCommerce)

---

## 1. 🌐 Genel Ekosistem Üst Düzey Ağ Topolojisi

```mermaid
flowchart TD
    subgraph WAN["🌍 Genel İnternet & Müşteriler"]
        Visitors["Ziyaretçiler / Müşteriler"]
        Guests["Otel Misafirleri (WhatsApp)"]
        Shoppers["Kitap Alıcıları (WooCommerce)"]
    end

    subgraph Cloudflare["🛡️ Cloudflare Edge & Zero Trust"]
        CF_DNS["Cloudflare DNS / Proxy"]
        CF_WAF["WAF & Bot Fight Mode"]
        CF_Tunnel["Cloudflare Zero Trust Tunnel"]
    end

    subgraph Perimeter["🏰 Ağ Sınırı & Güvenlik Duvarı"]
        OPN["OPNsense Firewall (VM 101)"]
        AdGuard["AdGuard Home (CT 106) - DNS/DoH"]
        NPM["NPMplus Reverse Proxy (CT 106)"]
        CrowdSec["CrowdSec LAPI & Bouncer"]
    end

    subgraph Proxmox["🖥️ Proxmox VE (pvenew) Altyapısı"]
        subgraph GroupGS["🛡️ GölgeSiber Katmanı"]
            GS_Web["golgesiber.com (Next.js 16)"]
            GS_Dash["GölgeSiber Dashboard (CT 104)"]
            Matomo["Matomo Analytics (CT 114)"]
            Uptime["Uptime Kuma (CT 110)"]
            NOC_Bot["@d8el_bot NOC Alerting"]
        end

        subgraph GroupDAS["🏨 Dalaman Airport Suites Katmanı"]
            DAS_Web["dalamanairportsuites.com"]
            WA_Bot["booking-whatsapp-bot (CT 116 - FastAPI/Baileys)"]
            STR_Kasa["STR Kasa & Muhasebe Motoru"]
            UniFi["UniFi OS Server (CT 107) - 5651 Hotspot"]
        end

        subgraph GroupGK["📚 GölgeKitabevi Katmanı"]
            GK_Web["golgekitabevi.com (WooCommerce / HPOS)"]
            PHP_FPM["PHP 8.4-FPM + Redis Cache"]
            CustomPlugins["golge-watermark & golge-isbn"]
            MariaDB[("MariaDB / InnoDB")]
        end
    end

    subgraph StorageBackup["💾 Depolama & Yedekleme"]
        ZFS["ZFS Mirror SSD Pool (TBW Korumalı)"]
        PBS["Proxmox Backup Server (VM 102)"]
        Nextcloud["Nextcloud (VM 103 - nc.golgesiber.com)"]
    end

    Visitors --> CF_DNS
    Guests --> CF_DNS
    Shoppers --> CF_DNS
    CF_DNS --> CF_WAF
    CF_WAF -->|CF-Connecting-IP| OPN
    OPN --> NPM
    AdGuard -.->|DNS Cozümleme| NPM
    CrowdSec -.->|Tehdit Engelleme| NPM

    NPM -->|HTTPS:3000| GS_Web
    NPM -->|HTTPS:3001| GS_Dash
    NPM -->|HTTPS:8080| Matomo
    NPM -->|HTTPS:3002| Uptime
    
    NPM -->|HTTPS:443| DAS_Web
    NPM -->|Webhook / API| WA_Bot
    NPM -->|HTTPS:8443| UniFi

    NPM -->|HTTPS:443| GK_Web
    GK_Web --> PHP_FPM
    PHP_FPM --> CustomPlugins
    PHP_FPM --> MariaDB

    Proxmox -.->|Günlük Snapshot| PBS
    Proxmox -.->|Veri Senkronu| Nextcloud
    Proxmox -.->|Depolama| ZFS
```

---

## 2. 🛡️ `golgesiber.com` Derin Mimari Haritası

```mermaid
sequenceDiagram
    autonumber
    actor User as 👤 Ziyaretçi / Güvenlik Araştırmacısı
    participant CF as 🛡️ Cloudflare WAF
    participant NPM as 🔀 NPMplus (CT 106)
    participant NextJS as ⚡ Next.js 16 (App Router)
    participant Matomo as 📊 Matomo (CT 114)
    participant Kuma as ⏱️ Uptime Kuma (CT 110)
    participant TG as 🤖 @d8el_bot (Telegram NOC)

    User->>CF: HTTPS İsteği (golgesiber.com)
    CF->>CF: WAF, DDoS Kontrolü & SSL Şifre Çözme
    CF->>NPM: CF-Connecting-IP ile Forward
    NPM->>NextJS: Reverse Proxy iletimi (Port 3000)
    NextJS-->>User: Server-Side Rendered (SSR) HTML + Tailwind
    NextJS->>Matomo: JS İzleme / Cookieless KVKK Analitik (Async)
    
    loop Her 60 Saniye
        Kuma->>NextJS: HTTP 200 Healthcheck Sorgusu
        alt Yanıt Yok veya HTTP 5xx
            Kuma->>TG: Acil Bildirim: "golgesiber.com DOWN!"
        end
    end
```

---

## 3. 🏨 `dalamanairportsuites.com` Rezervasyon, Misafir & Kasa Akışı

```mermaid
flowchart LR
    subgraph Channels["📲 Kanallar & Misafir"]
        Site["dalamanairportsuites.com"]
        OTA["Airbnb / Booking.com"]
        GuestWA["Misafir WhatsApp"]
    end

    subgraph BotEngine["🤖 Rezervasyon & İletişim Motoru (CT 116)"]
        FastAPI["FastAPI Webhook Handler"]
        Baileys["Baileys Socket (Mode A)"]
        MetaAPI["Meta Cloud API (Mode B)"]
        RouterMesaj Yönlendirici
    end

    subgraph Property["🏡 Daire 11 (Sirius Rezidans)"]
        Keybox["7/24 Şifreli Keybox"]
        WiFi["UniFi U6-Pro (CT 107 - 5651 Log)"]
        AC["Klima / Elektrik"]
    end

    subgraph Accounting["💰 Kasa & Muhasebe Motoru"]
        KasaLedger["Nakit / Banka Girişi"]
        TaxEngine["KDV (%10/%20) + Konaklama Vergisi (%2)"]
        ProfitSplit["Ortak Kar Dağıtımı (%50 - %50)"]
    end

    Site -->|Rezervasyon Talebi| FastAPI
    OTA -->|Rezervasyon Senkronu| FastAPI
    GuestWA <--> Baileys
    Baileys <--> Router
    MetaAPI <--> Router
    Router <--> FastAPI

    FastAPI -->|Giriş Kodu & Yol Tarifi| GuestWA
    FastAPI -->|Şifre Üretimi| Keybox
    FastAPI -->|Wi-Fi Şifresi| WiFi
    FastAPI -->|Gelir Kaydı| KasaLedger

    KasaLedger --> TaxEngine
    TaxEngine --> ProfitSplit
```

---

## 4. 📚 `golgekitabevi.com` WooCommerce & Sahaf Entegrasyon Haritası

```mermaid
flowchart TD
    subgraph Front["🌐 E-Ticaret & Pazaryeri"]
        Customer["Müşteri / Kitapsever"]
        Sahaf["Sahafburada / Nadirkitap"]
    end

    subgraph WP_Layer["🛒 WordPress & WooCommerce Çekirdeği"]
        WP["WordPress 6.7+ (PHP 8.4-FPM)"]
        HPOS["HPOS (High-Performance Order Storage)"]
        RedisCache[("Redis Object Cache")]
        
        subgraph CustomExt["🧩 Özel Gölge Eklentileri"]
            Watermark["golge-watermark (Görsel Koruma)"]
            ISBN["golge-isbn (Barkod & Otomatik Meta Çekici)"]
        end
    end

    subgraph DB_Storage["💾 Veritabanı & Dosya Sistemi"]
        MySQL[("MariaDB (InnoDB Tabloları)")]
        Media["wp-content/uploads (Kitap Fotoğrafları)"]
        WPCLI["WP-CLI Otomasyonu (www-data)"]
    end

    Customer -->|Sipariş / Ödeme| WP
    Sahaf <-->|Stok / Sipariş API| WP
    WP --> HPOS
    HPOS --> MySQL
    WP <--> RedisCache

    ISBN -->|Barkod Sorgusu| WP
    WP -->|Görsel Yükleme| Watermark
    Watermark --> Media
    WPCLI -->|Toplu Fiyat/Stok Güncelleme| MySQL
```
