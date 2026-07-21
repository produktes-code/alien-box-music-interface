const puppeteer = require('puppeteer');
const path = require('path');

const translations = {
    'es': { 
        input: 'Panel de Abducción', btn_launch: 'INICIAR SECUENCIA', 
        res: 'Descodificación del Target', res_subtitle: 'Análisis Espectral' 
    },
    'en': { 
        input: 'Abduction Panel', btn_launch: 'INITIATE SEQUENCE', 
        res: 'Target Decoding', res_subtitle: 'Spectral Analysis' 
    },
    'ru': { 
        input: 'Панель абдукции', btn_launch: 'ЗАПУСТИТЬ', 
        res: 'Декодирование цели', res_subtitle: 'Спектральный анализ' 
    },
    'uk': { 
        input: 'Панель абдукції', btn_launch: 'ЗАПУСТИТИ', 
        res: 'Декодування цілі', res_subtitle: 'Спектральний аналіз' 
    },
    'zh': { 
        input: '劫持面板', btn_launch: '启动序列', 
        res: '目标解码', res_subtitle: '光谱分析' 
    },
    'ja': { 
        input: 'アブダクションパネル', btn_launch: 'シーケンス開始', 
        res: 'ターゲットデコード', res_subtitle: 'スペクトル分析' 
    },
    'de': { 
        input: 'Entführungspanel', btn_launch: 'SEQUENZ STARTEN', 
        res: 'Zieldekodierung', res_subtitle: 'Spektralanalyse' 
    }
};

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900, deviceScaleFactor: 2 });
    
    const inputUrl = `file://${path.join(__dirname, 'input_screen_organic_v4_final_2', 'code.html')}`;
    const resultsUrl = `file://${path.join(__dirname, 'results_screen_organic_v4_final_2', 'code.html')}`;
    
    for (const [lang, t] of Object.entries(translations)) {
        console.log(`Processing screenshots for ${lang}...`);
        
        // 1. INPUT SCREEN
        await page.goto(inputUrl, { waitUntil: 'load' });
        await page.evaluate((tr) => {
            const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
            let n;
            while(n = walk.nextNode()) {
                if (n.nodeValue.includes('ALIEN BOX INJECTION')) n.nodeValue = n.nodeValue.replace('ALIEN BOX INJECTION', tr.input);
                if (n.nodeValue.includes('INICIAR SECUENCIA')) n.nodeValue = n.nodeValue.replace('INICIAR SECUENCIA', tr.btn_launch);
            }
        }, t);
        await page.screenshot({ path: `ui_input_${lang}.png` });
        
        // 2. RESULTS SCREEN
        await page.goto(resultsUrl, { waitUntil: 'load' });
        await page.evaluate((tr) => {
            const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
            let n;
            while(n = walk.nextNode()) {
                if (n.nodeValue.includes('Extracción Completada')) n.nodeValue = n.nodeValue.replace('Extracción Completada', tr.res);
                if (n.nodeValue.includes('Ficha Técnica Forense')) n.nodeValue = n.nodeValue.replace('Ficha Técnica Forense', tr.res_subtitle);
            }
        }, t);
        // Desplazar un poco hacia abajo para que se vea el contenido
        await page.evaluate(() => window.scrollBy(0, 100));
        await page.screenshot({ path: `ui_results_${lang}.png` });
    }
    
    await browser.close();
    console.log("All distinct localized screenshots generated!");
})();
