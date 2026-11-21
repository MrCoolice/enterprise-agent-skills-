# 🚀 Enterprise Agent Skills

A modular collection of **26 production-grade agent skills** for **Google Antigravity**, **Claude Code**, **Cursor**, and autonomous AI coding agents.

This repository packages real-world, battle-tested system rules and automation playbooks spanning **Enterprise SecOps, Homelab Infrastructure, Web Engineering, NOC Monitoring, Publishing, and Growth Engineering**.

---

## 📥 How to Install in Antigravity (Nasıl Kurulur / Wie man installiert)

### Option 1: Global Installation (Tüm Projeler İçin Genel Kurulum)
Skills placed in the global Antigravity configuration directory become available across all conversations and workspaces.

**Windows (PowerShell):**
```powershell
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git
Copy-Item -Recurse -Force .\enterprise-agent-skills-\skills\* "$HOME\.gemini\config\skills\"
```

**Linux / macOS (Bash):**
```bash
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git
mkdir -p ~/.gemini/config/skills
cp -r enterprise-agent-skills-/skills/* ~/.gemini/config/skills/
```

### Option 2: Project-Level Installation (Proje Bazlı Kurulum)
If you only want specific skills inside a dedicated workspace:
```bash
# Copy desired skill folder into your project's .agent/skills/ or .gemini/skills/
cp -r skills/opnsense-proxmox-secops /path/to/your/project/.agent/skills/
```

---

## 📋 Comprehensive Skills Directory / Beceri Dizini / Fähigkeiten-Katalog

