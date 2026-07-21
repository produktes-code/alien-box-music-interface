# Alien Box: Die universelle Musikbibel 👽

![Alien Box](alien_imagotype/screen.png)

🌐 **Lies das auf:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | **🇩🇪 Deutsch** | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

---

**Alien Box** ist eine hochmoderne multimodale forensische Audioanalyse-Engine und ein DAW-Vorlagengenerator. Es stellt eine direkte Verbindung zu globalen Musiknetzwerken her, um echte Metadaten aus jeder Texteingabe zu extrahieren, analysiert die Frequenz und dynamischen Parameter kommerzieller Tracks und generiert maßgeschneiderte Starter-Vorlagen für die wichtigsten DAWs (Ableton, Logic Pro, Cubase, FL Studio, Pro Tools).

Gebaut mit Präzisionstechnik von **CHUS BZN** bei **produktes-code**.

## 🚀 Funktionen
- **Universelle Suche:** Geben Sie einen beliebigen YouTube-Link, Spotify-Link oder Freitext ein (z. B. „The Prodigy Poison“).
- **Brutale forensische Analyse:** Berechnet Ziel-LUFS, spezifische EQ-Kurven (Kick/Bass-Crossover) und VCA-Komprimierungs-Attack-/Release-Zeiten.
- **Multimodaler Export:** Erzeugt eine echte ZIP-Datei, die eine vorgeroutete DAW-Vorlage enthält.
- **Organische Benutzeroberfläche:** Flüssige, atmende grafische Benutzeroberfläche mit dynamischen Partikelhintergründen.
- **Native Universal PDF-Handbuch (V14):** Hochauflösend generiertes PDF-Handbuch, symmetrisch in 7 Sprachen übersetzt, sorgfältig formatiert und perfekt skaliert für den DIN-A5-Druck.

## 🛠 Installation

### 1. Backend-Setup
Das Backend läuft auf einem leichtgewichtigen Python-Server.
„Bash
# 1. Starten Sie den Analyseserver
python3 alienbox_server.py
„

### 2. Frontend
Öffnen Sie einfach „splash_screen_organic_v3_final/code.html“ in einem modernen Webbrowser.

### 3. Erstellen Sie das Handbuch (V14)
So stellen Sie das absolut symmetrische V14-Universalhandbuch im DIN-A5-Layout zusammen:
„Bash
python3 build_universal_manual_v14.py
Knoten print_multilingual_v14_pdf.js
„

## 📦 Installationsprogramme erstellen (macOS und Windows)
Um Alien Box in eine native Desktop-Anwendung zu packen, stellen wir Build-Skripte für Electron/PyInstaller bereit. Dadurch wird die Veröffentlichung für unser GitHub-Repository vorbereitet.

* **Mac OS (.dmg):** Führen Sie „./build_mac.sh“ aus
* **Windows (.exe):** Führen Sie „build_win.bat“ aus

---
*Teil des „produktes-code“-Ökosystems. CC BY-NC-SA 4.0. UNTERNEHMENSSTANDARD – BEREIT FÜR DEN EINZELHANDEL.*