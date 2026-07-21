import re

langs = ['es', 'en', 'ru', 'uk', 'zh', 'ja', 'de']

content = {
    'es': {
        'title': 'Manual Técnico de Operaciones',
        'subtitle': 'VERSIÓN 1.0.0 (RELEASE CANDIDATE)',
        'confidential': 'Confidencial – DSP Architecture',
        'ch1': '1. ARQUITECTURA DEL SISTEMA',
        'ch1_sub1': '¿Qué es Alien Box?',
        'ch1_text1': 'Alien Box es una estación forense de análisis de audio basada en redes neuronales profundas. A diferencia de un separador de stems tradicional, Alien Box utiliza la matriz Demucs v4 combinada con algoritmos de transcripción Basic-Pitch para decodificar el ADN musical de cualquier track comercial.\\n\\nEl sistema está diseñado para operar en la fase de pre-producción y estudio (White Room), ofreciendo a los productores la capacidad de abducir la firma espectral, el rango dinámico y los patrones MIDI de referencias complejas, exportándolos instantáneamente como plantillas nativas para entornos DAW.',
        'ch1_sub2': 'Motor Alien Bioworks',
        'ch1_text2': 'El núcleo del sistema ("Alien Engine") ejecuta procesos asíncronos en un entorno aislado, permitiendo el cálculo de transformadas de Fourier rápidas (FFT) y la re-síntesis de armónicos. No utilizamos simulaciones; cada extracción analiza la fase estéreo y la correlación del audio fuente.',
        'ch2': '2. DESPLIEGUE TÉCNICO E INSTALACIÓN CI/CD',
        'ch2_sub1': 'Pipeline Riguroso',
        'ch2_text1': 'Empleamos un pipeline riguroso (CI/CD) para la aplicación de escritorio, garantizando un despliegue sin fallos y una instalación nativa.',
        'ch2_sub2': 'macOS (Gatekeeper)',
        'ch2_text2': 'Al no contar con un certificado de desarrollador de pago de Apple, Gatekeeper pondrá el binario en cuarentena temporal por seguridad. El método legítimo y certificado por ingenieros para el bypass local es hacer Clic derecho sobre la aplicación -> Abrir (no hagas doble clic directo). No es un fallo ni un archivo corrupto, es el flujo de trabajo estándar en software open-source de alto rendimiento.',
        'ch2_sub3': 'Windows (SmartScreen)',
        'ch2_text3': 'Windows Defender mostrará una pantalla azul indicando "PC protegido". Simplemente haz clic en "Más información" y luego en el botón "Ejecutar de todas formas" que aparecerá.',
        'ch3': '3. FLUJO DE SEÑAL Y RUTEO',
        'ch3_sub1': 'Transparencia Absoluta',
        'ch3_text1': 'Una plataforma profesional de grado estudio debe ofrecer transparencia absoluta sobre sus flujos de datos. La consola no es meramente decorativa.',
        'ch3_sub2': 'Ruteo I/O',
        'ch3_text2': 'En producción de alta densidad, un renderizado pesado en el disco SSD principal puede asfixiar el paginado de memoria del sistema. Alien Box redirige y mapea de forma determinista la caché hacia matrices RAID o unidades NVMe.',
        'ch3_sub3': 'Aislamiento Neuronal 64-bit',
        'ch3_text3': 'Todo el procesamiento interno ocurre en aritmética de punto flotante de 64 bits. Esto previene cualquier degradación o distorsión de fase durante el cálculo cruzado.',
        'ch4': '4. PANEL DE ABDUCCIÓN (INPUT)',
        'ch4_sub1': 'Entrada Universal (URL o Texto)',
        'ch4_text1': 'El sistema admite cualquier URL válida (YouTube, Spotify) o texto libre (ej: "The Prodigy - Poison"). Un módulo de scraping en segundo plano intercepta los metadatos y el flujo de audio en tiempo real, omitiendo las protecciones estándar.',
        'ch4_sub2': 'Selección de Entorno (DAW)',
        'ch4_text2': 'Alien Box compila los datos extraídos en plantillas propietarias estructuradas. Los formatos soportados incluyen: Ableton Live (.als), Logic Pro (.logicx), Cubase (.cpr), FL Studio (.flp) y Pro Tools (.ptx). Se generan buses de grupo y ruteos preconfigurados con plugins nativos.',
        'ch5': '5. MODOS DE EXTRACCIÓN (D1, D2, D3)',
        'ch5_sub1': 'Modo D1 (Ligero)',
        'ch5_text1': 'Análisis de transitorios y generación de MIDI rítmico. Extrae el groove fundamental sin procesar polifonía pesada. Ideal para clonar el swing exacto de un track. Tiempo de ejecución: ~5s.',
        'ch5_sub2': 'Modo D2 (Profundo)',
        'ch5_text2': 'Activa el módulo demucs. Separación en 4 stems (Vocals, Drums, Bass, Other). Extracción de MIDI polifónico a través de basic-pitch, detectando síntesis FM o Wavetable subyacente. Tiempo de ejecución: ~3m.',
        'ch5_sub3': 'Modo D3 (Extremo)',
        'ch5_text3': 'Desglose en 6 stems. Análisis forense de la curva de ecualización y emulaciones específicas de hardware analógico de los ingenieros de mezcla originales.',
        'ch6': '6. DESCODIFICACIÓN FORENSE (CAPA POR CAPA)',
        'ch6_sub1': 'Bombo, Caja y Percusión (Drums)',
        'ch6_text1': '• **Kick:** Se analiza la frecuencia fundamental (ej. 48Hz) y el armónico secundario de pegada (click). Alien Box infiere EQ quirúrgica estilo SSL E-Channel y sugiere un anclaje Mono filtrando el canal Side < 120Hz.\\n• **Snare:** Identifica el Snap de la bordonera (2kHz a 5kHz) y el Cuerpo fundamental (150-250Hz). Propone Transient Shapers.\\n• **Hi-Hats:** Detecta estridencias y automáticamente sugiere De-Essers o compresión multibanda súper rápida.',
        'ch6_sub2': 'Sintetizadores, Guitarras y Percusión Auxiliar',
        'ch6_text2': '• **Congas / Toms:** Mapeo de panorámica estéreo asimétrica (L/R) y ecualización dinámica para eliminar "ringings".\\n• **Synths:** Identificación del corte de filtro (Cutoff) e inyección de Ensanchadores Estéreo basados en el efecto Haas.\\n• **Guitarras:** Identifica el cuerpo de madera o la distorsión del amplificador. Propone recortes estratégicos entre 200-500Hz para limpiar el barro frecuencial.',
        'ch6_sub3': 'Cuerdas, Vientos y Vocales',
        'ch6_text3': '• **Strings/Brass:** Análisis de articulación. Infiere reverberación por convolución tipo "Hall" oscuro o "Chamber".\\n• **Vocales:** Disecciona la cadena vocal líder. Detecta compresión en serie (Ej: Ataque rápido estilo 1176 seguido de nivelación óptica LA-2A) y EQ dinámica activa.',
        'ch7': '7. SUPER PROMPT IA Y GUÍA DE MEZCLA',
        'ch7_sub1': 'Guía de Mezcla y Ruteo',
        'ch7_text1': 'Se reportan técnicas detectadas como Sidechain Compression extremo (Ghost Kick), uso de expansión estéreo (Algoritmo Haas), De-Essing en vocales y distorsión armónica en buses grupales (Tape/Tube saturation).',
        'ch7_sub2': 'Super Prompt IA',
        'ch7_text2': 'Alien Box compila todos estos datos (BPM, Key, LUFS objetivo, Estructura, Instrumentos) en un prompt altamente estructurado, optimizado para alimentar modelos generativos como Suno, Udio o Stable Audio, obligándolos a adherirse a parámetros de mastering profesional.',
        'ch8': '8. TELEMETRÍA Y EMPAQUETADO',
        'ch8_sub1': 'Sensores Alien Bioworks',
        'ch8_text1': 'El icono superior de sensores activa la monitorización del Alien Engine en tiempo real. Permite al ingeniero observar el uso de CPU, la asignación de RAM y los tiempos de latencia durante la extracción profunda en el modo D2/D3.',
        'ch8_sub2': 'Descarga de Plantilla .ZIP',
        'ch8_text2': 'El botón final genera dinámicamente un archivo ZIP en el servidor que contiene:\\n• El archivo de proyecto del DAW seleccionado (.als, .cpr, etc).\\n• La estructura de buses ruteada y etiquetada por colores.\\n• Los archivos MIDI extraídos importados directamente en sus pistas correspondientes.\\n• Una copia en texto plano de la Ficha Técnica para referencia offline.',
        'ch9': '9. ARQUITECTURA MULTIMODAL GLOBAL',
        'ch9_sub1': 'Soporte Estructural 100% Unicode',
        'ch9_text1': 'Tratar la internacionalización de una herramienta corporativa mediante simples archivos JSON de traducción plana es insuficiente. En Alien Box hemos codificado un paradigma Multimodal Estructural de grado A. Esto implica un soporte total del estándar Unicode, permitiendo una recarga en caliente de los diccionarios completos en 7 idiomas nativos.',
        'ch10': '10. BLINDAJE, FAQ Y LICENCIA',
        'ch10_sub1': 'Arquitectura de Blindaje (Shielding)',
        'ch10_text1': '• **Anti-Flood:** Algoritmos estrangulan cualquier pico anómalo de peticiones.\\n• **Magic Bytes:** Certificación de firma binaria cruda para evitar malware inyectado en archivos .mp3.\\n• **Limitador RAM:** Rechazamos archivos atípicos (>2GB) en umbral para prevenir colapsos OOM.',
        'ch10_sub2': 'FAQ Operativo',
        'ch10_text2': '**P:** Puerto 8000 "Address Already In Use".\\n**R:** Ejecuta `lsof -i :8000 -t | xargs kill -9`.\\n**P:** Interbloqueo al subir WAV.\\n**R:** RAM colapsada o firma binaria bloqueada.',
        'ch10_sub3': 'Manifiesto y Licencia',
        'ch10_text3': 'Desarrollado en **produktes-code** por CHUS BZN. Licenciado bajo CC BY-NC-SA 4.0. ESTÁNDAR CORPORATIVO - RETAIL READY.',
    },
    'en': {
        'title': 'Technical Operations Manual',
        'subtitle': 'VERSION 1.0.0 (RELEASE CANDIDATE)',
        'confidential': 'Confidential – DSP Architecture',
        'ch1': '1. SYSTEM ARCHITECTURE',
        'ch1_sub1': 'What is Alien Box?',
        'ch1_text1': 'Alien Box is a forensic audio analysis station based on deep neural networks. Unlike a traditional stem separator, Alien Box uses the Demucs v4 matrix combined with Basic-Pitch transcription algorithms to decode the musical DNA of any commercial track.\\n\\nThe system is designed to operate in the pre-production and studio phase (White Room), offering producers the ability to abduct the spectral signature, dynamic range, and MIDI patterns of complex references, exporting them instantly as native templates for DAW environments.',
        'ch1_sub2': 'Alien Bioworks Engine',
        'ch1_text2': 'The core of the system ("Alien Engine") executes asynchronous processes in an isolated environment, allowing the calculation of Fast Fourier Transforms (FFT) and harmonic re-synthesis. We do not use simulations; each extraction analyzes the stereo phase and correlation of the source audio.',
        'ch2': '2. TECHNICAL DEPLOYMENT AND CI/CD INSTALLATION',
        'ch2_sub1': 'Rigorous Pipeline',
        'ch2_text1': 'We employ a rigorous pipeline (CI/CD) for the desktop application, guaranteeing a flawless deployment and a native installation.',
        'ch2_sub2': 'macOS (Gatekeeper)',
        'ch2_text2': 'Since it lacks a paid Apple developer certificate, Gatekeeper will temporarily quarantine the binary for security. The legitimate and engineer-certified method for local bypass is to Right-click on the application -> Open (do not double-click directly). This is not a bug or a corrupt file, it is the standard workflow in high-performance open-source software.',
        'ch2_sub3': 'Windows (SmartScreen)',
        'ch2_text3': 'Windows Defender will display a blue screen indicating "PC protected". Simply click on "More info" and then on the "Run anyway" button that will appear.',
        'ch3': '3. SIGNAL FLOW AND ROUTING',
        'ch3_sub1': 'Absolute Transparency',
        'ch3_text1': 'A professional studio-grade platform must offer absolute transparency regarding its data flows. The console is not merely decorative.',
        'ch3_sub2': 'I/O Routing',
        'ch3_text2': 'In high-density production, heavy rendering on the main SSD drive can choke the system\'s memory paging. Alien Box deterministically redirects and maps the cache to RAID arrays or NVMe drives.',
        'ch3_sub3': '64-bit Neural Isolation',
        'ch3_text3': 'All internal processing occurs in 64-bit floating-point arithmetic. This prevents any phase degradation or distortion during cross-calculation.',
        'ch4': '4. ABDUCTION PANEL (INPUT)',
        'ch4_sub1': 'Universal Input (URL or Text)',
        'ch4_text1': 'The system accepts any valid URL (YouTube, Spotify) or free text (e.g., "The Prodigy - Poison"). A background scraping module intercepts the metadata and audio stream in real-time, bypassing standard protections.',
        'ch4_sub2': 'Environment Selection (DAW)',
        'ch4_text2': 'Alien Box compiles the extracted data into structured proprietary templates. Supported formats include: Ableton Live (.als), Logic Pro (.logicx), Cubase (.cpr), FL Studio (.flp), and Pro Tools (.ptx). Pre-configured group buses and routings with native plugins are generated.',
        'ch5': '5. EXTRACTION MODES (D1, D2, D3)',
        'ch5_sub1': 'D1 Mode (Lightweight)',
        'ch5_text1': 'Transient analysis and rhythmic MIDI generation. Extracts the fundamental groove without processing heavy polyphony. Ideal for cloning the exact swing of a track. Execution time: ~5s.',
        'ch5_sub2': 'D2 Mode (Deep)',
        'ch5_text2': 'Activates the demucs module. Separation into 4 stems (Vocals, Drums, Bass, Other). Extraction of polyphonic MIDI via basic-pitch, detecting underlying FM or Wavetable synthesis. Execution time: ~3m.',
        'ch5_sub3': 'D3 Mode (Extreme)',
        'ch5_text3': 'Breakdown into 6 stems. Forensic analysis of the equalization curve and specific analog hardware emulations of the original mixing engineers.',
        'ch6': '6. FORENSIC DECODING (LAYER BY LAYER)',
        'ch6_sub1': 'Kick, Snare, and Percussion (Drums)',
        'ch6_text1': '• **Kick:** The fundamental frequency (e.g., 48Hz) and the secondary punch harmonic (click) are analyzed. Alien Box infers surgical EQ SSL E-Channel style and suggests a Mono anchor by filtering the Side channel < 120Hz.\\n• **Snare:** Identifies the Snap of the snare wire (2kHz to 5kHz) and the fundamental Body (150-250Hz). Proposes Transient Shapers.\\n• **Hi-Hats:** Detects harshness and automatically suggests De-Essers or super-fast multiband compression.',
        'ch6_sub2': 'Synthesizers, Guitars, and Aux Percussion',
        'ch6_text2': '• **Congas / Toms:** Asymmetrical stereo panning mapping (L/R) and dynamic equalization to eliminate "ringings".\\n• **Synths:** Identification of the filter cutoff and injection of Stereo Wideners based on the Haas effect.\\n• **Guitars:** Identifies the wooden body or amplifier distortion. Proposes strategic cuts between 200-500Hz to clean up frequency mud.',
        'ch6_sub3': 'Strings, Brass, and Vocals',
        'ch6_text3': '• **Strings/Brass:** Articulation analysis. Infers convolution reverb of the dark "Hall" or "Chamber" type.\\n• **Vocals:** Dissects the lead vocal chain. Detects serial compression (Ex: 1176-style fast attack followed by LA-2A optical leveling) and active dynamic EQ.',
        'ch7': '7. SUPER PROMPT AI AND MIXING GUIDE',
        'ch7_sub1': 'Mixing and Routing Guide',
        'ch7_text1': 'Detected techniques such as extreme Sidechain Compression (Ghost Kick), use of stereo expansion (Haas Algorithm), vocal De-Essing, and harmonic distortion on group buses (Tape/Tube saturation) are reported.',
        'ch7_sub2': 'Super Prompt AI',
        'ch7_text2': 'Alien Box compiles all this data (BPM, Key, target LUFS, Structure, Instruments) into a highly structured prompt, optimized to feed generative models like Suno, Udio, or Stable Audio, forcing them to adhere to professional mastering parameters.',
        'ch8': '8. TELEMETRY AND PACKAGING',
        'ch8_sub1': 'Alien Bioworks Sensors',
        'ch8_text1': 'The top sensors icon activates real-time monitoring of the Alien Engine. It allows the engineer to observe CPU usage, RAM allocation, and latency times during deep extraction in D2/D3 mode.',
        'ch8_sub2': '.ZIP Template Download',
        'ch8_text2': 'The final button dynamically generates a ZIP file on the server containing:\\n• The project file of the selected DAW (.als, .cpr, etc).\\n• The bus structure routed and color-coded.\\n• The extracted MIDI files imported directly into their corresponding tracks.\\n• A plain text copy of the Technical Sheet for offline reference.',
        'ch9': '9. GLOBAL MULTIMODAL ARCHITECTURE',
        'ch9_sub1': '100% Unicode Structural Support',
        'ch9_text1': 'Handling the internationalization of a corporate tool using simple flat translation JSON files is insufficient. In Alien Box, we have coded an A-grade Structural Multimodal paradigm. This implies full support of the Unicode standard, allowing hot-reloading of complete dictionaries in 7 native languages.',
        'ch10': '10. SHIELDING, FAQ AND LICENSE',
        'ch10_sub1': 'Shielding Architecture',
        'ch10_text1': '• **Anti-Flood:** Algorithms throttle any anomalous spike in requests.\\n• **Magic Bytes:** Raw binary signature certification to prevent malware injected into .mp3 files.\\n• **RAM Limiter:** We reject atypical files (>2GB) at the threshold to prevent OOM collapses.',
        'ch10_sub2': 'Operational FAQ',
        'ch10_text2': '**Q:** Port 8000 "Address Already In Use".\\n**A:** Run `lsof -i :8000 -t | xargs kill -9`.\\n**Q:** Deadlock when uploading WAV.\\n**A:** Collapsed RAM or blocked binary signature.',
        'ch10_sub3': 'Manifesto and License',
        'ch10_text3': 'Developed at **produktes-code** by CHUS BZN. Licensed under CC BY-NC-SA 4.0. CORPORATE STANDARD - RETAIL READY.',
    },
    'ru': {
        'title': 'Техническое руководство по эксплуатации',
        'subtitle': 'ВЕРСИЯ 1.0.0 (RELEASE CANDIDATE)',
        'confidential': 'Конфиденциально – DSP Architecture',
        'ch1': '1. АРХИТЕКТУРА СИСТЕМЫ',
        'ch1_sub1': 'Что такое Alien Box?',
        'ch1_text1': 'Alien Box — это станция форензического анализа аудио, основанная на глубоких нейронных сетях. В отличие от традиционного разделителя стемов, Alien Box использует матрицу Demucs v4 в сочетании с алгоритмами транскрипции Basic-Pitch для декодирования музыкальной ДНК любого коммерческого трека.\\n\\nСистема предназначена для работы на этапе предпродакшна и в студии (White Room), предоставляя продюсерам возможность похищать спектральную подпись, динамический диапазон и MIDI-паттерны сложных референсов, мгновенно экспортируя их как нативные шаблоны для сред DAW.',
        'ch1_sub2': 'Движок Alien Bioworks',
        'ch1_text2': 'Ядро системы ("Alien Engine") выполняет асинхронные процессы в изолированной среде, обеспечивая расчет быстрых преобразований Фурье (FFT) и гармонический ресинтез. Мы не используем симуляции; каждое извлечение анализирует стереофазу и корреляцию исходного звука.',
        'ch2': '2. ТЕХНИЧЕСКОЕ РАЗВЕРТЫВАНИЕ И УСТАНОВКА CI/CD',
        'ch2_sub1': 'Строгий конвейер',
        'ch2_text1': 'Мы используем строгий конвейер (CI/CD) для настольного приложения, гарантирующий безошибочное развертывание и нативную установку.',
        'ch2_sub2': 'macOS (Gatekeeper)',
        'ch2_text2': 'Поскольку у него нет платного сертификата разработчика Apple, Gatekeeper временно поместит двоичный файл в карантин в целях безопасности. Законный и сертифицированный инженерами метод локального обхода — щелкнуть правой кнопкой мыши по приложению -> Открыть (не дважды щелкайте). Это не ошибка и не поврежденный файл, это стандартный рабочий процесс в высокопроизводительном ПО с открытым исходным кодом.',
        'ch2_sub3': 'Windows (SmartScreen)',
        'ch2_text3': 'Windows Defender отобразит синий экран с надписью «Защита ПК». Просто нажмите «Подробнее», а затем появившуюся кнопку «Выполнить в любом случае».',
        'ch3': '3. ПОТОК СИГНАЛОВ И МАРШРУТИЗАЦИЯ',
        'ch3_sub1': 'Абсолютная прозрачность',
        'ch3_text1': 'Профессиональная платформа студийного уровня должна обеспечивать абсолютную прозрачность своих потоков данных. Консоль не является просто декоративной.',
        'ch3_sub2': 'Маршрутизация ввода/вывода',
        'ch3_text2': 'При производстве с высокой плотностью тяжелый рендеринг на основном SSD-накопителе может заглушить подкачку памяти системы. Alien Box детерминированно перенаправляет и сопоставляет кеш с RAID-массивами или накопителями NVMe.',
        'ch3_sub3': '64-битная нейронная изоляция',
        'ch3_text3': 'Вся внутренняя обработка происходит в 64-битной арифметике с плавающей запятой. Это предотвращает любую деградацию фазы или искажения во время перекрестных вычислений.',
        'ch4': '4. ПАНЕЛЬ ПОХИЩЕНИЯ (ВВОД)',
        'ch4_sub1': 'Универсальный ввод (URL или текст)',
        'ch4_text1': 'Система принимает любой действительный URL-адрес (YouTube, Spotify) или произвольный текст (например, «The Prodigy - Poison»). Модуль фонового парсинга перехватывает метаданные и аудиопоток в реальном времени в обход стандартных защит.',
        'ch4_sub2': 'Выбор среды (DAW)',
        'ch4_text2': 'Alien Box компилирует извлеченные данные в структурированные проприетарные шаблоны. Поддерживаемые форматы: Ableton Live (.als), Logic Pro (.logicx), Cubase (.cpr), FL Studio (.flp) и Pro Tools (.ptx). Генерируются предварительно настроенные групповые шины и маршрутизации с нативными плагинами.',
        'ch5': '5. РЕЖИМЫ ИЗВЛЕЧЕНИЯ (D1, D2, D3)',
        'ch5_sub1': 'Режим D1 (Легкий)',
        'ch5_text1': 'Анализ транзиентов и генерация ритмического MIDI. Извлекает фундаментальный грув без обработки тяжелой полифонии. Идеально подходит для клонирования точного свинга трека. Время выполнения: ~5с.',
        'ch5_sub2': 'Режим D2 (Глубокий)',
        'ch5_text2': 'Активирует модуль demucs. Разделение на 4 стема (Вокал, Ударные, Бас, Другое). Извлечение полифонического MIDI через basic-pitch, обнаружение базового FM- или волнового синтеза. Время выполнения: ~3м.',
        'ch5_sub3': 'Режим D3 (Экстремальный)',
        'ch5_text3': 'Разбивка на 6 стемов. Форензический анализ кривой эквализации и специфических аппаратных аналоговых эмуляций оригинальных инженеров по микшированию.',
        'ch6': '6. ФОРЕНЗИЧЕСКОЕ ДЕКОДИРОВАНИЕ (СЛОЙ ЗА СЛОЕМ)',
        'ch6_sub1': 'Бочка, малый барабан и перкуссия (Ударные)',
        'ch6_text1': '• **Kick:** Анализируются основная частота (например, 48 Гц) и вторичная гармоника удара (щелчок). Alien Box делает вывод о хирургическом эквалайзере в стиле SSL E-Channel и предлагает моно-якорь, фильтруя боковой канал < 120 Гц.\\n• **Snare:** Идентифицирует щелчок подструнника (от 2 до 5 кГц) и фундаментальное тело (150-250 Гц). Предлагает Transient Shapers.\\n• **Hi-Hats:** Обнаруживает резкость и автоматически предлагает De-Essers или сверхбыструю многополосную компрессию.',
        'ch6_sub2': 'Синтезаторы, гитары и вспомогательная перкуссия',
        'ch6_text2': '• **Congas / Toms:** Асимметричное отображение стереопанорамирования (Л/П) и динамическая эквализация для устранения «звонов».\\n• **Synths:** Определение среза фильтра (Cutoff) и введение расширителей стерео на основе эффекта Хааса.\\n• **Guitars:** Определяет деревянный корпус или искажение усилителя. Предлагает стратегические вырезы между 200-500 Гц для очистки частотной грязи.',
        'ch6_sub3': 'Струнные, духовые и вокал',
        'ch6_text3': '• **Strings/Brass:** Анализ артикуляции. Выводит конволюционную реверберацию темного типа «Hall» или «Chamber».\\n• **Vocals:** Анализирует цепь ведущего вокала. Обнаруживает последовательную компрессию (Например: быстрая атака в стиле 1176 с последующим оптическим выравниванием LA-2A) и активный динамический эквалайзер.',
        'ch7': '7. СУПЕР-ПРОМПТ ИИ И РУКОВОДСТВО ПО МИКШИРОВАНИЮ',
        'ch7_sub1': 'Руководство по микшированию и маршрутизации',
        'ch7_text1': 'Сообщается об обнаруженных методах, таких как экстремальная компрессия Sidechain (Ghost Kick), использование стерео-расширения (алгоритм Хааса), De-Essing вокала и гармонические искажения на групповых шинах (Tape/Tube saturation).',
        'ch7_sub2': 'Супер-промпт ИИ',
        'ch7_text2': 'Alien Box компилирует все эти данные (BPM, тональность, целевые LUFS, структура, инструменты) в строго структурированный промпт, оптимизированный для генеративных моделей (Suno, Udio, Stable Audio), заставляя их придерживаться параметров профессионального мастеринга.',
        'ch8': '8. ТЕЛЕМЕТРИЯ И УПАКОВКА',
        'ch8_sub1': 'Датчики Alien Bioworks',
        'ch8_text1': 'Верхний значок датчиков активирует мониторинг Alien Engine в реальном времени. Позволяет инженеру наблюдать использование ЦП, выделение ОЗУ и задержку во время глубокого извлечения в режиме D2/D3.',
        'ch8_sub2': 'Загрузка шаблона .ZIP',
        'ch8_text2': 'Кнопка динамически генерирует ZIP-файл на сервере, содержащий:\\n• Файл проекта выбранной DAW.\\n• Структуру шин, маршрутизированную и отмеченную цветом.\\n• Извлеченные MIDI-файлы, импортированные прямо на их дорожки.\\n• Текстовую копию технического паспорта.',
        'ch9': '9. ГЛОБАЛЬНАЯ МУЛЬТИМОДАЛЬНАЯ АРХИТЕКТУРА',
        'ch9_sub1': '100% структурная поддержка Unicode',
        'ch9_text1': 'Обработка интернационализации корпоративного инструмента с помощью простых плоских файлов перевода JSON недостаточна. В Alien Box мы закодировали структурную мультимодальную парадигму класса А. Это подразумевает полную поддержку стандарта Unicode, позволяя выполнять горячую перезагрузку полных словарей на 7 языках.',
        'ch10': '10. ЗАЩИТА, FAQ И ЛИЦЕНЗИЯ',
        'ch10_sub1': 'Архитектура защиты (Shielding)',
        'ch10_text1': '• **Anti-Flood:** Алгоритмы ограничивают любой аномальный всплеск запросов.\\n• **Magic Bytes:** Сертификация необработанной двоичной подписи для предотвращения вредоносного ПО.\\n• **Limitador RAM:** Мы отклоняем нетипичные файлы (>2ГБ) для предотвращения краха OOM.',
        'ch10_sub2': 'Оперативный FAQ',
        'ch10_text2': '**В:** Порт 8000 "Address Already In Use".\\n**О:** Выполните `lsof -i :8000 -t | xargs kill -9`.\\n**В:** Взаимная блокировка при загрузке WAV.\\n**О:** Сбой RAM или заблокированная подпись.',
        'ch10_sub3': 'Манифест и лицензия',
        'ch10_text3': 'Разработано в **produktes-code** (CHUS BZN). Лицензия CC BY-NC-SA 4.0. КОРПОРАТИВНЫЙ СТАНДАРТ - RETAIL READY.',
    },
    'uk': { 'title': 'Технічний посібник', 'subtitle': 'ВЕРСІЯ 1.0.0 (RELEASE CANDIDATE)', 'confidential': 'Конфіденційно – DSP Architecture', 'ch1': '1. АРХІТЕКТУРА СИСТЕМИ', 'ch1_sub1': 'Що таке Alien Box?', 'ch1_text1': 'Alien Box — це станція форензичного аналізу аудіо на основі глибоких нейромереж. На відміну від традиційного розділювача стемів, Alien Box використовує матрицю Demucs v4 у поєднанні з алгоритмами транскрипції Basic-Pitch для декодування музичної ДНК будь-якого комерційного треку.\\n\\nСистема розроблена для роботи на етапі пре-продакшну та в студії (White Room), пропонуючи продюсерам можливість вилучати спектральну сигнатуру, динамічний діапазон та MIDI-патерни складних референсів, миттєво експортуючи їх як нативні шаблони для середовищ DAW.', 'ch1_sub2': 'Рушій Alien Bioworks', 'ch1_text2': 'Ядро системи ("Alien Engine") виконує асинхронні процеси в ізольованому середовищі, дозволяючи обчислювати швидкі перетворення Фур\'є (FFT) та гармонійний ресинтез. Ми не використовуємо симуляції; кожне вилучення аналізує стереофазу та кореляцію вихідного звуку.', 'ch2': '2. ТЕХНІЧНЕ РОЗГОРТАННЯ ТА ВСТАНОВЛЕННЯ CI/CD', 'ch2_sub1': 'Суворий конвеєр', 'ch2_text1': 'Ми використовуємо суворий конвеєр (CI/CD) для настільної програми, гарантуючи бездоганне розгортання та нативне встановлення.', 'ch2_sub2': 'macOS (Gatekeeper)', 'ch2_text2': 'Оскільки немає платного сертифіката розробника Apple, Gatekeeper тимчасово помістить двійковий файл у карантин. Законний метод локального обходу — клацнути правою кнопкою миші програму -> Відкрити. Це не помилка, це стандартний робочий процес у ПЗ з відкритим вихідним кодом.', 'ch2_sub3': 'Windows (SmartScreen)', 'ch2_text3': 'Windows Defender відобразить синій екран із написом «ПК захищено». Просто натисніть «Докладніше», а потім кнопку «Виконати в будь-якому випадку».', 'ch3': '3. ПОТІК СИГНАЛІВ ТА МАРШРУТИЗАЦІЯ', 'ch3_sub1': 'Абсолютна прозорість', 'ch3_text1': 'Професійна платформа студійного рівня повинна забезпечувати абсолютну прозорість потоків даних. Консоль не є просто декоративною.', 'ch3_sub2': 'Маршрутизація I/O', 'ch3_text2': 'У високощільних проектах важкий рендеринг на SSD може перевантажити систему. Alien Box перенаправляє кеш на диски RAID або NVMe.', 'ch3_sub3': '64-бітна нейронна ізоляція', 'ch3_text3': 'Уся внутрішня обробка відбувається у 64-бітній арифметиці. Це запобігає будь-якій деградації фази під час перехресних обчислень.', 'ch4': '4. ПАНЕЛЬ ВИТЯГАННЯ (ВВІД)', 'ch4_sub1': 'Універсальний ввід (URL або текст)', 'ch4_text1': 'Система приймає будь-яку URL-адресу (YouTube, Spotify) або вільний текст (наприклад, "The Prodigy - Poison"). Модуль фонового парсингу перехоплює метадані та аудіопотік у реальному часі.', 'ch4_sub2': 'Вибір середовища (DAW)', 'ch4_text2': 'Alien Box компілює дані у структуровані шаблони. Підтримуються форматы: Ableton Live, Logic Pro, Cubase, FL Studio та Pro Tools. Створюються налаштовані групові шини з нативними плагінами.', 'ch5': '5. РЕЖИМИ ВИТЯГАННЯ (D1, D2, D3)', 'ch5_sub1': 'Режим D1 (Легкий)', 'ch5_text1': 'Аналіз транзієнтів і генерація ритмічного MIDI. Вилучає фундаментальний грув без обробки важкої поліфонії. Ідеально підходить для клонування свінгу. Час: ~5с.', 'ch5_sub2': 'Режим D2 (Глибокий)', 'ch5_text2': 'Активує модуль demucs. Розділення на 4 стеми (Вокал, Барабани, Бас, Інше). Вилучення поліфонічного MIDI через basic-pitch. Час: ~3хв.', 'ch5_sub3': 'Режим D3 (Екстремальний)', 'ch5_text3': 'Розбивка на 6 стемів. Форензичний аналіз кривої еквалізації та специфічних апаратних аналогових емуляцій оригінальних інженерів мікшування.', 'ch6': '6. ФОРЕНЗИЧНЕ ДЕКОДУВАННЯ', 'ch6_sub1': 'Барабани та перкусія (Drums)', 'ch6_text1': '• **Kick:** Аналізується основна частота (наприклад, 48 Гц). Пропонує моно-якір, фільтруючи бічний канал < 120 Гц.\\n• **Snare:** Ідентифікує щиголь підструнника. Пропонує Transient Shapers.\\n• **Hi-Hats:** Виявляє різкість і автоматично пропонує De-Essers.', 'ch6_sub2': 'Синтезатори, гітари та перкусія', 'ch6_text2': '• **Congas / Toms:** Асиметричне панорамування (Л/П) та динамічна еквалізація.\\n• **Synths:** Визначення зрізу фільтра та ін\'єкція розширювачів стерео (ефект Хааса).\\n• **Guitars:** Пропонує стратегічні вирізи між 200-500 Гц для очищення бруду.', 'ch6_sub3': 'Струнні, духові та вокал', 'ch6_text3': '• **Strings:** Аналіз артикуляції. Виводить реверберацію типу «Hall».\\n• **Vocals:** Аналізує ланцюг вокалу. Виявляє компресію (1176 -> LA-2A) та активний динамічний еквалайзер.', 'ch7': '7. СУПЕР-ПРОМПТ ІІ', 'ch7_sub1': 'Посібник з мікшування', 'ch7_text1': 'Повідомляється про виявлені методи, такі як Sidechain Compression, алгоритм Хааса, De-Essing вокалу та гармонійні спотворення (Tape saturation).', 'ch7_sub2': 'Супер-промпт', 'ch7_text2': 'Alien Box компілює ці дані (BPM, тональність, LUFS) у структурований промпт для моделей (Suno, Udio), змушуючи їх дотримуватися параметрів професійного мастерингу.', 'ch8': '8. ТЕЛЕМЕТРІЯ ТА ПАКУВАННЯ', 'ch8_sub1': 'Датчики Alien Bioworks', 'ch8_text1': 'Значок датчиків активує моніторинг Alien Engine. Дозволяє спостерігати використання ЦП та ОЗП під час вилучення.', 'ch8_sub2': 'Завантаження .ZIP', 'ch8_text2': 'Кнопка генерує ZIP-файл, що містить проект DAW, структуру шин, MIDI-файли та копію технічного паспорта.', 'ch9': '9. МУЛЬТИМОДАЛЬНА АРХІТЕКТУРА', 'ch9_sub1': '100% структурна підтримка Unicode', 'ch9_text1': 'У Alien Box ми закодували структурну мультимодальну парадигму класу А. Це означає повну підтримку стандарту Unicode, що дозволяє перезавантажувати повні словники на 7 мовах.', 'ch10': '10. ЗАХИСТ, FAQ ТА ЛІЦЕНЗІЯ', 'ch10_sub1': 'Архітектура захисту', 'ch10_text1': '• **Anti-Flood:** Алгоритми обмежують аномальні запити.\\n• **Magic Bytes:** Сертифікація підпису для запобігання зловмисному ПЗ.', 'ch10_sub2': 'Оперативний FAQ', 'ch10_text2': '**П:** Порт 8000 зайнятий.\\n**В:** Виконайте `lsof -i :8000 -t | xargs kill -9`.', 'ch10_sub3': 'Ліцензія', 'ch10_text3': 'Розроблено **produktes-code** (CHUS BZN). CC BY-NC-SA 4.0. КОРПОРАТИВНИЙ СТАНДАРТ.' },
    'zh': { 'title': '技术操作手册', 'subtitle': '版本 1.0.0 (RELEASE CANDIDATE)', 'confidential': '机密 – DSP 架构', 'ch1': '1. 系统架构', 'ch1_sub1': 'Alien Box 是什么？', 'ch1_text1': 'Alien Box 是一款基于深度神经网络的法医音频分析工作站。与传统的音轨分离器不同，Alien Box 使用 Demucs v4 矩阵结合 Basic-Pitch 转录算法来解码任何商业曲目的音乐 DNA。\\n\\n该系统旨在制作前阶段和工作室 (White Room) 运行，让制作人能够提取复杂参考音轨的频谱特征、动态范围和 MIDI 模式，并将它们立即导出为 DAW 环境的本地模板。', 'ch1_sub2': 'Alien Bioworks 引擎', 'ch1_text2': '系统的核心（“Alien Engine”）在隔离环境中执行异步过程，允许计算快速傅里叶变换 (FFT) 和谐波重新合成。我们不使用模拟；每次提取都会分析源音频的立体声相位和相关性。', 'ch2': '2. 技术部署和 CI/CD 安装', 'ch2_sub1': '严格的流水线', 'ch2_text1': '我们对桌面应用程序采用了严格的 CI/CD 流水线，保证了无故障部署和本地安装。', 'ch2_sub2': 'macOS (Gatekeeper)', 'ch2_text2': '由于没有付费的 Apple 开发者证书，Gatekeeper 出于安全考虑会暂时隔离该二进制文件。工程师认证的本地绕过方法是右键单击应用程序 -> 打开（不要直接双击）。这不是错误或损坏的文件，这是高性能开源软件的标准工作流程。', 'ch2_sub3': 'Windows (SmartScreen)', 'ch2_text3': 'Windows Defender 将显示蓝屏，提示“Windows 已保护你的电脑”。只需单击“更多信息”，然后单击出现的“仍要运行”按钮。', 'ch3': '3. 信号流和路由', 'ch3_sub1': '绝对透明度', 'ch3_text1': '专业工作室级平台必须确保其数据流的绝对透明度。控制台不仅是装饰性的。', 'ch3_sub2': 'I/O 路由', 'ch3_text2': '在高密度制作中，主 SSD 上的繁重渲染可能会阻塞系统的内存分页。Alien Box 确定性地将缓存重定向并映射到 RAID 阵列或 NVMe 驱动器。', 'ch3_sub3': '64 位隔离', 'ch3_text3': '所有内部处理均在 64 位浮点算术中发生。这可防止在交叉计算期间发生任何相位降级或失真。', 'ch4': '4. 提取面板 (输入)', 'ch4_sub1': '通用输入 (URL 或文本)', 'ch4_text1': '该系统接受任何有效的 URL（YouTube、Spotify）或自由文本（例如“The Prodigy - Poison”）。后台抓取模块实时拦截元数据和音频流，绕过标准保护。', 'ch4_sub2': '环境选择 (DAW)', 'ch4_text2': 'Alien Box 将提取的数据编译为结构化的专有模板。支持的格式包括：Ableton Live、Logic Pro、Cubase、FL Studio 和 Pro Tools。使用本机插件生成预配置的组总线和路由。', 'ch5': '5. 提取模式 (D1, D2, D3)', 'ch5_sub1': '模式 D1 (轻量级)', 'ch5_text1': '瞬态分析和节奏 MIDI 生成。提取基本律动而无需处理繁重的复音。非常适合克隆曲目的确切摆动。执行时间：~5秒。', 'ch5_sub2': '模式 D2 (深度)', 'ch5_text2': '激活 demucs 模块。分离为 4 个音轨（人声、鼓、贝斯、其他）。通过 basic-pitch 提取复音 MIDI，检测底层的 FM 或波表合成。执行时间：~3分钟。', 'ch5_sub3': '模式 D3 (极端)', 'ch5_text3': '分解为 6 个音轨。原始混音工程师的均衡曲线和特定硬件模拟的法医分析。', 'ch6': '6. 法医解码', 'ch6_sub1': '底鼓，军鼓和打击乐', 'ch6_text1': '• **Kick:** 分析基频（如 48Hz）和二次打击谐波。推断 SSL E-Channel 风格的 EQ。\\n• **Snare:** 识别军鼓的 Snap (2kHz-5kHz)。\\n• **Hi-Hats:** 检测刺耳声并建议使用 De-Essers。', 'ch6_sub2': '合成器和吉他', 'ch6_text2': '• **Congas:** 动态均衡以消除铃声。\\n• **Synths:** 识别滤波器截止频率并基于哈斯效应注入立体声宽度器。\\n• **Guitars:** 建议在 200-500Hz 之间进行战略性削减。', 'ch6_sub3': '弦乐和人声', 'ch6_text3': '• **Strings:** 发音分析。推断卷积混响。\\n• **Vocals:** 剖析主唱链。检测串行压缩 (1176 -> LA-2A) 和动态 EQ。', 'ch7': '7. AI 超级提示和混音指南', 'ch7_sub1': '混音和路由指南', 'ch7_text1': '报告检测到的技术，例如极端的侧链压缩、哈斯算法、人声 De-Essing 和组总线上的谐波失真。', 'ch7_sub2': '超级提示词', 'ch7_text2': '将所有这些数据（BPM，目标 LUFS，结构）编译成结构化的提示，针对 Suno 或 Udio 等生成模型进行了优化。', 'ch8': '8. 遥测和打包', 'ch8_sub1': '传感器', 'ch8_text1': '实时监控 Alien Engine。观察 CPU 使用率，RAM 分配和延迟时间。', 'ch8_sub2': '下载 .ZIP', 'ch8_text2': '动态生成包含 DAW 项目文件，MIDI 和技术数据表的 ZIP 文件。', 'ch9': '9. 全局多模态架构', 'ch9_sub1': '100% Unicode 支持', 'ch9_text1': '在 Alien Box 中，我们编码了 A 级结构化多模态范式。这允许以 7 种母语热重载完整的字典。', 'ch10': '10. 安全，常见问题和许可证', 'ch10_sub1': '防洪限制', 'ch10_text1': '• **Anti-Flood:** 算法限制任何异常的请求高峰。\\n• **Magic Bytes:** 原始二进制签名认证，以防止恶意软件。', 'ch10_sub2': '操作常见问题', 'ch10_text2': '**问:** 端口 8000 已被占用。\\n**答:** 运行 `lsof -i :8000 -t | xargs kill -9`。', 'ch10_sub3': '宣言和许可证', 'ch10_text3': '由 **produktes-code** 开发。根据 CC BY-NC-SA 4.0 许可。企业标准。' },
    'ja': { 'title': '技術・操作マニュアル', 'subtitle': 'バージョン 1.0.0 (RELEASE CANDIDATE)', 'confidential': '機密 – DSP Architecture', 'ch1': '1. システムアーキテクチャ', 'ch1_sub1': 'Alien Box とは？', 'ch1_text1': 'Alien Boxは、深層ニューラルネットワークに基づく法医学的オーディオ分析ステーションです。従来のステム分離器とは異なり、Demucs v4マトリックスとBasic-Pitch転写アルゴリズムを組み合わせて、商用トラックの音楽DNAをデコードします。\\n\\nシステムはプレプロダクションおよびスタジオフェーズで動作するように設計されており、複雑なリファレンスのスペクトルシグネチャ、ダイナミックレンジ、およびMIDIパターンを抽出し、DAW環境用のネイティブテンプレートとして瞬時にエクスポートします。', 'ch1_sub2': 'Alien Bioworks エンジン', 'ch1_text2': 'システムのコアは、分離された環境で非同期プロセスを実行し、高速フーリエ変換（FFT）と高調波再合成の計算を可能にします。シミュレーションは使用しません。各抽出は、ソースオーディオのステレオ位相と相関を分析します。', 'ch2': '2. デプロイとCI/CDのインストール', 'ch2_sub1': '厳格なパイプライン', 'ch2_text1': 'デスクトップアプリケーションに厳格なパイプライン（CI/CD）を採用し、完璧なデプロイメントとネイティブインストールを保証します。', 'ch2_sub2': 'macOS (Gatekeeper)', 'ch2_text2': '有料のApple開発者証明書がないため、Gatekeeperはセキュリティのためにバイナリを一時的に隔離します。ローカルバイパスの正当な方法は、アプリケーションを右クリックして[開く]を選択することです。これはオープンソースソフトウェアの標準的なワークフローです。', 'ch2_sub3': 'Windows (SmartScreen)', 'ch2_text3': 'Windows Defenderは、「WindowsによってPCが保護されました」という青い画面を表示します。「詳細情報」をクリックしてから、「実行」ボタンをクリックするだけです。', 'ch3': '3. 信号の流れとルーティング', 'ch3_sub1': '絶対的な透明性', 'ch3_text1': 'プロフェッショナルなスタジオグレードのプラットフォームは、データフローの絶対的な透明性を提供する必要があります。', 'ch3_sub2': 'I/O ルーティング', 'ch3_text2': '高密度の制作では、メインSSDドライブでの重いレンダリングがシステムのメモリページングを窒息させる可能性があります。Alien Boxは、キャッシュをRAIDアレイまたはNVMeドライブにリダイレクトします。', 'ch3_sub3': '64ビットの神経分離', 'ch3_text3': 'すべての内部処理は、64ビットの浮動小数点演算で行われます。これにより、クロス計算中の位相の低下や歪みが防止されます。', 'ch4': '4. 抽出パネル (入力)', 'ch4_sub1': 'ユニバーサル入力 (URL またはテキスト)', 'ch4_text1': 'システムは、有効なURL（YouTube、Spotify）またはフリーテキスト（例：「The Prodigy-Poison」）を受け入れます。バックグラウンドスクレイピングモジュールは、標準の保護をバイパスして、メタデータとオーディオストリームをリアルタイムで傍受します。', 'ch4_sub2': '環境の選択 (DAW)', 'ch4_text2': 'Alien Boxは、抽出されたデータを構造化された独自のテンプレートにコンパイルします。サポートされているフォーマット：Ableton Live、Logic Pro、Cubase、FL Studio、Pro Tools。', 'ch5': '5. 抽出モード (D1, D2, D3)', 'ch5_sub1': 'D1 モード (軽量)', 'ch5_text1': 'トランジェント分析とリズミカルなMIDI生成。重いポリフォニーを処理せずに基本的なグルーブを抽出します。実行時間：約5秒。', 'ch5_sub2': 'D2 モード (詳細)', 'ch5_text2': 'demucsモジュールをアクティブにします。4つのステム（ボーカル、ドラム、ベース、その他）への分離。実行時間：約3分。', 'ch5_sub3': 'D3 モード (極端)', 'ch5_text3': '6つのステムへの内訳。元のミキシングエンジニアの等化曲線と特定のハードウェアアナログエミュレーションの法医学的分析。', 'ch6': '6. 法医学的デコード', 'ch6_sub1': 'キックとスネア', 'ch6_text1': '• **Kick:** 基本周波数（例：48Hz）と二次パンチ高調波を分析します。\\n• **Snare:** スネアワイヤーのスナップを識別します。\\n• **Hi-Hats:** ハーシュネスを検出し、De-Esserを推奨します。', 'ch6_sub2': 'シンセとギター', 'ch6_text2': '• **Synths:** フィルターカットオフの識別とハース効果に基づくステレオワイドナーの注入。\\n• **Guitars:** 200〜500Hzの戦略的カットを提案して、泥をきれいにします。', 'ch6_sub3': 'ストリングスとボーカル', 'ch6_text3': '• **Vocals:** リードボーカルチェーンを解剖します。シリアル圧縮（例：1176の後のLA-2A）と動的EQを検出します。', 'ch7': '7. AI スーパープロンプト', 'ch7_sub1': 'ミキシングガイド', 'ch7_text1': 'ゴーストキック、ハースアルゴリズム、テープサチュレーションなどの検出された手法が報告されます。', 'ch7_sub2': 'プロンプト', 'ch7_text2': 'Alien Boxは、これらのすべてのデータ（BPM、キー、ターゲットLUFS）を構造化されたプロンプトにコンパイルし、Sunoなどの生成モデルをフィードバックします。', 'ch8': '8. テレメトリーとパッケージ', 'ch8_sub1': 'センサー', 'ch8_text1': 'Alien Engineのリアルタイム監視。CPU使用率とRAM割り当てを観察します。', 'ch8_sub2': '.ZIP のダウンロード', 'ch8_text2': 'DAWプロジェクトファイル、MIDI、およびテクニカルシートのコピーを含むZIPファイルをサーバー上に動的に生成します。', 'ch9': '9. グローバルなマルチモーダル', 'ch9_sub1': '100% Unicode サポート', 'ch9_text1': 'Alien Boxでは、Aグレードの構造化マルチモーダルパラダイムをコーディングしました。7つの言語での辞書のホットリロードが可能です。', 'ch10': '10. 保護とライセンス', 'ch10_sub1': 'シールドアーキテクチャ', 'ch10_text1': '• **Anti-Flood:** リクエストの異常なスパイクを抑制します。\\n• **Magic Bytes:** マルウェアを防ぐための生のバイナリ署名。', 'ch10_sub2': 'FAQ', 'ch10_text2': '**Q:** ポート8000が使用中。\\n**A:** `lsof -i :8000 -t | xargs kill -9` を実行します。', 'ch10_sub3': 'ライセンス', 'ch10_text3': '**produktes-code** 開発。CC BY-NC-SA 4.0のライセンス。コーポレートスタンダード。' },
    'de': { 'title': 'Technisches Handbuch', 'subtitle': 'VERSION 1.0.0 (RELEASE CANDIDATE)', 'confidential': 'Vertraulich – DSP Architecture', 'ch1': '1. SYSTEMARCHITEKTUR', 'ch1_sub1': 'Was ist Alien Box?', 'ch1_text1': 'Alien Box ist eine forensische Audioanalysestation, die auf tiefen neuronalen Netzen basiert. Im Gegensatz zu herkömmlichen Stem-Separatoren verwendet Alien Box die Demucs v4-Matrix in Kombination mit Basic-Pitch-Transkriptionsalgorithmen, um die musikalische DNA jedes kommerziellen Tracks zu decodieren.\\n\\nDas System ist für den Betrieb in der Vorproduktions- und Studio-Phase konzipiert und bietet Produzenten die Möglichkeit, die spektrale Signatur, den Dynamikbereich und die MIDI-Muster komplexer Referenzen zu extrahieren und sofort als native Templates für DAW-Umgebungen zu exportieren.', 'ch1_sub2': 'Alien Bioworks Engine', 'ch1_text2': 'Der Kern des Systems ("Alien Engine") führt asynchrone Prozesse in einer isolierten Umgebung aus und ermöglicht so die Berechnung schneller Fourier-Transformationen (FFT) und die harmonische Resynthese. Wir verwenden keine Simulationen; jede Extraktion analysiert die Stereophase und Korrelation des Quellaudios.', 'ch2': '2. TECHNISCHE BEREITSTELLUNG', 'ch2_sub1': 'Strenge Pipeline', 'ch2_text1': 'Wir verwenden eine strenge CI/CD-Pipeline für die Desktop-Anwendung, die eine fehlerfreie Bereitstellung garantiert.', 'ch2_sub2': 'macOS (Gatekeeper)', 'ch2_text2': 'Da es kein kostenpflichtiges Apple-Zertifikat hat, wird Gatekeeper die Binärdatei aus Sicherheitsgründen vorübergehend unter Quarantäne stellen. Rechtsklick auf die App -> Öffnen.', 'ch2_sub3': 'Windows (SmartScreen)', 'ch2_text3': 'Windows Defender zeigt einen blauen Bildschirm an. Klicken Sie auf "Weitere Informationen" und dann auf "Trotzdem ausführen".', 'ch3': '3. SIGNALFLUSS UND ROUTING', 'ch3_sub1': 'Absolute Transparenz', 'ch3_text1': 'Eine professionelle Plattform muss absolute Transparenz über ihre Datenflüsse bieten.', 'ch3_sub2': 'I/O Routing', 'ch3_text2': 'Alien Box leitet den Cache deterministisch an RAID-Arrays oder NVMe-Laufwerke weiter.', 'ch3_sub3': '64-Bit-Isolierung', 'ch3_text3': 'Die gesamte interne Verarbeitung erfolgt in 64-Bit-Gleitkomma-Arithmetik. Dies verhindert jede Phasenverschlechterung während der Kreuzberechnung.', 'ch4': '4. EINGABE-PANEL (INPUT)', 'ch4_sub1': 'Universelle Eingabe', 'ch4_text1': 'Das System akzeptiert jede URL oder Freitext. Ein Hintergrund-Scraping-Modul fängt die Metadaten in Echtzeit ab.', 'ch4_sub2': 'Umgebungsauswahl (DAW)', 'ch4_text2': 'Alien Box kompiliert die extrahierten Daten. Unterstützte Formate: Ableton, Logic, Cubase, FL Studio, Pro Tools.', 'ch5': '5. EXTRAKTIONSMODI', 'ch5_sub1': 'Modus D1 (Leicht)', 'ch5_text1': 'Transientenanalyse und rhythmische MIDI-Generierung. Ideal zum Klonen des genauen Swings. Ausführungszeit: ~5s.', 'ch5_sub2': 'Modus D2 (Tief)', 'ch5_text2': 'Trennung in 4 Stems und polyphone MIDI-Extraktion über Basic-Pitch. Ausführungszeit: ~3m.', 'ch5_sub3': 'Modus D3 (Extrem)', 'ch5_text3': 'Aufschlüsselung in 6 Stems. Forensische Analyse der Equalizer-Kurve und Hardware-Emulationen.', 'ch6': '6. FORENSISCHE DEKODIERUNG', 'ch6_sub1': 'Kick und Snare', 'ch6_text1': '• **Kick:** Analysiert die Grundfrequenz und den sekundären Punch. Schlägt Mono-Verankerung vor.\\n• **Snare:** Identifiziert den Snap. Schlägt Transient Shapers vor.', 'ch6_sub2': 'Synths und Gitarren', 'ch6_text2': '• **Synths:** Identifizierung des Filter-Cutoffs und Injektion von Stereo-Wideners (Haas-Effekt).\\n• **Guitars:** Schlägt Kürzungen zwischen 200-500 Hz vor, um Frequenzschlamm zu bereinigen.', 'ch6_sub3': 'Streicher und Gesang', 'ch6_text3': '• **Vocals:** Seziert die Lead-Vocal-Chain. Erkennt serielle Kompression (z.B. 1176 -> LA-2A).', 'ch7': '7. SUPER PROMPT AI', 'ch7_sub1': 'Mischhandbuch', 'ch7_text1': 'Extremes Sidechain-Compression, Haas-Algorithmus und Tape-Sättigung werden gemeldet.', 'ch7_sub2': 'Prompt', 'ch7_text2': 'Alien Box kompiliert alle diese Daten (BPM, Key, LUFS) in einen strukturierten Prompt für Modelle wie Suno oder Udio.', 'ch8': '8. TELEMETRIE UND VERPACKUNG', 'ch8_sub1': 'Sensoren', 'ch8_text1': 'Echtzeit-Überwachung der Alien Engine (CPU, RAM).', 'ch8_sub2': '.ZIP Download', 'ch8_text2': 'Generiert eine ZIP-Datei mit DAW-Projekt, MIDI-Dateien und einer Kopie des technischen Datenblatts.', 'ch9': '9. MULTIMODALE ARCHITEKTUR', 'ch9_sub1': '100% Unicode', 'ch9_text1': 'Wir haben ein strukturelles multimodales Paradigma codiert. Dies ermöglicht das Hot-Reloading von Wörterbüchern in 7 Muttersprachen.', 'ch10': '10. SCHUTZ UND LIZENZ', 'ch10_sub1': 'Abschirmung', 'ch10_text1': '• **Anti-Flood:** Begrenzt anomale Anfragen.\\n• **Magic Bytes:** Zertifizierung der rohen Binärsignatur.', 'ch10_sub2': 'FAQ', 'ch10_text2': '**F:** Port 8000 belegt. \\n**A:** `lsof -i :8000 -t | xargs kill -9` ausführen.', 'ch10_sub3': 'Lizenz', 'ch10_text3': 'Entwickelt bei **produktes-code**. Lizenziert unter CC BY-NC-SA 4.0. CORPORATE STANDARD.' }
}

