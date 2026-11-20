// Render index.html to a full-length PNG (780px wide) and record section boundaries.
// Usage: node src/render.js [scale]   -> output/_full@{scale}x.png + output/_sections.json
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const scale = Number(process.argv[2] || 1);
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 780, height: 1200 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.join(root, 'index.html'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const secs = await page.$$eval('.sec', els => els.map(e => {
    const r = e.getBoundingClientRect();
    return { id: e.id, top: Math.round(r.top + scrollY), height: Math.round(r.height) };
  }));
  const missing = await page.evaluate(() => [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family));
  fs.mkdirSync(path.join(root, 'output'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'output', `_full@${scale}x.png`), fullPage: true });
  fs.writeFileSync(path.join(root, 'output', '_sections.json'), JSON.stringify(secs, null, 1));
  console.log(JSON.stringify(secs), 'unloaded fonts:', missing);
  await browser.close();
})();
