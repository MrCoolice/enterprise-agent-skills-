# 🚀 Enterprise Agent Skills

<p align="center">
  <b>Production-grade, modular Agent Skills for Google Antigravity, Claude Code, Cursor, and AI Coding Agents.</b><br>
  <i>Enterprise SecOps • Proxmox & OPNsense Infrastructure • Modern Web Engineering • Autonomous NOC</i>
</p>

<p align="center">
  <a href="#-english">🇬🇧 English</a> •
  <a href="#-deutsch">🇩🇪 Deutsch</a> •
  <a href="#-türkçe">🇹🇷 Türkçe</a>
</p>

---

<p align="center">
  📖 <b>Comprehensive Deep-Dive Guide / Detaylı Mimari Rehber / Ausführlicher Architektur-Leitfaden:</b><br>
  👉 <a href="https://golgesiber.com/yazi/yapay-zeka-ajanlari-ile-sistem-yonetimi"><b>https://golgesiber.com/yazi/yapay-zeka-ajanlari-ile-sistem-yonetimi</b></a>
</p>

---

## 🇬🇧 English

### 1. What is this repository? (WHAT)
**Enterprise Agent Skills** is an open-source, modular collection of **26 battle-tested agent skills** engineered for autonomous AI agents (**Google Antigravity**, **Claude Code**, **Cursor**, and CLI-based LLMs). 

Instead of dumping massive, monolithic prompts into your AI chats, an **Agent Skill** is a structured, on-demand operational playbook (`SKILL.md`). It provides the AI agent with domain-specific knowledge, exact command execution recipes, safety boundaries, and validation checklists only when the specific task is triggered.

This repository covers 6 core operational pillars:
1. **Perimeter SecOps & Networking:** OPNsense 7-layer audits, Cloudflare Zero Trust / WAF, UniFi Wi-Fi, network troubleshooting.
2. **Virtualization & Storage:** Proxmox VE 8, ZFS pools, SSD TBW protection, Proxmox Backup Server (PBS) deduplication.
3. **Application Layer & Containers:** Hardened Docker Compose, systemd sandboxing, Nextcloud occ lifecycle.
4. **Autonomous NOC & Alerting:** Uptime Kuma monitoring, GoAccess log analytics, Telegram interactive NOC bots.
5. **Code & Web Engineering:** 6-phase source code vulnerability audits, Next.js 16 / React 19 / Core Web Vitals optimization.
6. **Publishing & Growth:** Editorial technical architecture diagrams, B5 book typesetting, SEO/llms.txt engines.

### 2. Why use Agent Skills? (WHY)
When using standard LLM prompts for mission-critical infrastructure, three major failure points occur:
* **Context Window Pollution:** Pasting 2,000 lines of firewall rules and Linux guidelines exhausts the model's token budget and degrades reasoning performance.
* **Hallucinations & Risk of Destruction:** A generic AI might propose destructive commands (e.g. `rm -rf`, uncontrolled firewall restarts, or breaking ZFS pools) without checking state.
* **Lack of Repeatable Standards:** Every engineer receives slightly different outputs depending on how they frame their prompt.

**How Agent Skills solve this:**
* 🎯 **Dynamic Skill Discovery:** The agent loads *only* the relevant skill when needed (e.g. calling `opnsense-proxmox-secops` only when inspecting firewall files).
* 🛡️ **Read-Only-First Guardrails:** Skills enforce strict pre-flight safety checks (e.g. static XML analysis before any real change, least-privilege credentials).
* ⚡ **CLI-First & Zero-Dependency:** 90% of these skills require no third-party plugins or complex setups—they leverage native CLI tools (`pvesh`, `qm`, `docker`, `curl`, `git`, `python`).

### 3. How to install and use? (HOW)

#### Global Installation (Recommended for Antigravity & Claude Code)
Installs skills globally so they are available across all your workspaces and conversations:

**Windows (PowerShell):**
```powershell
# Clone the repository
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git

# Copy skills to your Antigravity global configuration
Copy-Item -Recurse -Force .\enterprise-agent-skills-\skills\* "$HOME\.gemini\config\skills\"
```

**Linux / macOS (Bash):**
```bash
# Clone the repository
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git

# Copy skills to global configuration
mkdir -p ~/.gemini/config/skills
cp -r enterprise-agent-skills-/skills/* ~/.gemini/config/skills/
```

