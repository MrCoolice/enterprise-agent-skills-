# 🎮 Agent Commands & Prompt Trigger Cheat Sheet (Komut ve İstek Sözlüğü)

This document provides exact, copy-pasteable prompt triggers and command syntax for all **32 Enterprise Agent Skills** across different AI Agent platforms (**Google Antigravity**, **Claude Code**, **Cursor / Windsurf**).

---

## 🛠️ How to Trigger Skills by AI Agent Platform

### 1. Google Antigravity
* **Automatic Routing:** Antigravity automatically detects user intent from your prompt and loads the relevant skill.
* **Explicit Calling:** To guarantee a specific skill runs, include the skill name in your prompt:
  * *"Use `opnsense-proxmox-secops` to audit my firewall."*
  * *"Follow `proxmox-ve-ops` rules to inspect my ZFS pool."*
* **Location:** `$HOME/.gemini/config/skills/<skill-name>/SKILL.md`

### 2. Claude Code (Anthropic CLI)
* **Natural Language:** Claude Code reads local skills or guidelines from `CLAUDE.md`.
* **Explicit Slash Reference:**
  * Mention the skill explicitly: *"Read `skills/code-security-audit/SKILL.md` and audit `src/api/auth.ts`."*
* **Location:** `~/.claude/` or workspace `skills/`

### 3. Cursor & Windsurf
* **@ Rules Reference:** Type `@` in the chat window to reference the specific skill:
  * `@opnsense-proxmox-secops Audit this XML file`
  * `@web-quality-modern-guidance Optimize this Next.js page`
* **Location:** `.cursor/rules/<skill-name>.mdc` or workspace `.cursorrules`

---

## 📋 Complete 32 Skills Trigger Prompt Matrix

