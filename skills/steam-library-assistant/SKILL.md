---
name: steam-library-assistant
description: >-
  Steam library analysis, playtime statistics, co-op/friend matching, local disk game transfers,
  and Steam Web API / Steamworks MCP workflows. Use when analyzing Steam libraries, moving Steam
  games across local drives, or querying Steam stats. Do NOT use for building browser/HTML5
  games (use quiz-word-game-master) or Proxmox/Linux storage operations (use proxmox-ve-ops).
---

# Steam Library & Gaming Assistant

Bu skill, kullanıcının **Steam kütüphanesini**, **oyun istatistiklerini**, **yerel disk alanını** ve **Steam mağaza/geliştirici araçlarını** yapay zeka asistanıyla (Antigravity, Claude Desktop, Claude Code) yönetmek için derlenen araç ve iş akışı rehberidir.

---

## 1. Steam Web API & Kütüphane Sorgulama MCP Sunucuları
Doğal dil ile *"Kütüphanemde arkadaşlarımla oynayabileceğim hangi co-op oyunlar var?", "En az oynadığım RPG hangisi?", "Hafta sonu bitirebileceğim kısa oyunları listele"* gibi sorgular için:

- **Resmi / Web API Tabanlı MCP'ler:**
  - `steamwebapi.com/mcp` — Steam Web API üzerinden profil, sahip olunan oyunlar, oynama süreleri ve başarım sorguları.
  - `TMHSDigital/steam-mcp` — Kütüphane, oyun detayları ve istatistik sorgulama.
  - `sandraschi/steam-mcp` — Kütüphane, arkadaş listesi ve oyun verisi analizi.
  - `matheusslg/steam-mcp` — Steam Web API entegrasyonu ve oyun öneri sorguları.
  - `jkiley129/steam-mcp` — Oyun geçmişi ve kütüphane filtreleme.
  - `jimsantora/simple-steam-mcp` — Hafif ve hızlı Steam API MCP sunucusu.
  - `mcpmarket.com/server/steam-2` — Topluluk dizini Steam MCP sunucusu.

### Örnek Sorgu Şablonları
1. **Backlog Temizliği:** *"Steam kütüphanemde satın alıp hiç (0 saat) veya 2 saatten az oynadığım oyunları türüne ve tahmini bitirme süresine göre sırala."*
2. **Arkadaşlarla Co-Op Eşleştirme:** *"Benim ve [Arkadaş Steam ID] kütüphanesinde ortak bulunan co-op / multiplayer oyunları listele."*
3. **Tür & Ruh Hali Filtresi:** *"Şu an yüklü oyunlar arasından tek oturuşta 1-2 saat oynanabilecek strateji veya roguelike oyunları öner."*

---

## 2. Yerel Steam Kurulumu & Disk Yönetimi (`steam-local` / `steam-library-explorer`)
- **`steam-local` (`claudecodeagents.com/mcp/steam-local`):** Bilgisayardaki yerel `libraryfolders.vdf` ve `appmanifest_*.acf` dosyalarını okuyarak hangi oyunun hangi diskte, ne kadar yer kapladığını analiz eder.
- **`steam-library-explorer` (`rpaquay/SteamLibraryExplorer` & MCP skill türevleri):** Birden fazla SSD/HDD üzerindeki Steam kütüphane klasörlerini görüntüler; oyunları ve Workshop içeriklerini sürücüler arasında güvenli şekilde taşımaya yardımcı olur.

---

## 3. Tarayıcı & Platform Eklentileri
- **`NemoKing1210/steam-plus`:** ScriptCat / Tampermonkey üzerinde çalışan userscript. Steam Mağaza ve Topluluk sayfalarında oyun açıklamalarını, kullanıcı incelemelerini, profil yorumlarını ve haberleri satır içi otomatik çevirir.
- **`420noscope-exe/Claude-Desktop-for-Steam-Frame`:** Valve Steam Frame VR ekosistemi üzerinde Claude Desktop çalıştırmak için yardımcı kurulum scripti.

---

## 4. Oyun Geliştiriciler İçin: Steamworks Yayın Asistanı
- **`wazzapsenk/steamworks-mcp`:** Unity, Godot veya Unreal Engine projelerini Valve'ın Steamworks teknik yayın kurallarına göre tarar; mağaza açıklamalarını hazırlar ve Steamworks yapılandırma hatalarını önceden yakalar.
- **İlgili Stüdyo Referansı:** `donchitos/claude-code-game-studios` (Çoklu ajanlı Unity/Unreal/Godot oyun geliştirme rol hiyerarşisi).

---

## 5. Güvenlik & Gizlilik Kuralları
1. **Steam Web API Key & SteamID:** API anahtarlarını asla repo içine veya `.claude/settings.local.json` gibi commit edilebilir dosyalara yazma; yalnızca `.env` (`.gitignore` içinde) veya yerel MCP gizli değişkenlerinde sakla.
2. **Profil Gizliliği:** Arkadaş karşılaştırması veya kütüphane taraması için ilgili Steam profilinin *"Oyun Detayları"* gizlilik ayarının geçici olarak *"Herkese Açık"* olması gerekir; işlem bitince tekrar *"Arkadaşlar"* veya *"Gizli"* konumuna alınması önerilir.