#### Option B: Single Skill Download (Download Only What You Need)
If you only want one specific skill (e.g. `opnsense-proxmox-secops`), you don't need to clone the entire repo:

**Windows (PowerShell):**
```powershell
$skill = "opnsense-proxmox-secops"
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills\$skill"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -OutFile "$HOME\.gemini\config\skills\$skill\SKILL.md"
```

**Linux / macOS (curl):**
```bash
skill="opnsense-proxmox-secops"
mkdir -p ~/.gemini/config/skills/$skill
curl -sSL "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -o ~/.gemini/config/skills/$skill/SKILL.md
```

**Or using `degit` (Easiest for npm users):**
```bash
npx degit MrCoolice/enterprise-agent-skills-/skills/opnsense-proxmox-secops ~/.gemini/config/skills/opnsense-proxmox-secops
```

#### How to Trigger in Chat
Once installed, your agent automatically detects and triggers the skills based on user intent. You can also invoke them directly:
* *"Audit my OPNsense config.xml using opnsense-proxmox-secops rules."*
* *"Optimize my Proxmox VE ZFS pool and check SSD TBW endurance using proxmox-ve-ops."*
* *"Perform a 6-phase adversarial code security audit on this API route."*

---

## 🇩🇪 Deutsch

### 1. Was ist dieses Repository? (WAS)
**Enterprise Agent Skills** ist eine quelloffene, modulare Sammlung von **26 praxiserprobten Agent-Fähigkeiten (Skills)**, entwickelt für autonome KI-Coding-Agenten (**Google Antigravity**, **Claude Code**, **Cursor** und LLM-Terminals).

Anstatt riesige, unübersichtliche System-Prompts in den KI-Kontext zu laden, ist ein **Agent Skill** ein strukturiertes, bedarfsgesteuertes Playbook (`SKILL.md`). Es versorgt den KI-Agenten genau dann mit Fachwissen, Befehlsfolgen, Sicherheitsregeln und Checklisten, wenn die jeweilige Aufgabe anfällt.

Das Repository umfasst 6 zentrale Domänen:
1. **Perimeter SecOps & Netzwerke:** 7-Schichten OPNsense Audits, Cloudflare Zero Trust / WAF, UniFi WLAN, 6-stufige Netzwerkanalyse.
2. **Virtualisierung & Storage:** Proxmox VE 8, ZFS-Speicherpools, SSD TBW Schutz, Proxmox Backup Server (PBS) Deduplizierung.
3. **Container & Applikationen:** Gehärtetes Docker Compose auf Debian 13 LXC, systemd-Dienste, Nextcloud occ Wartung.
4. **Autonomes NOC & Monitoring:** Uptime Kuma Überwachung, GoAccess Echtzeit-Logs, Telegram NOC-Bots mit Genehmigungs-Workflow.
5. **Code & Web Engineering:** 6-Phasen Quellcode-Schwachstellenjagd, Next.js 16 / React 19 / Core Web Vitals (Lighthouse 95+).
6. **Publikation & Business:** Technische Architekturdiagramme, B5-Buchsatz, autonome SEO/GEO Content-Engine.

### 2. Warum Agent Skills einsetzen? (WARUM)
Bei der Verwaltung kritischer IT-Infrastrukturen stoßen gewöhnliche KI-Prompts schnell an ihre Grenzen:
* **Überfüllter Kontext:** Das ständige Kopieren von Richtlinien verbraucht wertvolle Tokens und verringert die logische Schärfe des Modells.
* **Halluzinationen & Ausfallrisiken:** Eine ungesicherte KI schlägt womöglich riskante Befehle vor (z. B. ungetestete Neustarts, Überschreiben von Firewall-Regeln).
* **Mangelnde Reproduzierbarkeit:** Ohne feste Standards weichen die Ergebnisse bei jeder Anfrage voneinander ab.

**Die Lösung durch Agent Skills:**
* 🎯 **Modulare Aktivierung:** Der Agent liest nur das Regelwerk, das für das aktuelle Problem relevant ist.
* 🛡️ **Read-Only-First Sicherheitsprinzip:** Zuerst wird der Zustand passiv analysiert (z. B. statische XML-Prüfung), bevor Aktionen vorgeschlagen werden.
* ⚡ **CLI-First & Null-Abhängigkeiten:** 90 % aller Skills laufen direkt mit Standard-CLI-Tools (`pvesh`, `qm`, `docker`, `curl`, `git`, `python`) ohne Zusatzsoftware.

