# Alien Box: The Universal Musical Bible 👽

![Alien Box](alien_imagotype/screen.png)

🌐 **Read this in:** **🇬🇧 English** | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---


**Alien Box** is a state-of-the-art multimodal forensic audio analysis engine and DAW template generator. It connects directly to global music networks to extract real metadata from any text input, dissects the frequency and dynamic parameters of commercial tracks, and generates customized starter templates for major DAWs (Ableton, Logic Pro, Cubase, FL Studio, Pro Tools).

Built with precision engineering by **CHUS BZN** at **produktes-code**.

## 🚀 Features
- **Universal Search:** Input any YouTube link, Spotify link, or free text (e.g., "The Prodigy Poison").
- **Brutal Forensic Analysis:** Calculates Target LUFS, specific EQ curves (Kick/Bass crossover), and VCA compression attack/release times.
- **Multimodal Export:** Generates a real ZIP file containing a pre-routed DAW template.
- **Organic UI:** Fluid, breathing graphic interface with dynamic particle backgrounds.
- **Native Universal PDF Manual (V14):** High-resolution generated PDF manual translated symmetrically into 7 languages, meticulously formatted and perfectly scaled for DIN A5 printing.

## 🛠 Installation

### 1. Backend Setup
The backend runs on a lightweight Python server.
```bash
# 1. Start the analysis server
python3 alienbox_server.py
```

### 2. Frontend
Just open `splash_screen_organic_v3_final/code.html` in any modern web browser.

### 3. Generate the Manual (V14)
To compile the absolute symmetrical V14 Universal Manual in DIN A5 layout:
```bash
python3 build_universal_manual_v14.py
node print_multilingual_v14_pdf.js
```

## 📦 Building Installers (macOS & Windows)
To package Alien Box into a native desktop application, we provide build scripts for Electron/PyInstaller. This prepares the release for our GitHub repository.

*   **Mac OS (.dmg):** Run `./build_mac.sh`
*   **Windows (.exe):** Run `build_win.bat`

---
*Part of the `produktes-code` ecosystem. CC BY-NC-SA 4.0. CORPORATE STANDARD - RETAIL READY.*
