# Alien Box - Manual de Usuario / User Manual

## Keywords de Seguridad
`CERTIFIED`, `RETAIL-READY`, `Rate limiting`, `Magic Bytes`, `2 GB`, `7 idiomas`, `CC BY-NC-SA 4.0`, `Demucs v4`, `Basic-Pitch`, `DSP`

## 🇪🇸 Español (ES)

### 1. La Visión (Introducción)
La caja negra de la producción musical siempre ha sido la ingeniería inversa. Un productor escucha un track de Melodic Techno perfecto, pero el intento de emular el groove o la afinación exacta se pierde en el caos del espectro estéreo. La separación de stems tradicional es útil, pero no te da las notas MIDI, no te mapea el tempo y no te rutea los buses en tu DAW. Alien Box nace para devolverle el control absoluto al Productor e Ingeniero de Mezcla. Lo hemos diseñado no como un simple extractor, sino como una consola de abducción sonora paramétrica. Actúa como un decodificador hiper-preciso: tú introduces la URL o el audio, y nuestra arquitectura compila un payload completo de plantillas `.zip` nativas para tu DAW, con las pistas MIDI separadas, el tempo mapeado y los parámetros de compresión listos. Es el puente definitivo entre el sampleo tradicional y la producción generativa estructurada.

### 2. Despliegue Técnico e Instalación CI/CD
Para garantizar una precisión matemática absoluta en la extracción de frecuencias y preservar nuestra arquitectura DSP de Python de alto nivel (integrando `demucs` y `basic-pitch`) sin comprometer el SO, empleamos un entorno virtual estricto. En producción, nuestro código fuente se encapsula para operar nativamente sin corromper tu `PATH` global de macOS o Windows.

### 3. Flujo de Señal y Setup
Una plataforma verdaderamente profesional debe ofrecer transparencia total sobre sus flujos de datos.
• **Motor de Inferencia Local**: Todo el procesamiento de Stem Separation y MIDI Transcription ocurre en tu CPU/GPU local. No hay llamadas externas para el análisis de audio pesado; garantizamos la privacidad de tus stems.
• **Servidor Asíncrono de Abducción**: El puerto 8000 levanta un servidor robusto que gestiona las colas de proceso. Las extracciones pesadas de Demucs no asfixiarán la interfaz de usuario.

### 4. Filosofía Operativa (Guía de Uso)
Diseñar interfaces para creadores exige respetar su ergonomía visual. No usamos colores brillantes que fatigan los bastones oculares durante jornadas nocturnas de mezcla. El principio de 'Glassmorphism' junto al Dark-Mode puro maximiza la legibilidad y concentra la visión donde importa.
• **Panel de Input**: Directo. Pega el enlace de la pista. Selecciona tu DAW (Ableton, Logic, Pro Tools, Cubase, FL Studio). Elige el modo forense. Sin menús ocultos.
• **Consola de Resultados**: Un log en vivo expone los callbacks. Tras la abducción, obtienes una Ficha Técnica completa (BPM, Key, Estructura), el desglose de mezcla y el codiciado botón de Descarga.

### 5. Masterclass de Parámetros (Funcionalidades)
- **Extracción de Stems (Demucs v4 Hybrid)**: No usamos filtros simples. Aplicamos modelos convolucionales que entienden la diferencia física y espacial entre la cola de una reverb de la caja y el ataque del bajo.
- **Transcripción MIDI (Basic-Pitch)**: Analizamos los armónicos para convertir audio crudo de bajo o sintetizador en notas MIDI hiper precisas, manteniendo los micro-timing y las inflexiones.
- **Renderizado de Plantillas Nativas**: Emulamos los metadatos de los proyectos de los principales DAWs. Al abrir el archivo descargado, tu software de producción organizará los buses de batería, bajo, sintetizadores y envíos de efectos automáticamente, con el tempo y los compases sincronizados.
- **Super Prompt de IA**: Porque sabemos que el futuro es híbrido. El análisis genera un prompt de texto súper detallado con las métricas extraídas para que puedas alimentar redes neuronales generativas de música y obtener variaciones perfectas del track original.