| Skill Name | 🇹🇷 Türkçe Açıklama | 🇬🇧 English Description | 🇩🇪 Deutsche Beschreibung |
| :--- | :--- | :--- | :--- |
| **`opnsense-proxmox-secops`** | OPNsense 7 katmanlı statik güvenlik denetimi, VLAN/DMZ segmentasyonu ve WireGuard sıkılaştırma. | 7-layer static security audits for OPNsense, VLAN/DMZ segmentation, and WireGuard hardening. | 7-Schichten OPNsense Sicherheitsaudit, VLAN/DMZ-Segmentierung und WireGuard-Härtung. |
| **`proxmox-ve-ops`** | Proxmox VE VM/LXC yaşam döngüsü, ZFS depolama havuzları, SSD TBW koruması ve PBS tekilleştirilmiş yedekleme. | Proxmox VE VM/LXC lifecycle, ZFS pool protection, SSD TBW budgets, and PBS deduplicated backups. | Proxmox VE VM/LXC Lifecycle, ZFS-Speicherpools, SSD TBW Schutz und PBS Backup-Deduplizierung. |
| **`cloudflare-edge-proxy-secops`** | Cloudflare WAF kuralları, Zero Trust tünelleri (cloudflared), NPMplus ters proxy ve CrowdSec entegrasyonu. | Cloudflare Edge WAF rules, Zero Trust tunnels (cloudflared), NPMplus proxy hosts, and CrowdSec. | Cloudflare Edge WAF, Zero Trust Tunnel (cloudflared), NPMplus Reverse-Proxy und CrowdSec. |
| **`homelab-network-troubleshoot`** | Canlı ağ, DNS, 502/504 servis kesintileri ve UniFi/VLAN trafiği için 6 adımlı canlı teşhis. | 6-step live network & service diagnostics across VLANs, DNS, OPNsense, and reverse proxies. | 6-stufige Live-Netzwerk- und Dienstdiagnose für VLANs, DNS, OPNsense und Reverse-Proxies. |
| **`unifi-wifi-hotspot-ops`** | UniFi Controller AP yönetimi, RF kanal ve dolaşım optimizasyonu, 5651 uyumlu misafir portalı. | UniFi OS Server AP management, RF channel and roaming tuning, and captive guest portal engineering. | UniFi OS AP-Verwaltung, RF-Kanal- und Roaming-Optimierung und Gäste-Captive-Portal. |
| **`docker-linux-deploy-ops`** | Debian 13 LXC/VM Docker Compose sıkılaştırma, systemd servisleri ve sıfır kesintili dağıtım. | Docker Compose hardening on Debian LXC/VM, systemd unit generation, and zero-downtime deploys. | Docker Compose Härtung auf Debian LXC/VM, systemd-Dienste und Zero-Downtime-Deployment. |
| **`observability-monitoring-ops`** | Uptime Kuma izleme, GoAccess gerçek zamanlı log analitiği, Grafana/Prometheus ve postmortem (RCA). | Uptime Kuma monitors, GoAccess real-time log analytics, Grafana/Prometheus, and blameless postmortems. | Uptime Kuma Monitoring, GoAccess Log-Analytik, Grafana/Prometheus und Postmortem-Analysen. |
| **`nextcloud-selfhosted-ops`** | Nextcloud `occ` bakım komutları, PHP/Redis/APCu optimizasyonu ve OnlyOffice entegrasyonu. | Self-hosted Nextcloud occ maintenance, PHP/Redis/APCu caching tuning, and OnlyOffice integration. | Nextcloud occ Wartungsbefehle, PHP/Redis/APCu Performance-Tuning und OnlyOffice Integration. |
| **`code-security-audit`** | Next.js, FastAPI, PHP ve Python kod tabanları için 6 fazlı kaynak kod zaafiyet avcılığı. | Adversarial 6-phase source-code security audit and vulnerability hunting across fullstack apps. | 6-Phasen Quellcode-Sicherheitsaudit und Schwachstellensuche für Fullstack-Anwendungen. |
| **`web-quality-modern-guidance`** | Next.js 16, React 19, Prisma, Tailwind, Core Web Vitals (LCP/INP/CLS) ve Lighthouse 95+ optimizasyonu. | Modern web engineering, Core Web Vitals optimization, Next.js 16, React 19, and Lighthouse 95+. | Moderne Webentwicklung, Core Web Vitals Optimierung, Next.js 16, React 19 und Lighthouse 95+. |
| **`frontend-design`** | Üst düzey kullanıcı arayüzü tasarımı, tasarım tokenleri, erişilebilirlik ve UX denetimleri. | Distinctive, production-grade frontend design ideation, design-tokens, and accessibility audits. | Hochwertiges Frontend-Design, Design-Tokens, Barrierefreiheit und umfassende UX-Audits. |
| **`editorial-web-design-studio`** | Anti-AI-slop sanat yönetimi, mikro ses efektleri (Web Audio), animasyonlar ve marka tasarımı. | Anti-AI-slop art direction, DESIGN.md systems, Web Audio micro-sounds, and interaction design. | Anti-AI-Slop Art Direction, DESIGN.md Systeme, Web Audio Mikro-Sounds und Interaktionsdesign. |
| **`editorial-architecture-diagrams`** | Yayın kalitesinde ağ mimarisi şemaları, baskıya hazır SVG/PNG figürleri ve HTML topolojileri. | Publication-grade technical architecture diagrams, print-ready SVG/PNG figures, and HTML topologies. | Publikationsreife Architekturdiagramme, druckfertige SVG/PNG-Grafiken und interaktive Topologien. |
| **`technical-book-publishing`** | Teknik kitap yazarlığı, 10 Altın Kural denetimi ve B5 formatında baskı/PDF dizgisi (Pandoc/Typst). | Technical book authoring, editorial review laws, and B5 print/PDF/EPUB typesetting. | Technische Bucherstellung, redaktionelle Qualitätsprüfung und B5 Druck/PDF/EPUB Schriftsatz. |
| **`native-pptx-presentations`** | Kod ile tam düzenlenebilir yerel PowerPoint (.pptx) slaytları ve eğitim setleri üretimi. | Native editable PowerPoint (.pptx) slide deck studio using python-pptx and shape automation. | Native editierbare PowerPoint (.pptx) Folien-Generierung mit python-pptx und Formen-Automatisierung. |
| **`video-director-engine`** | Remotion ve FFmpeg ile kod tabanlı dikey video, Reels ve ses mastering (-14 LUFS). | Code-rendered video, Reels, talking-head editing, Remotion engine, and FFmpeg audio mastering. | Code-gerendertes Video, Reels, Talking-Head Schnitt, Remotion Engine und FFmpeg Audio-Mastering. |
| **`telegram-bot-alerting-ops`** | Telegram NOC alarm botları, interaktif onay komutları ve CPU/OOM/ZED izleyicileri. | Telegram bot engineering, NOC alerting, interactive approval commands, and CPU/OOM/ZED watchers. | Telegram NOC Alerting-Bots, interaktive Genehmigungsbefehle und CPU/OOM/ZED Überwachung. |
| **`whatsapp-bot-gateway-ops`** | Çift modlu WhatsApp bot mimarisi (Baileys ve Meta Cloud API geçiş adaptörü). | Dual-mode WhatsApp bot gateway engineering (Baileys adapter and Meta Cloud API integration). | Dual-Modus WhatsApp Bot Gateway Architektur (Baileys Adapter und Meta Cloud API Integration). |
| **`wordpress-woocommerce-ops`** | Güvenli www-data WP-CLI yönetimi, WooCommerce HPOS, PHP 8.4 ve özel eklenti denetimi. | Safe www-data WP-CLI operations, WooCommerce HPOS, PHP 8.4-FPM, and custom plugin security. | Sichere www-data WP-CLI Wartung, WooCommerce HPOS, PHP 8.4-FPM und Plugin-Sicherheitsprüfungen. |
| **`matomo-analytics-ops`** | Kendi barındırdığın Matomo analitiği, Reporting API sorguları ve KVKK/DSGVO gizlilik denetimi. | Self-hosted Matomo analytics Reporting API queries, JS tracking, and privacy governance audits. | Self-hosted Matomo Reporting API Abfragen, JS-Tracking und DSGVO/KVKK Datenschutz-Audits. |
| **`quiz-word-game-master`** | Trivia, kelime bulmacaları ve 2D HTML5 Canvas web arcade oyunları mühendisliği. | Web and mobile game engineering for Trivia, Word Games, and 2D HTML5 Canvas arcade games. | Web- und Mobil-Gaming für Trivia, Worträtsel und 2D HTML5 Canvas Arcade-Spiele. |
| **`seo-content-master`** | Otonom SEO/GEO içerik motoru, Wikidata varlıkları, PAS/BAB metinleri ve llms.txt üretimi. | Autonomous SEO/GEO content and audit engine, Wikidata entities, and llms.txt generation. | Autonome SEO/GEO Content-Engine, Wikidata Entitäten, PAS/BAB Copywriting und llms.txt Erstellung. |
| **`social-media-growth`** | Instagram, LinkedIn ve YouTube için çoklu ajan sosyal medya ve büyüme fabrikası. | Multi-agent social media growth factory for Instagram, LinkedIn, and YouTube (60/25/15 rhythm). | Multi-Agenten Social Media Wachstumsfabrik für Instagram, LinkedIn und YouTube (60/25/15 Rhythmus). |
| **`founder-gtm-growth-council`** | Fikir doğrulama, MVP kapsam belirleme, değer tabanlı fiyatlandırma ve GTM lansman stratejisi. | Solo-founder idea validation, MVP scoping, value pricing psychology, and GTM launch roadmaps. | Ideenvalidierung für Solo-Gründer, MVP-Scoping, wertbasierte Preisgestaltung und GTM-Launch. |
| **`str-revenue-listing-master`** | Kısa dönem kiralama gelir yönetimi, rakip gecelik fiyat kıyaslama ve OTA komisyon paritesi. | Short-term rental revenue management, competitor rate benchmarking, and OTA parity. | Kurzzeitmiete-Ertragsmanagement, Mitbewerber-Preisanalyse und OTA-Provisionsparität. |
| **`steam-library-assistant`** | Steam kütüphane analizi, oynama istatistikleri ve yerel sürücüler arası oyun taşıma otomasyonu. | Steam library analysis, playtime statistics, co-op matching, and local disk transfer workflows. | Steam-Bibliotheksanalyse, Spielzeit-Statistiken, Co-Op-Matching und Festplatten-Spieletransfer. |

