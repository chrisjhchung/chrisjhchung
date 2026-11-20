const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1024, height: 1024 } });
  const names = fs.readdirSync('.').filter(f => f.endsWith('.svg')).map(f => f.replace('.svg',''));
  for (const n of names) {
    await p.setContent(`<html><body style="margin:0">${fs.readFileSync(n + '.svg','utf8')}</body></html>`);
    await p.screenshot({ path: n + '.png', clip: { x:0, y:0, width:1024, height:1024 } });
  }
  // preview sheet: each variant at 360, 120, 40 px circle crops on light + dark bg
  const row = n => `<div style="display:flex;align-items:center;gap:28px;margin:18px 0">
     <div style="width:180px;font:14px sans-serif;color:#ccc">${n}</div>
     ${[360,120,40].map(s=>`<img src="${n}.png" style="width:${s}px;height:${s}px;border-radius:50%">`).join('')}
     <div style="background:#fff;padding:12px;border-radius:8px;display:flex;gap:14px;align-items:center">${[120,40].map(s=>`<img src="${n}.png" style="width:${s}px;height:${s}px;border-radius:50%">`).join('')}</div></div>`;
  fs.writeFileSync('preview.html', `<html><body style="background:#1e1e1e;padding:20px;margin:0">${names.map(row).join('')}</body></html>`);
  const p2 = await b.newPage({ viewport: { width: 1000, height: 1250 } });
  await p2.goto('file://' + process.cwd() + '/preview.html');
  await p2.screenshot({ path: 'preview.png', fullPage: true });
  await b.close();
})();
