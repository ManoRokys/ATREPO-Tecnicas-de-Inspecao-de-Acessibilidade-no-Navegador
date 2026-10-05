const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function run() {
    const htmlPath = 'file:///' + path.resolve(__dirname, 'painel-campanha.html').replace(/\\/g, '/');
    console.log('Opening:', htmlPath);

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: { width: 1280, height: 800 },
        deviceScaleFactor: 2
    });
    const page = await context.newPage();
    await page.goto(htmlPath);
    await page.waitForTimeout(1000);

    const evidenciasDir = path.resolve(__dirname, 'evidencias');
    if (!fs.existsSync(evidenciasDir)) {
        fs.mkdirSync(evidenciasDir, { recursive: true });
    }

    // 1. Normal screenshot
    await page.screenshot({ path: path.join(evidenciasDir, 'base_normal.png') });

    // 2. Vision deficiencies via CDP
    const client = await context.newCDPSession(page);

    await client.send('Emulation.setEmulatedVisionDeficiency', { type: 'protanopia' });
    await page.screenshot({ path: path.join(evidenciasDir, 'base_protanopia.png') });

    await client.send('Emulation.setEmulatedVisionDeficiency', { type: 'deuteranopia' });
    await page.screenshot({ path: path.join(evidenciasDir, 'base_deuteranopia.png') });

    await client.send('Emulation.setEmulatedVisionDeficiency', { type: 'blurredVision' });
    await page.screenshot({ path: path.join(evidenciasDir, 'base_blurred.png') });

    // Reset vision deficiency
    await client.send('Emulation.setEmulatedVisionDeficiency', { type: 'none' });

    // 3. Tab focus interaction
    // Focus email input (tabindex=1)
    await page.focus('input[tabindex="1"]');
    await page.screenshot({ path: path.join(evidenciasDir, 'base_focus_email.png') });

    // Focus name input (tabindex=2)
    await page.focus('input[tabindex="2"]');
    await page.screenshot({ path: path.join(evidenciasDir, 'base_focus_nome.png') });

    await browser.close();
    console.log('Screenshots base gerados com sucesso!');
}

run().catch(console.error);