---


---

## 🔌 Recommended Companion Plugins (Önerilen Tamamlayıcı Eklentiler)

While all 26 skills are 100% self-contained and run out of the box, pairing them with the following official Antigravity plugins unlocks advanced visual reverse-engineering and design capabilities:

### 1. Chrome DevTools (`antigravity-plugins-official/plugin/chrome-devtools-plugin`)
* **Synergy With:** `editorial-web-design-studio`, `frontend-design`, `web-quality-modern-guidance`.
* **What it does:** Allows the agent to open live websites via headless Chrome, extract exact computed CSS design tokens (colors, typography, spacing hierarchies), and run automated performance audits.

### 2. Mobbin (`antigravity-plugins-partners/plugin/mobbin`)
* **Synergy With:** `editorial-web-design-studio`, `frontend-design`.
* **What it does:** Grants the agent access to 600,000+ real-world production UI screens (Stripe, Linear, Airbnb) via the Mobbin MCP server, preventing generic AI design patterns and benchmarking against top industry UX.

---
## 🔒 Privacy & Sanitization Guarantee
This repository has been strictly sanitized:
- **No private IP addresses:** Subnets use standard RFC 1918 templates (`10.10.10.x`, `192.168.1.x`).
- **No private domains:** Replaced with standardized `.example.com` placeholders.
- **No secrets, tokens, or credentials:** All sensitive API keys and bots have been decoupled.

## 📄 License
Released under the [MIT License](LICENSE).
