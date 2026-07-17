const puppeteer = require('puppeteer-core');
(async () => {
  const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new' });
  const p = await b.newPage();
  await p.setViewport({ width: 1280, height: 800 });
  await p.goto('http://localhost:4199/77-unfold/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 2300));
  const out = await p.evaluate(() => ({
    overtureDone: document.getElementById('overture').classList.contains('done'),
    borne: document.body.classList.contains('borne'),
    h1Visible: getComputedStyle(document.querySelector('h1')).opacity,
  }));
  await p.screenshot({ path: '/private/tmp/claude-501/-Users-jeremyxiang-Claude-Sites/b7b60670-397b-4ad5-9f91-5ea1087723ab/scratchpad/77b.png' });
  console.log(JSON.stringify(out));
  await b.close();
})();
