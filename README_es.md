#Alien Box: La Biblia Musical Universal 👽

![Alien Box](alien_imagotype/screen.png)

🌐 **Léelo en:** [🇬🇧 English](README.md) | **🇪🇸 Español** | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

---

**Alien Box** es un motor de análisis de audio forense multimodal y un generador de plantillas DAW de última generación. Se conecta directamente a redes musicales globales para extraer metadatos reales de cualquier entrada de texto, analiza la frecuencia y los parámetros dinámicos de pistas comerciales y genera plantillas de inicio personalizadas para los principales DAW (Ableton, Logic Pro, Cubase, FL Studio, Pro Tools).

Construido con ingeniería de precisión por **CHUS BZN** en **produktes-code**.

## 🚀 Características
- **Búsqueda universal:** Ingrese cualquier enlace de YouTube, enlace de Spotify o texto libre (por ejemplo, "The Prodigy Poison").
- **Análisis forense brutal:** Calcula el LUFS objetivo, las curvas de ecualización específicas (cruce de bombo/bajo) y los tiempos de ataque/liberación de compresión VCA.
- **Exportación multimodal:** Genera un archivo ZIP real que contiene una plantilla DAW preenrutada.
- **UI orgánica:** Interfaz gráfica fluida y respirable con fondos de partículas dinámicas.
- **Manual PDF Universal Nativo (V14):** Manual en PDF generado en alta resolución traducido simétricamente a 7 idiomas, meticulosamente formateado y perfectamente escalado para impresión DIN A5.

## 🛠 Instalación

### 1. Configuración del servidor
El backend se ejecuta en un servidor Python ligero.
```golpecito
# 1. Inicie el servidor de análisis
python3 alienbox_server.py
```

### 2. Interfaz
Simplemente abra `splash_screen_organic_v3_final/code.html` en cualquier navegador web moderno.

### 3. Generar el Manual (V14)
Para compilar el manual universal V14 simétrico absoluto en formato DIN A5:
```golpecito
python3 build_universal_manual_v14.py
nodo print_multilingual_v14_pdf.js
```

## 📦 Instaladores de compilación (macOS y Windows)
Para empaquetar Alien Box en una aplicación de escritorio nativa, proporcionamos scripts de compilación para Electron/PyInstaller. Esto prepara el lanzamiento de nuestro repositorio de GitHub.

* **Mac OS (.dmg):** Ejecute `./build_mac.sh`
* **Windows (.exe):** Ejecute `build_win.bat`

---
*Parte del ecosistema `produktes-code`. CC BY-NC-SA 4.0. ESTÁNDAR CORPORATIVO - LISTO PARA LA VENTA AL POR MENOR.*