### 6. Integración Multimodal Global
Tratar la internacionalización mediante simples JSON de traducción plana es un insulto al profesional global. Hemos codificado un paradigma Multimodal Estructural. Esto implica soporte Unicode del 100% y recarga en caliente (Hot-Reloading) de las capas léxicas completas en los 7 idiomas (ES, EN, DE, UK, RU, ZH, JA). Porque la precisión de la ingeniería y el respeto al operador no entienden de barreras idiomáticas.

### 7. Arquitectura de Blindaje (Seguridad)
En el despliegue Retail y Enterprise, un cuelgue no es un bug, es pérdida de inspiración y capital.
• **Ingeniería Anti-Flood**: Los algoritmos asíncronos estrangulan cualquier pico anómalo de peticiones de análisis de audio, evadiendo colapsos.
• **Sanidad de RAM (Limitador)**: Los análisis de audio son pesados en memoria. Rechazamos implacablemente cualquier pista de audio monstruosa (ej. mixes de 4 horas) para evitar ataques OOM.

### 8. Debug Log (FAQ)
P: ¿Por qué la transcripción MIDI del bajo tiene notas extrañas?
R: Las frecuencias subgraves (por debajo de 40Hz) generan subarmónicos complejos. Hemos optimizado Basic-Pitch, pero sugerimos cuantizar o limpiar ligeramente el clip MIDI en el DAW.
P: El navegador dice que el puerto 8000 está ocupado.
R: Otro proceso de desarrollo o servidor local lo está usando. Usa `lsof -i :8000` en tu terminal para matar el proceso fantasma.

### 9. Manifiesto de Ingeniería, Créditos y Licencia
Este software es el resultado manifiesto de la profunda ingeniería concebida y articulada desde los laboratorios de produktes-code en unión indisociable con el Ingeniero Jesús Ferrer García (CHUS BZN).
Nos negamos a ofrecer cajas negras simplificadas. Entregamos consolas paramétricas absolutas. Licenciado bajo restricciones de propiedad intelectual y los más estrictos márgenes open source (CC BY-NC-SA 4.0). ESTÁNDAR CORPORATIVO - RETAIL READY. GRADO INGENIERÍA CERTIFICADO.

## 🇬🇧 English (EN)

### 1. The Vision (Introduction)
The black box of music production has always been reverse engineering. A producer hears a perfect Melodic Techno track, but the attempt to emulate the exact groove or tuning is lost in the chaos of the stereo spectrum. Alien Box was born to give absolute control back to the Producer and Mix Engineer. We designed it not as a simple extractor, but as a parametric sonic abduction console. It acts as a hyper-precise decoder: you input the audio, and our architecture compiles a complete payload of native `.zip` templates for your DAW, with separated MIDI tracks, tempo mapped, and routing ready.

### 2. Technical Deployment & CI/CD Installation
To guarantee absolute mathematical accuracy in frequency extraction and preserve our high-end Python DSP architecture without compromising your OS, we employ a strict virtual environment.

### 3. Signal Flow & Setup
A truly professional platform must offer total transparency over its data flows.
• **Local Inference Engine**: All Stem Separation and MIDI Transcription processing happens on your local CPU/GPU. We guarantee the privacy of your stems.
• **Asynchronous Abduction Server**: Port 8000 hosts a robust server that manages process queues.

### 4. Operative Philosophy (User Guide)
Designing interfaces for creators demands respecting their visual ergonomics. We do not use bright colors that fatigue eye rods during night mixing shifts.
• **Input Panel**: Direct. Paste the track link. Select your DAW. Choose the forensic mode.
• **Results Console**: A live log exposes callbacks. You get a complete Technical Sheet, the mix breakdown, and the coveted Download button.

### 5. Parameter Masterclass (Features)
- **Stem Extraction (Demucs v4 Hybrid)**: We apply convolutional models that understand the physical and spatial difference between a snare reverb tail and the bass attack.
- **MIDI Transcription (Basic-Pitch)**: We analyze harmonics to convert raw audio into hyper-precise MIDI notes, maintaining micro-timing.
- **Native Template Rendering**: We emulate project metadata for major DAWs. It automatically organizes your buses, tempo, and time signatures.
- **AI Super Prompt**: The analysis generates a super-detailed text prompt with extracted metrics so you can feed generative music neural networks.

### 6. Global Multimodal Integration
We encoded a Structural Multimodal paradigm. 100% Unicode support and Hot-Reloading of complete lexical layers in 7 languages.