| Skill Name | 🇹🇷 Türkçe İstek / Komut Örneği | 🇬🇧 English Trigger Command / Prompt | 🇩🇪 Deutscher Befehl / Prompt-Beispiel |
| :--- | :--- | :--- | :--- |
| **`opnsense-proxmox-secops`** | `opnsense-proxmox-secops: paylaştığım config.xml dosyasını 7 katmanlı güvenlik, VLAN ve CARP denetiminden geçir.` | `opnsense-proxmox-secops: audit my config.xml for 7-layer security, VLAN segmentation, and WireGuard hardening.` | `opnsense-proxmox-secops: führe ein 7-Schichten Sicherheits- und VLAN-Audit für meine config.xml durch.` |
| **`proxmox-ve-ops`** | `proxmox-ve-ops: Proxmox ZFS havuzunu ve SSD TBW aşınma durumunu analiz et, PBS tekilleştirilmiş yedekleme planı çıkar.` | `proxmox-ve-ops: analyze my Proxmox ZFS pool health, SSD TBW endurance, and audit PBS backup schedule.` | `proxmox-ve-ops: analysiere den ZFS-Pool, die SSD TBW-Abnutzung und auditiere den PBS-Backup-Zeitplan.` |
| **`cloudflare-edge-proxy-secops`** | `cloudflare-edge-proxy-secops: Cloudflare Zero Trust tünelimi ve NPMplus WAF kurallarımı dış saldırılara karşı sıkılaştır.` | `cloudflare-edge-proxy-secops: inspect and harden my Cloudflare Zero Trust tunnel and NPMplus WAF rules.` | `cloudflare-edge-proxy-secops: prüfe und härte meinen Cloudflare Zero Trust Tunnel und NPMplus WAF-Regeln.` |
| **`homelab-network-troubleshoot`** | `homelab-network-troubleshoot: canlı 502 Bad Gateway / DNS kesintisini istemciden hipervizöre 6 adımda teşhis et.` | `homelab-network-troubleshoot: diagnose live 502 Bad Gateway or DNS failure using the 6-step protocol.` | `homelab-network-troubleshoot: diagnostiziere 502 Bad Gateway- oder DNS-Ausfälle mit dem 6-stufigen Protokoll.` |
| **`unifi-wifi-hotspot-ops`** | `unifi-wifi-hotspot-ops: AP'lerin RF kanal ve dolaşım ayarlarını optimize et, 5651 misafir portalını denetle.` | `unifi-wifi-hotspot-ops: optimize AP RF channels, roaming tuning, and audit captive guest portal setup.` | `unifi-wifi-hotspot-ops: optimiere AP RF-Kanäle, Roaming und auditiere das Gäste-Captive-Portal.` |
| **`docker-linux-deploy-ops`** | `docker-linux-deploy-ops: bu compose.yaml dosyasını Debian 13 LXC için güvenli hale getir ve systemd servisine dönüştür.` | `docker-linux-deploy-ops: harden this compose.yaml for Debian 13 LXC, sandbox resources, and generate systemd unit.` | `docker-linux-deploy-ops: härte diese compose.yaml für Debian 13 LXC und generiere einen systemd-Dienst.` |
| **`observability-monitoring-ops`** | `observability-monitoring-ops: Uptime Kuma için servis izleme planı hazırla ve kesinti için kök neden analizi (RCA) çıkar.` | `observability-monitoring-ops: design Uptime Kuma monitors, GoAccess telemetry, and write an incident RCA report.` | `observability-monitoring-ops: erstelle Uptime Kuma Monitore und verfasse einen Root-Cause-Analysis (RCA) Bericht.` |
| **`nextcloud-selfhosted-ops`** | `nextcloud-selfhosted-ops: Nextcloud occ bakım komutlarını çalıştır, Redis ve PHP önbellek parametrelerini optimize et.` | `nextcloud-selfhosted-ops: run Nextcloud occ maintenance routines, tune Redis/APCu caching, and repair file locks.` | `nextcloud-selfhosted-ops: führe Nextcloud occ Wartungsroutinen aus und optimiere Redis/APCu Caching.` |
| **`code-security-audit`** | `code-security-audit: bu API rotasında ve veritabanı sorgularında 6 fazlı zaafiyet ve güvenlik açığı avı yap.` | `code-security-audit: conduct a 6-phase adversarial vulnerability hunt on this API route and ORM queries.` | `code-security-audit: führe eine 6-Phasen-Schwachstellenanalyse für diesen API-Endpunkt und ORM-Queries durch.` |
| **`web-quality-modern-guidance`** | `web-quality-modern-guidance: bu özellik için önce 1 sayfalık SPEC.md şartnamesi çıkar, ardından Next.js 16 sayfasını Core Web Vitals (LCP, INP, CLS) ve Lighthouse 95+ için optimize et.` | `web-quality-modern-guidance: produce a 1-page SPEC.md (SDD) first, then optimize this Next.js 16 page for Core Web Vitals and Lighthouse 95+.` | `web-quality-modern-guidance: erstelle zuerst eine 1-seitige SPEC.md (SDD) Spezifikation und optimiere dann diese Next.js 16 Seite für Core Web Vitals.` |
| **`frontend-design`** | `frontend-design: modern, özgün ve erişilebilir (a11y) bir dashboard bileşeni tasarla ve tasarım tokenlerini tanımla.` | `frontend-design: design a distinctive, accessible dashboard component with consistent design tokens.` | `frontend-design: entwirf eine moderne, barrierefreie Dashboard-Komponente mit sauberen Design-Tokens.` |
| **`editorial-web-design-studio`** | `editorial-web-design-studio: UI/UX Pro Max kurallarıyla referans web sitesinin computed CSS tasarım DNA'sını çıkar ve dokunsal mikro-etkileşimleri kur.` | `editorial-web-design-studio: reverse-engineer computed CSS design DNA using UI/UX Pro Max rules and tactile micro-interactions.` | `editorial-web-design-studio: extrahiere die computed CSS Design-DNA mit UI/UX Pro Max Regeln und erstelle taktile Interaktionen.` |
| **`editorial-architecture-diagrams`** | `editorial-architecture-diagrams: OPNsense ve Proxmox ağ topolojisi için yayın kalitesinde SVG mimari şeması üret.` | `editorial-architecture-diagrams: generate a publication-grade SVG architecture topology for OPNsense & Proxmox.` | `editorial-architecture-diagrams: erstelle ein druckreifes SVG-Architekturdiagramm für OPNsense & Proxmox.` |
| **`technical-book-publishing`** | `technical-book-publishing: bu teknik bölümü 10 Altın Kurala göre denetle ve B5 baskı/EPUB formatına uyarla.` | `technical-book-publishing: review this chapter against the 10 Golden Laws and prepare B5 print/EPUB typesetting.` | `technical-book-publishing: prüfe dieses Kapitel nach den 10 Goldenen Regeln und formatiere für B5 Druck/EPUB.` |
| **`telegram-bot-alerting-ops`** | `telegram-bot-alerting-ops: kritik ZFS bozulması ve OOM çökmesi alarmları için interaktif onay butonlu Telegram botu oluştur.` | `telegram-bot-alerting-ops: build a hardened Telegram NOC bot for ZFS pool alerts and OOM panic with inline approvals.` | `telegram-bot-alerting-ops: erstelle einen Telegram NOC-Bot für ZFS- und OOM-Alarme mit interaktiven Genehmigungen.` |
| **`whatsapp-bot-gateway-ops`** | `whatsapp-bot-gateway-ops: FastAPI ve Baileys/Meta Cloud API ile çalışan çift modlu WhatsApp gateway mimarisini yapılandır.` | `whatsapp-bot-gateway-ops: configure dual-mode WhatsApp gateway with Baileys engine, Meta Cloud API, and HMAC webhooks.` | `whatsapp-bot-gateway-ops: konfiguriere das Dual-Mode WhatsApp Gateway mit Baileys und Meta Cloud API.` |
| **`wordpress-woocommerce-ops`** | `wordpress-woocommerce-ops: güvenli www-data WP-CLI komutlarıyla HPOS veritabanı geçişini ve önbellek temizliğini yap.` | `wordpress-woocommerce-ops: perform safe www-data WP-CLI operations, tune HPOS, and harden custom plugins.` | `wordpress-woocommerce-ops: führe sichere WP-CLI Befehle aus, optimiere HPOS und härte eigene Plugins.` |
| **`audiophile-music-curator`** | `audiophile-music-curator: müzik kütüphanemi tara, 500x500 kapakları ve sözleri göm, Opel Corsa USB belleğime ayna senkronizasyonu yap.` | `audiophile-music-curator: audit music library, embed 500x500 APIC covers & LRCLIB lyrics, and mirror sync to automotive USB.` | `audiophile-music-curator: auditiere die Musikbibliothek, binde 500x500 Cover und Texte ein und synchronisiere auf den Auto-USB-Stick.` |
| **`matomo-analytics-ops`** | `matomo-analytics-ops: Matomo Reporting API üzerinden en çok ziyaret edilen sayfaları listele ve KVKK gizlilik denetimi yap.` | `matomo-analytics-ops: query Matomo Reporting API for top landing pages and audit tracking for GDPR compliance.` | `matomo-analytics-ops: frage die Matomo Reporting API ab und auditiere das Tracking auf DSGVO-Konformität.` |
| **`video-director-engine`** | `video-director-engine: bu senaryo için Remotion kodlu bir video bileşeni ve -14 LUFS ses miksajı hazırla.` | `video-director-engine: script a programmatic Remotion video component with kinetic typography and audio normalization.` | `video-director-engine: erstelle eine programmatische Remotion-Videokomponente mit Audio-Normalisierung.` |
| **`native-pptx-presentations`** | `native-pptx-presentations: bu Markdown dokümanını kurumsal şablonlu, düzenlenebilir PowerPoint (.pptx) slaytına dönüştür.` | `native-pptx-presentations: convert this Markdown spec into a native editable PowerPoint (.pptx) workshop deck.` | `native-pptx-presentations: wandle dieses Markdown-Dokument in native, editierbare PowerPoint (.pptx) Folien um.` |
| **`quiz-word-game-master`** | `quiz-word-game-master: 2D HTML5 Canvas üzerinde çalışan, Web Audio efektli ve durum makineli bir kelime oyunu oluştur.` | `quiz-word-game-master: build a responsive 2D HTML5 Canvas word puzzle game with state machine and Web Audio FX.` | `quiz-word-game-master: erstelle ein responsives HTML5 Canvas Wortspiel mit Zustandsautomat und Web Audio FX.` |
| **`seo-content-master`** | `seo-content-master: bu konu hakkında Wikidata varlıkları ve PAS kopyalama modeliyle 100/100 RankMath uyumlu SEO makalesi yaz.` | `seo-content-master: generate an entity-backed SEO article with PAS copy framework and produce llms.txt.` | `seo-content-master: verfasse einen datengestützten SEO-Artikel mit PAS-Framework und generiere llms.txt.` |
| **`social-media-growth`** | `social-media-growth: bu blog yazısını 60/25/15 ritmiyle Instagram, LinkedIn ve YouTube için çoklu ajan sosyal postlarına dönüştür.` | `social-media-growth: repurpose this article into LinkedIn, Instagram, and YouTube posts using the 60/25/15 rhythm.` | `social-media-growth: erstelle LinkedIn-, Instagram- und YouTube-Beiträge im 60/25/15 Rhythmus aus diesem Artikel.` |
| **`founder-gtm-growth-council`** | `founder-gtm-growth-council: yeni SaaS fikrimi 4 rollü icra kurulu bakış açısıyla eleştir ve MVP kapsamını belirle.` | `founder-gtm-growth-council: stress-test my new product idea with the 4-role executive board and scope the MVP.` | `founder-gtm-growth-council: validiere meine Produktidee mit dem 4-Rollen-Vorstand und definiere das MVP.` |
| **`str-revenue-listing-master`** | `str-revenue-listing-master: Airbnb ve Booking.com komisyon paritesini hesapla ve rakip gecelik fiyat kıyaslaması yap.` | `str-revenue-listing-master: benchmark competitor nightly rates, calculate OTA commission parity, and optimize listing copy.` | `str-revenue-listing-master: analysiere Mitbewerber-Übernachtungspreise und berechne OTA-Provisionsparität.` |
| **`steam-library-assistant`** | `steam-library-assistant: Steam kütüphanemi analiz et, en çok oynanan oyunları listele ve diskler arası oyun taşıma betiği oluştur.` | `steam-library-assistant: analyze my Steam library stats, find co-op matches, and generate a local disk transfer script.` | `steam-library-assistant: analysiere meine Steam-Bibliothek und generiere ein Skript für den lokalen Spieletransfer.` |