### 3. Wie wird es installiert und genutzt? (WIE)

#### Globale Installation (Antigravity & Claude Code)

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

#### Option B: Einzelne Fähigkeit herunterladen (Nur das Nötigste)
Wenn Sie nur eine bestimmte Fähigkeit (z. B. `opnsense-proxmox-secops`) benötigen, müssen Sie nicht das gesamte Repository klonen:

**Windows (PowerShell):**
```powershell
$skill = "opnsense-proxmox-secops"
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills\$skill"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -OutFile "$HOME\.gemini\config\skills\$skill\SKILL.md"
```

**Linux / macOS (curl):**
```bash
skill="opnsense-proxmox-secops"
mkdir -p ~/.gemini/config/skills/$skill
curl -sSL "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -o ~/.gemini/config/skills/$skill/SKILL.md
```

**Oder mit `degit` (Für Node.js-Entwickler):**
```bash
npx degit MrCoolice/enterprise-agent-skills-/skills/opnsense-proxmox-secops ~/.gemini/config/skills/opnsense-proxmox-secops
```

#### Beispiel-Befehle im Chat:
* *"Prüfe meine OPNsense config.xml nach den Regeln von opnsense-proxmox-secops."*
* *"Optimiere mein Proxmox VE ZFS-Setup und prüfe das SSD TBW-Budget mit proxmox-ve-ops."*
* *"Führe ein 6-stufiges Sicherheitsaudit für diesen Next.js API-Endpunkt durch."*

---

## 🇹🇷 Türkçe

### 1. Bu Depo Nedir? (NE)
**Enterprise Agent Skills**, otonom yapay zeka ajanları (**Google Antigravity**, **Claude Code**, **Cursor**) ve komut satırı LLM sistemleri için geliştirilmiş, kurumsal düzeyde **26 modüler ajanik beceri (Agent Skill)** içeren açık kaynaklı bir kütüphanedir.

Yapay zekaya her seferinde yüzlerce satırlık genel kural metinleri (prompt) yapıştırmak yerine, **Agent Skill** mimarisi ajana sadece ihtiyaç anında çağrılan yapılandırılmış bir işletim rehberi (`SKILL.md`) sunar.

Depodaki beceriler 6 ana operasyonel katmanı kapsar:
1. **Çevre Güvenliği ve Ağ (SecOps):** OPNsense 7 katmanlı statik denetim, Cloudflare Zero Trust / WAF, UniFi Wi-Fi, canlı kesinti teşhisi.
2. **Sanallaştırma ve Depolama:** Proxmox VE 8 yönetimi, ZFS havuzları, SSD TBW bütçe koruması, PBS tekilleştirilmiş yedekleme.
3. **Uygulama ve Konteyner:** Debian 13 LXC üzerinde sıkılaştırılmış Docker Compose, systemd servisleri, Nextcloud occ operasyonları.
4. **Otonom NOC ve Alarm:** Uptime Kuma izleme, GoAccess canlı log analitiği, Telegram altyapı botları ve yetkili onay mekanizması.
5. **Kod Güvenliği ve Web Mühendisliği:** 6 aşamalı kaynak kod zaafiyet avcılığı, Next.js 16, React 19, Core Web Vitals (Lighthouse 95+).
6. **Yayıncılık ve Büyüme:** Yayın kalitesinde mimari diyagramlar (SVG/HTML), B5 kitap dizgisi, otonom SEO ve llms.txt motoru.

### 2. Neden Agent Skill Kullanmalısınız? (NİÇİN)
Kritik sunucu ve ağ altyapılarını sıradan sohbet pencereleri üzerinden yönetmeye çalışmak üç temel risk doğurur:
* **Bağlam Kirliliği (Context Bloat):** Bütün kuralları tek bir sohbete yüklemek yapay zekanın dikkat penceresini daraltır ve mantıksal hatalara yol açar.
* **Halüsinasyon ve Kesinti Riski:** Kural sınırları çizilmemiş bir model, sunucuda telafisi güç yıkıcı komutlar önerebilir veya servisleri aniden durdurabilir.
* **Standart Eksikliği:** Her komut isteminde farklı ve öngörülemeyen çıktılar üretilir.