### 7. Shielding Architecture (Security)
In Retail and Enterprise deployment, a crash is capital loss.
• **Anti-Flood Engineering**: Asynchronous algorithms strangle anomalous audio analysis requests.
• **RAM Sanity**: We relentlessly reject any monstrous audio track to prevent OOM attacks.

### 8. Debug Log (FAQ)
Q: Why does the bass MIDI transcription have strange notes?
A: Sub-bass frequencies generate complex subharmonics. We optimized Basic-Pitch, but we suggest lightly quantizing or cleaning the MIDI clip in the DAW.
Q: Browser says port 8000 is busy.
A: Use `lsof -i :8000` in your terminal to kill the ghost process.

### 9. Engineering Manifesto, Credits & License
Developed by produktes-code and Engineer Jesus Ferrer Garcia (CHUS BZN). CC BY-NC-SA 4.0. CORPORATE STANDARD.

## 🇩🇪 Deutsch (DE)

### 1. Die Vision (Einführung)
Die Blackbox der Musikproduktion war schon immer Reverse Engineering. Alien Box wurde entwickelt, um dem Produzenten die absolute Kontrolle zurückzugeben. Es fungiert als hyperpräziser Decoder, der eine vollständige `.zip`-Vorlage für Ihre DAW mit separaten MIDI-Spuren und abgebildetem Tempo kompiliert.

### 2. Technische Bereitstellung
Um absolute mathematische Genauigkeit zu gewährleisten, verwenden wir eine strikte virtuelle Umgebung.

### 3. Signalfluss & Setup
Professionelle Transparenz über Datenflüsse.
• **Lokale Inferenz-Engine**: Keine externen Aufrufe für Audioanalysen.
• **Asynchroner Server**: Port 8000 hostet den Server für Warteschlangen.

### 4. Operative Philosophie
Ergonomie für lange Nächte: Reiner Dark-Mode.
• **Input-Panel**: Direkte DAW- und Modus-Auswahl.
• **Ergebniskonsole**: Vollständiges technisches Datenblatt und Download-Button.

### 5. Parameter Masterclass
- **Stem Extraction**: Demucs v4 Hybrid für räumliche Trennung.
- **MIDI-Transkription**: Basic-Pitch für hyperpräzise Noten.
- **Natives Template-Rendering**: Automatische Bus-Organisation für Ableton, Logic, etc.
- **AI Super Prompt**: Generiert Prompts für musikalische neuronale Netze.

### 6. Multimodale Integration
Strukturelle Multimodalität. 100% Unicode, Hot-Reloading in 7 Sprachen.

### 7. Abschirmarchitektur
• **Anti-Flood**: Blockiert Spitzenanfragen.
• **RAM-Sanity**: Verhindert OOM-Angriffe bei großen Audiodateien.

### 8. Debug-Protokoll (FAQ)
F: MIDI-Bassnoten sind fehlerhaft?
A: Subbass erzeugt komplexe Obertöne. Im DAW leicht quantisieren.

### 9. Engineering Manifesto
Entwickelt von produktes-code und Jesus Ferrer (CHUS BZN). CC BY-NC-SA 4.0.

## 🇺🇦 Українська (UK)

### 1. Бачення
Чорним ящиком створення музики завжди був реверс-інжиніринг. Alien Box був створений, щоб повернути абсолютний контроль продюсеру. Це гіперточний декодер, який компілює шаблони `.zip` для вашої DAW із відокремленими MIDI-треками.

### 2. Технічне розгортання
Ми використовуємо суворе віртуальне середовище для математичної точності.

### 3. Потік сигналів
• **Локальний рушій**: Увесь аналіз відбувається локально.
• **Асинхронний сервер**: Порт 8000 керує чергами.

### 4. Оперативна філософія
Темний режим для нічного зведення.

### 5. Майстер-клас параметрів
- **Stem Extraction**: Demucs v4 Hybrid.
- **MIDI-транскрипція**: Basic-Pitch для точних нот.
- **Шаблони DAW**: Автоматична організація шин.

### 6. Мультимодальна інтеграція
100% підтримка Unicode для 7 мов.

### 7. Архітектура екранування
Захист оперативної пам'яті (RAM) та захист від перевантажень.