---

## 🎨 Creative & GameDev High-Impact Prompts (Jiro, Reelfolio, 60fps, Inspora)

| Goal / Amaç | 🇹🇷 Örnek İstek / Komut | 🇬🇧 Example Prompt |
| :--- | :--- | :--- |
| **Quiz Soru Üretimi (Mod A: Anti-Bias)** | `quiz-word-game-master: Siber güvenlik kategorisi için şık uzunlukları eşit, 12 soruluk (4 ve 8 mini-boss, 12 final-boss) anti-bias quiz seti üret.` | `quiz-word-game-master: generate a 12-question anti-bias cybersecurity quiz set with equal option lengths and boss pacing.` |
| **Kelime Seviye Üretimi (Mod B: Anagram)** | `quiz-word-game-master: TDK sözlüğüyle uyumlu 6 harfli bir kelime anagram seviyesi üret, hedef ve bonus kelimeleri listele.` | `quiz-word-game-master: create a 6-letter word anagram level with target and hidden bonus words matching the official dictionary.` |
| **Otonom QA Testi (Mod C: Playtester)** | `quiz-word-game-master: audit-quiz-balance ve audit-wordgame testlerini çalıştır, zorluk uçurumlarını ve şık biaslarını denetle.` | `quiz-word-game-master: run automated balance and regression audits to detect difficulty spikes, length bias, and encoding issues.` |
| **Viral Story Kartı (Mod D: Retention)** | `quiz-word-game-master: oyuncunun CyberRank unvanını ve skorunu gösteren 1080x1920 dikey Instagram Story kartı ve emoji ızgarası tasarla.` | `quiz-word-game-master: design a 1080x1920 vertical Instagram Story share card with CyberRank tier badge and score breakdown.` |
| **60 FPS Akıcı Oyun Hissi (`60fps.design`)** | `quiz-word-game-master: 60fps.design standartlarında yaylanma fiziği (spring), kart çevirme ve haptik titreşimli bir kelime oyunu karosu hazırla.` | `quiz-word-game-master: build a 60fps.design inspired word puzzle tile with spring physics, 3D flip, and haptic shake feedback.` |
| **Modern AI Section Mimarisi (`jiro.build` & `inspora.design`)** | `editorial-web-design-studio: jiro.build ve inspora.design ilhamıyla anti-AI-slop koyu mod asimetrik Bento grid ve cam efektli kart yapısı üret.` | `editorial-web-design-studio: generate an anti-AI-slop dark-mode asymmetrical Bento Grid section inspired by jiro.build and inspora.design.` |
| **Animasyonlu Ürün Showreel (`reelfolio.io`)** | `video-director-engine: reelfolio.io tarzında bu ürün ekran görüntüsünü 3D cihaz mockup'ı içinde akıcı kayan bir Remotion lansman videosuna çevir.` | `video-director-engine: convert this static UI screenshot into a reelfolio.io style 3D animated device showreel using Remotion.` |

---

📖 **Detailed Architectural Guide:** [https://golgesiber.com/yazi/yapay-zeka-ajanlari-ile-sistem-yonetimi](https://golgesiber.com/yazi/yapay-zeka-ajanlari-ile-sistem-yonetimi)