**Agent Skill Mimarisi Bunu Nasıl Çözer:**
* 🎯 **Dinamik Yükleme:** Ajan yalnızca ilgili görevi yürüteceği zaman o beceriyi bağlamına alır.
* 🛡️ **Salt-Okunur Güvenlik Önceliği (Read-Only-First):** Herhangi bir değişiklik yapılmadan önce durum pasif olarak doğrulanır (örneğin OPNsense için önce statik XML analizi).
* ⚡ **Sıfır Bağımlılık (CLI-First):** Becerilerin %90'ı ek eklenti gerektirmeden doğrudan sistem araçlarıyla (`pvesh`, `qm`, `docker`, `curl`, `git`, `python`) çalışır.

### 3. Nasıl Kurulur ve Kullanılır? (NASIL)

#### Genel Kurulum (Antigravity & Claude Code İçin Önerilen)
Becerileri tüm projelerinizde ve sohbetlerinizde kullanılabilir hale getirmek için genel dizine kopyalayın:

**Windows (PowerShell):**
```powershell
# Depoyu klonlayın
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git

# Becerileri Antigravity yapılandırma dizinine aktarın
Copy-Item -Recurse -Force .\enterprise-agent-skills-\skills\* "$HOME\.gemini\config\skills\"
```

**Linux / macOS (Bash):**
```bash
# Depoyu klonlayın
git clone https://github.com/MrCoolice/enterprise-agent-skills-.git

# Becerileri yapılandırma dizinine aktarın
mkdir -p ~/.gemini/config/skills
cp -r enterprise-agent-skills-/skills/* ~/.gemini/config/skills/
```

#### Seçenek B: Tekil Beceri İndirme (Sadece İhtiyacınız Olanı Alın)
Tüm repoyu klonlamak yerine sadece tek bir beceriyi (örneğin `opnsense-proxmox-secops`) kullanmak isterseniz:

**Windows (PowerShell):**
```powershell
$skill = "opnsense-proxmox-secops"
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills\$skill"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -OutFile "$HOME\.gemini\config\skills\$skill\SKILL.md"
```

**Linux / macOS (curl):**
```bash
skill="opnsense-proxmox-secops"
mkdir -p ~/.gemini/config/skills/$skill
curl -sSL "https://raw.githubusercontent.com/MrCoolice/enterprise-agent-skills-/main/skills/$skill/SKILL.md" -o ~/.gemini/config/skills/$skill/SKILL.md
```

**Veya `degit` ile (Tek Komutla Klasör Çekme):**
```bash
npx degit MrCoolice/enterprise-agent-skills-/skills/opnsense-proxmox-secops ~/.gemini/config/skills/opnsense-proxmox-secops
```

#### Sohbette Nasıl Kullanılır?
Kurulum tamamlandıktan sonra ajana doğrudan görevinizi söylemeniz yeterlidir:
* *"opnsense-proxmox-secops becerisini kullanarak paylaştığım config.xml dosyasını 7 katmanlı denetle."*
* *"proxmox-ve-ops kurallarına göre ZFS depolama havuzunun SSD TBW sağlığını analiz et."*
* *"Bu API endpointi üzerinde code-security-audit kurallarıyla 6 fazlı zaafiyet taraması yap."*

---

## 📋 26 Skills Directory / Beceri Dizini / Fähigkeiten-Katalog

