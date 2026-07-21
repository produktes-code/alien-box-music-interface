const puppeteer = require('puppeteer');
const path = require('path');

const translations = {
    'es': { 
        t1: 'ABDUCCIÓN DE PISTAS', t2: 'Preparar Secuencia', t3: 'INICIAR SECUENCIA',
        r1: 'Extracción Completada', r2: 'Ficha Técnica Forense'
    },
    'en': { 
        t1: 'TRACK ABDUCTION', t2: 'Prepare Sequence', t3: 'INITIATE SEQUENCE',
        r1: 'Extraction Completed', r2: 'Forensic Technical File'
    },
    'ru': { 
        t1: 'АБДУКЦИЯ ТРЕКОВ', t2: 'Подготовить последовательность', t3: 'ЗАПУСТИТЬ',
        r1: 'Извлечение завершено', r2: 'Технический файл'
    },
    'uk': { 
        t1: 'АБДУКЦІЯ ТРЕКІВ', t2: 'Підготувати послідовність', t3: 'ЗАПУСТИТИ',
        r1: 'Вилучення завершено', r2: 'Технічний файл'
    },
    'zh': { 
        t1: '轨道劫持', t2: '准备序列', t3: '启动序列',
        r1: '提取完成', r2: '取证技术文件'
    },
    'ja': { 
        t1: 'トラックアブダクション', t2: 'シーケンスの準備', t3: 'シーケンス開始',
        r1: '抽出完了', r2: '法医学的テクニカルファイル'
    },
    'de': { 
        t1: 'TRACK-ENTFÜHRUNG', t2: 'Sequenz vorbereiten', t3: 'SEQUENZ STARTEN',
        r1: 'Extraktion Abgeschlossen', r2: 'Forensische technische Datei'
    }
};

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    // Resolucion generosa para no morder cosas
    await page.setViewport({ width: 1400, height: 900, deviceScaleFactor: 2 });
    
    const inputUrl = `file://${path.join(__dirname, 'input_screen_organic_v4_final_2', 'code.html')}`;
    const resultsUrl = `file://${path.join(__dirname, 'results_screen_organic_v4_final_2', 'code.html')}`;
    
    for (const [lang, t] of Object.entries(translations)) {
        console.log(`Processing V6 screenshots for ${lang}...`);
        
        // --- INPUT SCREEN ---
        await page.goto(inputUrl, { waitUntil: 'load' });
        await page.evaluate((tr) => {
            // Reemplazo brutal en el HTML para garantizar la traduccion visual
            document.body.innerHTML = document.body.innerHTML
                .replace(/ABDUCCIÓN DE PISTAS/g, tr.t1)
                .replace(/Preparar Secuencia/g, tr.t2)
                .replace(/INICIAR SECUENCIA/g, tr.t3);
        }, t);
        await page.screenshot({ path: `v6_ui_input_${lang}.png` });
        
        // --- RESULTS SCREEN ---
        await page.goto(resultsUrl, { waitUntil: 'load' });
        await page.evaluate((tr) => {
            document.body.innerHTML = document.body.innerHTML
                .replace(/Extracción Completada/g, tr.r1)
                .replace(/Ficha Técnica Forense/gi, tr.r2);
                
            // Abrir el primer acordeón (Bombo) para que se vea rico en información
            const firstBtn = document.querySelector('button[onclick*="toggleAccordion"]');
            if (firstBtn) firstBtn.click();
        }, t);
        
        // Hacemos un scroll ligero para centrar la atencion en los resultados
        await page.evaluate(() => window.scrollBy(0, 150));
        await new Promise(r => setTimeout(r, 500)); // Esperamos a que abra el acordeón
        
        await page.screenshot({ path: `v6_ui_results_${lang}.png` });
    }
    
    await browser.close();
    console.log("All V6 localized screenshots generated!");
})();
