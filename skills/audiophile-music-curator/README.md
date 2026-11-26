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

## 🚘 Verified Car Infotainment & Model Compatibility Matrix

This standard is engineered to comply with the strictest automotive infotainment memory and codec requirements. Tested and verified for:

| Group / Manufacturer | Brands | Verified Popular Car Models | Infotainment Systems | Model Years |
| :--- | :--- | :--- | :--- | :--- |
| **Stellantis** | **Opel**, Peugeot, Citroën, Fiat, Alfa Romeo, Jeep, DS | **Corsa (D/E/F), Astra (J/K/L), Mokka, Crossland, Grandland, Insignia**; 208, 308, 2008, 3008, 5008, 508; C3, C3 Aircross, C4, C5 Aircross; Egea/Tipo, 500, 500X, Doblo, Fiorino; Giulietta, Tonale; Renegade, Compass; DS3, DS7 | IntelliLink (R4.0, Navi 4.0, 900), SMEG, SMEG+, NAC, i-Cockpit, Uconnect 5.0/7.0/8.4/10.25 | 2010 – 2026 |
| **VAG Group** | Volkswagen, Audi, SEAT, Škoda, Cupra | **Polo, Golf (6/7/8), Passat (B7/B8), Tiguan, T-Roc, Arteon, Caddy, Transporter**; A1, A3 (8V/8Y), A4 (B8/B9), A5, Q2, Q3, Q5; Ibiza, Leon (Mk3/Mk4), Arona, Ateca; Fabia, Scala, Octavia (A7/A8), Superb, Kodiaq; Formentor, Cupra Leon | Composition Colour/Media, Discover Media/Pro, MIB1, MIB2, MIB2.5, MIB3, Audi MMI 3G/Touch, RNS 315/510 | 2009 – 2026 |
| **Renault-Nissan-Dacia** | Renault, Dacia, Nissan | **Clio (3/4/5), Megane (3/4), Captur, Kadjar, Austral, Talisman, Fluence, Kangoo**; Duster, Sandero, Stepway, Jogger; Micra, Juke, Qashqai (J10/J11/J12), X-Trail | MediaNav, MediaNav Evolution, R-Link 1 & 2, Easy Link, OpenR Link, NissanConnect 1/2/3 | 2010 – 2026 |
| **Ford** | Ford | **Fiesta, Focus (Mk3/Mk4), Puma, Kuga, Mondeo, EcoSport, Tourneo Courier / Connect, Transit** | Monochrome Audio Matrix, Ford SYNC 1, SYNC 2 (MyFord Touch), SYNC 3, SYNC 4 | 2011 – 2026 |
| **Toyota & Lexus** | Toyota, Lexus | **Corolla, Yaris, C-HR, RAV4, Auris, Avensis, Hilux, Proace**; Lexus CT200h, IS, ES, NX, RX | Toyota Touch, Touch & Go, Touch 2, Toyota Smart Connect, Lexus Display Audio | 2011 – 2026 |
| **BMW Group** | BMW, MINI | **1 Serisi (F20/F40), 2 Serisi, 3 Serisi (E90 LCI/F30/G20), 4 Serisi, 5 Serisi (F10/G30), X1, X3, X5**; MINI Cooper, Countryman, Clubman | iDrive (CIC, NBT, NBT Evo ID4/5/6, iDrive 7/8), MINI Visual Boost / Connected | 2008 – 2026 |
| **Mercedes-Benz** | Mercedes-Benz | **A-Serisi (W176/W177), B-Serisi, C-Serisi (W204 FL/W205/W206), E-Serisi (W212/W213), CLA, GLA, GLB, GLC, Vito** | Audio 20, COMAND NTG 4.0, NTG 4.5, NTG 5.0, NTG 5.5, MBUX | 2010 – 2026 |
| **Hyundai-Kia** | Hyundai, Kia | **i10, i20, i30, Bayon, Elantra, Kona, Tucson, Santa Fe**; Picanto, Rio, Ceed, Cerato, Stonic, XCeed, Sportage, Sorento | Mobis Standard 5"/7" Display Audio, Gen5, Gen5W Widescreen (10.25"), ccNC | 2012 – 2026 |
| **Honda & Japanese** | Honda, Mazda, Suzuki, Mitsubishi, Subaru | **Civic (FC5/FE1), Jazz, HR-V, CR-V**; Mazda 3, CX-3, CX-5; Suzuki Swift, Vitara; Mitsubishi ASX; Subaru XV, Forester | Honda Connect, MZD Connect, Suzuki SLDA (Bosch), Smartphone Link Display Audio | 2013 – 2026 |
| **Aftermarket & Android** | Pioneer, Kenwood, Sony, Alpine, Android | **All 1-DIN / 2-DIN aftermarket head units** and all universal Android car infotainment displays (Roadstar, Navigold, Avgo, Multix, For-X vb.) | USB Audio 2.0 Mass Storage Class (MSC) | 2008 – 2026 |

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