| Skill Name | 🇬🇧 English Description | 🇩🇪 Deutsche Beschreibung | 🇹🇷 Türkçe Açıklama |
| :--- | :--- | :--- | :--- |
| **`opnsense-proxmox-secops`** | 7-layer static security audits for OPNsense, VLAN/DMZ segmentation, and WireGuard hardening. | 7-Schichten OPNsense Sicherheitsaudit, VLAN/DMZ-Segmentierung und WireGuard-Härtung. | OPNsense 7 katmanlı statik güvenlik denetimi, VLAN/DMZ segmentasyonu ve WireGuard sıkılaştırma. |
| **`proxmox-ve-ops`** | Proxmox VE VM/LXC lifecycle, ZFS pool protection, SSD TBW budgets, and PBS deduplicated backups. | Proxmox VE VM/LXC Lifecycle, ZFS-Speicherpools, SSD TBW Schutz und PBS Backup-Deduplizierung. | Proxmox VE VM/LXC yaşam döngüsü, ZFS depolama havuzları, SSD TBW koruması ve PBS tekilleştirilmiş yedekleme. |
| **`cloudflare-edge-proxy-secops`** | Cloudflare Edge WAF rules, Zero Trust tunnels (cloudflared), NPMplus proxy hosts, and CrowdSec. | Cloudflare Edge WAF, Zero Trust Tunnel (cloudflared), NPMplus Reverse-Proxy und CrowdSec. | Cloudflare WAF kuralları, Zero Trust tünelleri (cloudflared), NPMplus ters proxy ve CrowdSec entegrasyonu. |
| **`homelab-network-troubleshoot`** | 6-step live network & service diagnostics across VLANs, DNS, OPNsense, and reverse proxies. | 6-stufige Live-Netzwerk- und Dienstdiagnose für VLANs, DNS, OPNsense und Reverse-Proxies. | Canlı ağ, DNS, 502/504 servis kesintileri ve UniFi/VLAN trafiği için 6 adımlı canlı teşhis. |
| **`unifi-wifi-hotspot-ops`** | UniFi OS Server AP management, RF channel and roaming tuning, and captive guest portal engineering. | UniFi OS AP-Verwaltung, RF-Kanal- und Roaming-Optimierung und Gäste-Captive-Portal. | UniFi Controller AP yönetimi, RF kanal ve dolaşım optimizasyonu, 5651 uyumlu misafir portalı. |
| **`docker-linux-deploy-ops`** | Docker Compose hardening on Debian LXC/VM, systemd unit generation, and zero-downtime deploys. | Docker Compose Härtung auf Debian LXC/VM, systemd-Dienste und Zero-Downtime-Deployment. | Debian 13 LXC/VM Docker Compose sıkılaştırma, systemd servisleri ve sıfır kesintili dağıtım. |
| **`observability-monitoring-ops`** | Uptime Kuma monitors, GoAccess real-time log analytics, Grafana/Prometheus, and blameless postmortems. | Uptime Kuma Monitoring, GoAccess Log-Analytik, Grafana/Prometheus und Postmortem-Analysen. | Uptime Kuma izleme, GoAccess gerçek zamanlı log analitiği, Grafana/Prometheus ve postmortem (RCA). |
| **`nextcloud-selfhosted-ops`** | Self-hosted Nextcloud occ maintenance, PHP/Redis/APCu caching tuning, and OnlyOffice integration. | Nextcloud occ Wartungsbefehle, PHP/Redis/APCu Performance-Tuning und OnlyOffice Integration. | Nextcloud occ bakım komutları, PHP/Redis/APCu optimizasyonu ve OnlyOffice entegrasyonu. |
| **`code-security-audit`** | Adversarial 6-phase source-code security audit and vulnerability hunting across fullstack apps. | 6-Phasen Quellcode-Sicherheitsaudit und Schwachstellensuche für Fullstack-Anwendungen. | Next.js, FastAPI, PHP ve Python kod tabanları için 6 fazlı kaynak kod zaafiyet avcılığı. |
| **`web-quality-modern-guidance`** | Modern web engineering, Core Web Vitals optimization, Next.js 16, React 19, and Lighthouse 95+. | Moderne Webentwicklung, Core Web Vitals Optimierung, Next.js 16, React 19 und Lighthouse 95+. | Next.js 16, React 19, Prisma, Tailwind, Core Web Vitals (LCP/INP/CLS) ve Lighthouse 95+ optimizasyonu. |
| **`frontend-design`** | Distinctive, production-grade frontend design ideation, design-tokens, and accessibility audits. | Hochwertiges Frontend-Design, Design-Tokens, Barrierefreiheit und umfassende UX-Audits. | Üst düzey kullanıcı arayüzü tasarımı, tasarım tokenleri, erişilebilirlik ve UX denetimleri. |
| **`editorial-web-design-studio`** | Anti-AI-slop art direction, DESIGN.md systems, Web Audio micro-sounds, and interaction design. | Anti-AI-Slop Art Direction, DESIGN.md Systeme, Web Audio Mikro-Sounds und Interaktionsdesign. | Anti-AI-slop sanat yönetimi, mikro ses efektleri (Web Audio), animasyonlar ve marka tasarımı. |
| **`editorial-architecture-diagrams`** | Publication-grade technical architecture diagrams, print-ready SVG/PNG figures, and HTML topologies. | Publikationsreife Architekturdiagramme, druckfertige SVG/PNG-Abbildungen und HTML-Topologien. | Yayın kalitesinde ağ mimarisi şemaları, baskıya hazır SVG/PNG figürleri ve HTML topolojileri. |
| **`technical-book-publishing`** | Technical book authoring, cross-reference governance, and B5 print/PDF/EPUB typesetting. | Verfassen von Fachbüchern, Querverweis-Prüfung und B5-Druck/PDF/EPUB-Satz. | Teknik kitap yazımı, çapraz referans denetimi ve B5 baskı/PDF/EPUB profesyonel dizgisi. |
| **`telegram-bot-alerting-ops`** | Python/Bash NOC alerting bots, ZED/OOM watchers, inline approval dialogs, and alert cooldowns. | Python/Bash NOC-Alerting-Bots, ZED/OOM Watcher, interaktive Genehmigungen und Alarm-Cooldowns. | Telegram NOC alarm botları, ZED/OOM takipçileri, inline yetkili onay mekanizması ve cooldown yönetimi. |
| **`whatsapp-bot-gateway-ops`** | Dual-mode WhatsApp gateway engineering (Baileys engine and Meta Cloud API) with HMAC webhooks. | Dual-Mode WhatsApp Gateway Entwicklung (Baileys Engine & Meta Cloud API) mit HMAC Webhooks. | Çift modlu WhatsApp bot ağ geçidi mühendisliği (Baileys ve Meta Cloud API) ve HMAC webhook güvenliği. |
| **`wordpress-woocommerce-ops`** | Safe WP-CLI operations as www-data, HPOS performance tuning, PHP 8.4-FPM, and custom plugin hardening. | Sichere WP-CLI Befehle als www-data, HPOS Performance-Tuning, PHP 8.4-FPM und Plugin-Härtung. | Güvenli www-data WP-CLI komutları, HPOS performans optimizasyonu, PHP 8.4-FPM ve eklenti sıkılaştırma. |
| **`matomo-analytics-ops`** | Self-hosted Matomo analytics Reporting API queries, JS tracking, and KVKK/GDPR privacy compliance. | Matomo Analytics Reporting API Abfragen, JS-Tracking und DSGVO/KVKK Datenschutz-Audits. | Self-hosted Matomo analitik Reporting API sorguları, JS izleme ve KVKK/GDPR gizlilik uyumluluğu. |
| **`video-director-engine`** | Code-rendered programmatic videos (Remotion), shot recipes, ElevenLabs TTS/SFX, and FFmpeg audio gating. | Code-gerendertes Video (Remotion), Schnitt-Rezepte, ElevenLabs TTS/SFX und FFmpeg Audio-Mastering. | Kodla video üretimi (Remotion), çekim tarifleri, ElevenLabs seslendirme ve FFmpeg ses mühendisliği. |
| **`native-pptx-presentations`** | Native PowerPoint (.pptx) deck generation from Markdown/PDF into corporate shapes, charts, and speaker notes. | Generierung nativer PowerPoint (.pptx) Folien aus Markdown/PDF mit Firmenvorlagen und Diagrammen. | Markdown/PDF kaynaklarından native düzenlenebilir PowerPoint (.pptx) sunum ve slayt üretimi. |
| **`quiz-word-game-master`** | Interactive HTML5 Canvas games, state machines, Web Audio FX, haptic feedback, and retention mechanics. | Interaktive HTML5 Canvas Spiele, State Machines, Web Audio FX, Haptik und Retention-Mechaniken. | İnteraktif HTML5 Canvas oyunları, durum makineleri, Web Audio efektleri ve mobil tutundurma mekaniği. |
| **`seo-content-master`** | Autonomous SEO/GEO content and audit engine, Wikidata entities, and llms.txt generation. | Autonome SEO/GEO Content-Engine, Wikidata Entitäten, PAS/BAB Copywriting und llms.txt Erstellung. | Otonom Türkçe ve küresel SEO içerik motoru, Wikidata varlıkları, PAS/BAB metinleri ve llms.txt üretimi. |
| **`social-media-growth`** | Multi-agent social media growth factory for Instagram, LinkedIn, and YouTube (60/25/15 rhythm). | Multi-Agenten Social Media Wachstumsfabrik für Instagram, LinkedIn und YouTube (60/25/15 Rhythmus). | Instagram, LinkedIn ve YouTube için çoklu ajan sosyal medya ve büyüme fabrikası. |
| **`founder-gtm-growth-council`** | Solo-founder idea validation, MVP scoping, value pricing psychology, and GTM launch roadmaps. | Ideenvalidierung für Solo-Gründer, MVP-Scoping, wertbasierte Preisgestaltung und GTM-Launch. | Fikir doğrulama, MVP kapsam belirleme, değer tabanlı fiyatlandırma ve GTM lansman stratejisi. |
| **`str-revenue-listing-master`** | Short-term rental revenue management, competitor rate benchmarking, and OTA parity. | Kurzzeitmiete-Ertragsmanagement, Mitbewerber-Preisanalyse und OTA-Provisionsparität. | Kısa dönem kiralama gelir yönetimi, rakip gecelik fiyat kıyaslama ve OTA komisyon paritesi. |
| **`steam-library-assistant`** | Steam library analysis, playtime statistics, co-op matching, and local disk transfer workflows. | Steam-Bibliotheksanalyse, Spielzeit-Statistiken, Co-Op-Matching und Festplatten-Spieletransfer. | Steam kütüphane analizi, oynama istatistikleri ve yerel sürücüler arası oyun taşıma otomasyonu. |

