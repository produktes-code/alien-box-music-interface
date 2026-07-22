const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    const filePath = `file://${path.join(__dirname, 'manual_multilingual_v14.html')}`;
    console.log(`Generating Multilingual V14 PDF (Full symmetric text sizes)...`);
    
    try {
        await page.goto(filePath, { waitUntil: 'networkidle0', timeout: 90000 });
        
        await page.pdf({
            path: `AlienBox_Manual_Universal.pdf`,
            format: 'A4',
            printBackground: true,
            preferCSSPageSize: true, 
            margin: {
                top: '0',
                bottom: '0',
                left: '0',
                right: '0'
            }
        });
        console.log(`Success! Multilingual V14 PDF generated.`);
    } catch (e) {
        console.error(`Error generating Multilingual V14 PDF:`, e);
    }

    await browser.close();
})();