def format_text(text):
    text = text.replace('\\n\\n', '</p><p style="margin-top: 4px; color: #bacbb9; font-size: 11.5px; line-height: 1.4;">')
    text = text.replace('\\n', '<br>')
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #ffffff; font-weight: 700;">\1</strong>', text)
    text = re.sub(r'`(.*?)`', r'<code style="font-family: monospace; color: #75ff9e; font-size: 10.5px;">\1</code>', text)
    return f'<p style="margin-top: 4px; color: #bacbb9; font-size: 11.5px; line-height: 1.4;">{text}</p>'

html_header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"/>
    <style>
        * { box-sizing: border-box; }
        body, html {
            background-color: #0b0e14;
            color: #bacbb9;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        .a4-page {
            width: 100%;
            height: 100vh; 
            padding: 10mm 15mm; 
            display: flex;
            flex-direction: column;
            justify-content: space-between; /* Distribución uniforme para tamaños idénticos */
            page-break-after: always;
            page-break-inside: avoid;
            background-color: #0b0e14;
            overflow: hidden;
        }

        .chapter-container {
            flex: 1; /* Esto hace que todos los capítulos se expandan para ocupar el mismo espacio en todas las páginas y todos los idiomas, haciéndolos físicamente idénticos */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .chapter-title {
            color: #75ff9e;
            font-size: 16px; 
            font-weight: 700;
            font-family: 'Space Grotesk', sans-serif;
            border-bottom: 2px solid #1f382a;
            padding-bottom: 4px;
            margin-bottom: 8px;
            margin-top: 8px; 
            text-transform: uppercase;
            flex-shrink: 0;
        }

        .glass-panel {
            background-color: #12161b;
            border: 1px solid #1f252d;
            border-radius: 8px;
            padding: 10px 14px; 
            margin-bottom: 8px;
            flex-shrink: 0;
        }

        .panel-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 14px; 
            font-weight: 700;
            margin-top: 0;
            margin-bottom: 4px;
        }
        .panel-title.green { color: #75ff9e; }
        .panel-title.purple { color: #e7b4ff; }
        .panel-title.white { color: #ffffff; }
        .panel-title.orange { color: #ffb86c; }

        .two-cols {
            display: flex;
            gap: 10px; 
            margin-bottom: 8px;
            flex-shrink: 0;
            align-items: center;
        }
        .col-left { flex: 1; }
        .col-right {
            width: 100px; 
            background-color: #12161b;
            border: 1px solid #1f252d;
            border-radius: 8px;
            padding: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .cover-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            height: 100%;
        }
        
        .logo-img {
            width: 280px;
            height: 280px;
            object-fit: contain;
            margin-bottom: 20px;
            filter: drop-shadow(0 0 40px rgba(117, 255, 158, 0.5));
        }
        
        .cover-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 60px;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            text-shadow: 0 0 25px rgba(117, 255, 158, 0.6);
            letter-spacing: -0.02em;
        }
        
        .cover-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 22px;
            color: #75ff9e;
            margin-top: 12px;
            font-weight: 500;
        }

        .cover-box {
            background-color: #12161b;
            border: 1px solid #1f252d;
            border-radius: 12px;
            padding: 18px 25px;
            margin-top: 40px;
            text-align: center;
            width: 90%;
            max-width: 450px;
        }

        .cover-box-version {
            color: #bacbb9;
            font-size: 14px;
            letter-spacing: 0.1em;
            margin-bottom: 8px;
        }
        
        .cover-box-dev {
            color: #7e8b8c;
            font-size: 12px;
            margin-bottom: 10px;
        }

        .cover-box-conf {
            color: #2b5d43;
            font-size: 11px;
            font-family: monospace;
        }
    </style>
</head>
<body>
"""

html_body = ""

for lang in langs:
    c = content[lang]
        
    html_body += f"""
    <!-- PORTADA -->
    <div class="a4-page">
        <div class="cover-content">
            <img src="file:///Users/jesusferrer/Desktop/stitch_alien_box_music_interface/alien_imagotype/screen.png" alt="Logo" class="logo-img">
            <h1 class="cover-title">ALIEN BOX</h1>
            <div class="cover-subtitle">{c['title']}</div>
            
            <div class="cover-box">
                <div class="cover-box-version">{c['subtitle']}</div>
                <div class="cover-box-dev">Desarrollado por CHUS BZN & Alien Bioworks</div>
                <div class="cover-box-conf">{c['confidential']} | LANG: {lang.upper()}</div>
            </div>
        </div>
    </div>

    <!-- PÁGINA 1: CAPÍTULOS 1, 2, 3 -->
    <div class="a4-page">
        <div class="chapter-container">
            <div class="chapter-title" style="margin-top:0;">{c['ch1']}</div>
            <div class="two-cols">
                <div class="col-left">
                    <div class="panel-title white">{c['ch1_sub1']}</div>
                    {format_text(c['ch1_text1'])}
                </div>
                <div class="col-right">
                    <div style="width:60px;height:60px;border:2px solid #75ff9e;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-direction:column;box-shadow:inset 0 0 12px rgba(117,255,158,0.2);">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#75ff9e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                        <div style="color:#75ff9e;font-size:6px;margin-top:4px;font-weight:700;letter-spacing:1px;">ASTROVOLT</div>
                    </div>
                </div>
            </div>
            <div class="glass-panel">
                <h2 class="panel-title purple">{c['ch1_sub2']}</h2>
                {format_text(c['ch1_text2'])}
            </div>
        </div>
        
        <div class="chapter-container">
            <div class="chapter-title">{c['ch2']}</div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch2_sub1']}</h2>
                {format_text(c['ch2_text1'])}
            </div>
            <div class="two-cols">
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title white">{c['ch2_sub2']}</h2>
                    {format_text(c['ch2_text2'])}
                </div>
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title white">{c['ch2_sub3']}</h2>
                    {format_text(c['ch2_text3'])}
                </div>
            </div>
        </div>

        <div class="chapter-container">
            <div class="chapter-title">{c['ch3']}</div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch3_sub1']}</h2>
                {format_text(c['ch3_text1'])}
            </div>
            <div class="two-cols" style="margin-bottom:0;">
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch3_sub2']}</h2>
                    {format_text(c['ch3_text2'])}
                </div>
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch3_sub3']}</h2>
                    {format_text(c['ch3_text3'])}
                </div>
            </div>
        </div>
    </div>

    <!-- PÁGINA 2: CAPÍTULOS 4, 5, 6 -->
    <div class="a4-page">
        <div class="chapter-container">
            <div class="chapter-title" style="margin-top:0;">{c['ch4']}</div>
            <div class="glass-panel">
                <h2 class="panel-title white">{c['ch4_sub1']}</h2>
                {format_text(c['ch4_text1'])}
            </div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch4_sub2']}</h2>
                {format_text(c['ch4_text2'])}
            </div>
        </div>

        <div class="chapter-container">
            <div class="chapter-title">{c['ch5']}</div>
            <div class="two-cols" style="gap:8px;">
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch5_sub1']}</h2>
                    {format_text(c['ch5_text1'])}
                </div>
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch5_sub2']}</h2>
                    {format_text(c['ch5_text2'])}
                </div>
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch5_sub3']}</h2>
                    {format_text(c['ch5_text3'])}
                </div>
            </div>
        </div>
        
        <div class="chapter-container">
            <div class="chapter-title">{c['ch6']}</div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch6_sub1']}</h2>
                {format_text(c['ch6_text1'])}
            </div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch6_sub2']}</h2>
                {format_text(c['ch6_text2'])}
            </div>
            <div class="glass-panel" style="margin-bottom:0;">
                <h2 class="panel-title white">{c['ch6_sub3']}</h2>
                {format_text(c['ch6_text3'])}
            </div>
        </div>
    </div>

    <!-- PÁGINA 3: CAPÍTULOS 7, 8, 9, 10 -->
    <div class="a4-page">
        <div class="chapter-container">
            <div class="chapter-title" style="margin-top:0;">{c['ch7']}</div>
            <div class="glass-panel">
                <h2 class="panel-title orange">{c['ch7_sub1']}</h2>
                {format_text(c['ch7_text1'])}
            </div>
            <div class="glass-panel">
                <h2 class="panel-title orange">{c['ch7_sub2']}</h2>
                {format_text(c['ch7_text2'])}
            </div>
        </div>
        
        <div class="chapter-container">
            <div class="chapter-title">{c['ch8']}</div>
            <div class="glass-panel">
                <h2 class="panel-title white">{c['ch8_sub1']}</h2>
                {format_text(c['ch8_text1'])}
            </div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch8_sub2']}</h2>
                {format_text(c['ch8_text2'])}
            </div>
        </div>

        <div class="chapter-container">
            <div class="chapter-title">{c['ch9']}</div>
            <div class="glass-panel">
                <h2 class="panel-title green">{c['ch9_sub1']}</h2>
                {format_text(c['ch9_text1'])}
            </div>
        </div>
        
        <div class="chapter-container">
            <div class="chapter-title">{c['ch10']}</div>
            <div class="two-cols" style="margin-bottom:0;">
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch10_sub1']}</h2>
                    {format_text(c['ch10_text1'])}
                </div>
                <div class="glass-panel" style="flex:1; margin-bottom:0;">
                    <h2 class="panel-title purple">{c['ch10_sub2']}</h2>
                    {format_text(c['ch10_text2'])}
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 12px; font-family: monospace; font-size: 9px; color: #5a6668; text-transform: uppercase;">
                ALIEN BIOWORKS 2026 // {c['ch10_sub3']}<br>
                {c['ch10_text3']}
            </div>
        </div>
    </div>
    """

html_footer = """
</body>
</html>
"""

with open("manual_multilingual_v14.html", "w", encoding="utf-8") as f:
    f.write(html_header + html_body + html_footer)

print("Archivo HTML V14 generado (Full Translations, flex-grow para tamaños idénticos).")