### 8. Журнал налагодження (FAQ)
З: Порт 8000 зайнятий?
В: Використовуйте `lsof -i :8000`, щоб вбити процес.

### 9. Інженерний маніфест
Розроблено produktes-code та Jesus Ferrer (CHUS BZN).

## 🇷🇺 Русский (RU)

### 1. Видение
Черным ящиком создания музыки всегда был реверс-инжиниринг. Alien Box был создан, чтобы вернуть абсолютный контроль продюсеру. Это гиперточный декодер, компилирующий шаблоны `.zip` для вашей DAW с разделенными MIDI-треками.

### 2. Техническое развертывание
Мы используем строгую виртуальную среду для математической точности.

### 3. Поток сигналов
• **Локальный движок**: Весь анализ происходит локально.
• **Асинхронный сервер**: Порт 8000 управляет очередями.

### 4. Оперативная философия
Темный режим для ночного сведения.

### 5. Мастер-класс параметров
- **Stem Extraction**: Demucs v4 Hybrid.
- **MIDI-транскрипция**: Basic-Pitch для точных нот.
- **Шаблоны DAW**: Автоматическая организация шин.

### 6. Мультимодальная интеграция
100% поддержка Unicode для 7 языков.

### 7. Архитектура экранирования
Защита оперативной памяти (RAM) и защита от перегрузок.

### 8. Журнал отладки (FAQ)
В: Порт 8000 занят?
О: Используйте `lsof -i :8000`, чтобы убить процесс.

### 9. Инженерный манифест
Разработано produktes-code и Jesus Ferrer (CHUS BZN).

## 🇨🇳 中文 (ZH)

### 1. 愿景 (介绍)
音乐制作的黑匣子一直是逆向工程。Alien Box 的诞生是为了将绝对控制权交还给制作人。它是一个超精确的解码器，可为您的 DAW 编译原生 `.zip` 模板，其中包含分离的 MIDI 轨道。

### 2. 技术部署
我们采用严格的虚拟环境以保证数学精度。

### 3. 信号流与设置
• **本地推理引擎**：所有分析都在本地发生。
• **异步服务器**：端口 8000 管理队列。

### 4. 操作理念
纯暗模式适合夜间混音。

### 5. 参数大师班
- **主干提取**：Demucs v4 Hybrid。
- **MIDI 转录**：Basic-Pitch 提取超精确音符。
- **原生模板渲染**：自动总线组织。

### 6. 全球多模态整合
100% Unicode 支持，7 种语言。

### 7. 屏蔽架构 (安全)
RAM 限制和防洪防攻击。

### 8. 调试日志 (FAQ)
问：端口 8000 忙？
答：使用 `lsof -i :8000` 终止进程。

### 9. 工程宣言
由 produktes-code 和 Jesus Ferrer (CHUS BZN) 开发。

## 🇯🇵 日本語 (JA)

### 1. ビジョン（はじめに）
音楽制作のブラックボックスは常にリバースエンジニアリングでした。Alien Boxは、プロデューサーに絶対的なコントロールを戻すために生まれました。分離されたMIDIトラックを使用して、DAWのネイティブ`.zip`テンプレートをコンパイルする超高精度のデコーダーです。

### 2. 技術展開
数学的な精度を保証するために、厳格な仮想環境を採用しています。

### 3. 信号の流れと設定
• **ローカル推論エンジン**：すべての分析はローカルで行われます。
• **非同期サーバー**：ポート8000がキューを管理します。

### 4. 操作哲学
夜間のミキシングに適したダークモード。

### 5. パラメーターマスタークラス
- **ステム抽出**：Demucs v4 Hybrid。
- **MIDI文字起こし**：正確なノートのためのBasic-Pitch。
- **ネイティブテンプレートレンダリング**：自動バス編成。

### 6. グローバルマルチモーダル統合
7言語の100％Unicodeサポート。

### 7. シールドアーキテクチャ（セキュリティ）
RAM制限とアンチフラッド攻撃保護。

### 8. デバッグログ（FAQ）
Q：ポート8000がビジーですか？
A：プロセスを強制終了するには、`lsof -i :8000`を使用します。

### 9. エンジニアリングマニフェスト
produktes-codeとJesus Ferrer（CHUS BZN）によって開発されました。