---

## ⚡ Optional MCP Integrations / Optionale MCP Server / Opsiyonel MCP Sunucuları

| Skill | Optional MCP Server | 🇬🇧 Capability Unlocked | 🇩🇪 Freigeschaltete Funktion | 🇹🇷 Sağladığı Ekstra Yetenek |
| :--- | :--- | :--- | :--- | :--- |
| **`editorial-web-design-studio`**<br>**`frontend-design`** | **Chrome DevTools MCP**<br>**Mobbin MCP** | Live computed CSS extraction, network waterfall audits, and access to 600k+ UI screens. | Auslesen von Live-CSS-Werten, Netzwerk-Wasserfall-Audits und Zugriff auf 600.000+ UI-Screens. | Canlı sitelerden hesaplanmış CSS alma, ağ şelale denetimi ve 600 bin+ gerçek ekran tasarımı. |
| **`str-revenue-listing-master`** | **Airbnb / OpenBNB MCP** | Competitor nightly-rate extraction and occupancy benchmarking. | Automatische Preis- und Belegungsanalyse von Mitbewerbern. | Rakip gecelik fiyat ve doluluk oranı kıyaslama. |
| **`steam-library-assistant`** | **Steam Web API MCP** | Direct library queries, playtime analytics, and friends co-op matching. | Direkte Bibliotheksabfragen, Spielzeitstatistiken und Co-Op-Matching. | Doğrudan kütüphane sorgulama, oynama istatistikleri ve arkadaş eşleştirme. |
| **`observability-monitoring-ops`** | **Prometheus / Grafana MCP** | Real-time PromQL querying and dashboard panel inspections. | Echtzeit-PromQL-Abfragen und Dashboard-Inspektionen. | Gerçek zamanlı PromQL sorgulama ve canlı gösterge paneli denetimi. |
| **`unifi-wifi-hotspot-ops`** | **UniFi Network MCP** | Read-only AP telemetry, client device counts, and RF maps. | Lesezugriff auf AP-Telemetrie, Endgeräte und RF-Kanalkarten. | Salt-okunur AP telemetrisi, bağlı cihaz sayısı ve RF kanal haritaları. |

---

## 🔒 Privacy & Sanitization Guarantee
This repository has been strictly sanitized:
* **No private IP addresses:** Subnets use standard RFC 1918 templates (`10.10.10.x`, `192.168.1.x`).
* **No private domains:** Replaced with standardized `.example.com` placeholders.
* **No secrets, tokens, or credentials:** All sensitive API keys and bots have been decoupled.

## 📄 License
Released under the [MIT License](LICENSE).
