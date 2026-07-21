const puppeteer = require('puppeteer');
const path = require('path');

const translations = {
    'es': { title: 'Modo de Análisis Neuronal', btn: 'D3 EXTREME', launch: 'INICIAR SECUENCIA' },
    'en': { title: 'Neural Analysis Mode', btn: 'D3 EXTREME', launch: 'INITIATE SEQUENCE' },
    'ru': { title: 'Режим нейронного анализа', btn: 'D3 ЭКСТРИМ', launch: 'ЗАПУСТИТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ' },
    'uk': { title: 'Режим нейронного аналізу', btn: 'D3 ЕКСТРИМ', launch: 'ЗАПУСТИТИ ПОСЛІДОВНІСТЬ' },
    'zh': { title: '神经分析模式', btn: 'D3 极限', launch: '启动序列' },
    'ja': { title: 'ニューラル分析モード', btn: 'D3 エクストリーム', launch: 'シーケンス開始' },
    'de': { title: 'Neuronale Analyse', btn: 'D3 EXTREM', launch: 'SEQUENZ STARTEN' }
};

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900, deviceScaleFactor: 2 });
    const uiPath = `file://${path.join(__dirname, 'input_screen_organic_v4_final_2', 'code.html')}`;
    
    for (const [lang, trans] of Object.entries(translations)) {
        console.log(`Processing screenshots for ${lang}...`);
        await page.goto(uiPath, { waitUntil: 'load' });
        
        // Inject translations
        await page.evaluate((t) => {
            // Replace text in DOM
            const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
            let n;
            while(n = walk.nextNode()) {
                if (n.nodeValue.includes('Modo de Análisis Neuronal')) n.nodeValue = n.nodeValue.replace('Modo de Análisis Neuronal', t.title);
                if (n.nodeValue.includes('INICIAR SECUENCIA')) n.nodeValue = n.nodeValue.replace('INICIAR SECUENCIA', t.launch);
            }
            
            // Try to find D3 button and translate it
            const btns = Array.from(document.querySelectorAll('button'));
            const d3Btn = btns.find(b => b.textContent.includes('D3'));
            if (d3Btn) d3Btn.innerHTML = d3Btn.innerHTML.replace('D3', t.btn);
        }, trans);
        
        // Main screenshot
        await page.screenshot({ path: `ui_screenshot_main_${lang}.png` });
        
        // Click D3 if exists and take second screenshot
        try {
            await page.evaluate(() => {
                const btns = Array.from(document.querySelectorAll('button'));
                const d3Btn = btns.find(b => b.textContent.includes('D3') || b.textContent.includes('D3'));
                // Just click the third mode button (D3 is usually index 2 in the mode group)
                if(btns.length > 2) btns[2].click();
            });
            await new Promise(r => setTimeout(r, 500));
            await page.screenshot({ path: `ui_screenshot_d3_${lang}.png` });
        } catch(e) {}
    }
    
    await browser.close();
    console.log("All localized screenshots generated!");
})();
