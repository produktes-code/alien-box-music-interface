const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set a good desktop resolution
    await page.setViewport({ width: 1280, height: 900, deviceScaleFactor: 2 });
    
    const uiPath = `file://${path.join(__dirname, 'input_screen_organic_v4_final_2', 'code.html')}`;
    console.log('Loading UI:', uiPath);
    await page.goto(uiPath, { waitUntil: 'load' });
    
    // Take screenshot of main screen
    await page.screenshot({ path: 'ui_screenshot_main.png' });
    console.log('Took ui_screenshot_main.png');
    
    // Interact with UI if possible to get a different state
    // Let's click the D3 mode button if it exists
    try {
        // We evaluate a script to click the D3 element
        await page.evaluate(() => {
            const d3Btn = Array.from(document.querySelectorAll('button')).find(el => el.textContent.includes('D3'));
            if (d3Btn) d3Btn.click();
        });
        await new Promise(resolve => setTimeout(resolve, 500));
        await page.screenshot({ path: 'ui_screenshot_d3.png' });
        console.log('Took ui_screenshot_d3.png');
    } catch (e) {
        console.log('Could not click D3', e);
    }

    await browser.close();
})();
