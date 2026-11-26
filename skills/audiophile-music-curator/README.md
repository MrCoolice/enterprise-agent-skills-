# 🎵 Audiophile Music Curator & Universal Car Audio Station (v3.0)

> **Autonomous Audiophile Music Library Curation & Universal Automotive USB Mirror Sync**
> 
> Works out-of-the-box for **all car infotainment systems** (Opel, Volkswagen, Ford, Renault, Fiat, Toyota, BMW, Mercedes, Peugeot, Hyundai/Kia, and Aftermarket units) and synchronizes with **Nextcloud** or local music directories.

---

## 🌟 Key Features

- **🚗 Universal Automotive Standard:** Formats USB drives with **MBR** partition table and **FAT32** filesystem via automated `diskpart` (compatible with 2008–2026 car head units).
- **🎚️ Audiophile Loudness Normalization:** Standardizes all tracks to **EBU R128 (-14.0 LUFS / -1.5 dB True Peak)**, preventing ear-shattering transitions and inaudible tracks during road travel.
- **🖼️ 500x500 Baseline JPEG Covers:** Downscales and crops album covers to exact 500x500 square Baseline JPEG embedded in ID3v2.3 `APIC` (prevents dashboard RAM crashes and black screens).
- **🎤 Synced & Plain Lyrics:** Integrates with LRCLIB to embed synchronized or plain lyrics in ID3 `USLT` frames.
- **🔄 True Mirror Synchronization:** High-speed atomic sync from Nextcloud/Local library to USB. Orphan files deleted from the source are cleanly pruned from the USB.
- **🤖 Autonomous AI Agent Ready:** Zero manual configuration needed. AI agents (Gemini, Claude, Cursor, Codex) can bootstrap the environment with 1 single command.

---

## 🚘 Verified Car Infotainment Compatibility

| Brand Group | Makes | Infotainment Systems |
| :--- | :--- | :--- |
| **Stellantis** | Peugeot, Citroën, Fiat, Opel, Alfa Romeo, Jeep, DS | IntelliLink R4.0/Navi, SMEG/SMEG+, NAC, i-Cockpit, Uconnect 5.0/7.0/8.4 |
| **VAG Group** | Volkswagen, Audi, SEAT, Škoda, Cupra | MIB1, MIB2, MIB3, RNS 315/510, Composition Media, Discover Media, MMI |
| **Renault-Nissan** | Renault, Dacia, Nissan | MediaNav, MediaNav Evolution, R-Link 1/2, Easy Link, NissanConnect |
| **Ford** | Ford (Fiesta, Focus, Puma, Kuga, Mondeo) | SYNC 1, SYNC 2 (MyFord Touch), SYNC 3, SYNC 4 |
| **Toyota & Lexus** | Toyota, Lexus | Toyota Touch, Touch 2, Smart Connect, Lexus Display Audio |
| **BMW Group** | BMW, MINI | iDrive (CIC, NBT, NBT Evo, iDrive 7/8), MINI Connected |
| **Mercedes-Benz** | Mercedes-Benz | Audio 20, COMAND NTG 4.5/5.0/5.5, MBUX |
| **Hyundai-Kia** | Hyundai, Kia | Mobis Display Audio, Standart Gen5, Gen5W, ccNC |
| **Aftermarket** | Pioneer, Kenwood, Sony, Alpine, Android | All USB-capable aftermarket head units and Android car stereos |

---

## ⚡ 1-Click Quick Start (For Humans & AI Agents)

### 1. Autonomous Bootstrap
Run this single command to verify Python, install `mutagen`, `Pillow`, `yt-dlp`, and verify `ffmpeg`:
```bash
python scripts/bootstrap.py
```

### 2. Launch Universal Car Audio Station
```bash
# Windows (Interactive Launcher)
Oto_Muzik_Merkezi.bat

# Or direct Python
python scripts/car_audio_station.py
```

---

## 📂 Project Structure

```
skills/audiophile-music-curator/
├── SKILL.md                   # Full Antigravity AI Agent Skill Definition
├── README.md                  # This documentation
├── requirements.txt           # Python dependencies (mutagen, Pillow, yt-dlp)
└── scripts/
    ├── bootstrap.py           # 1-click autonomous dependency & system installer
    ├── car_audio_station.py   # Universal Car Audio Station v3.0 (Interactive Menu)
    ├── corsa_station.py       # Backward compatibility forwarding wrapper
    ├── library_config.py      # Dynamic 4-tier music directory resolver
    ├── Oto_Muzik_Merkezi.bat  # 1-click Windows desktop batch launcher
    ├── Corsa_Muzik_Merkezi.bat# Backward-compatible batch launcher
    ├── audit_library.py       # Health audit (missing covers, lyrics, paths)
    ├── normalize_audio.py     # EBU R128 (-14 LUFS) loudness normalizer
    ├── embed_metadata.py      # iTunes/Deezer/LRCLIB tagger & 500x500 JPEG embedder
    └── sync_usb.py            # High-speed delta mirror sync to USB
```

---

## ⚙️ Custom Music Library Paths

The station automatically detects:
1. `AUDIOPHILE_MUSIC_DIR` or `CORSA_MUSIC_DIR` environment variables.
2. `config.json` custom directory.
3. `~/Nextcloud/Music` or default OS `~/Music`.
4. Option `[4]` in the interactive menu allows setting any custom path (e.g. `D:\MyMusic`).
