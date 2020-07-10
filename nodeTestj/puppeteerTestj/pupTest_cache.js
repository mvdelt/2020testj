const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    userDataDir: './userDataDir_j',
    headless: true,
    args: ['--no-sandbox'],
  });

  const page = await browser.newPage();
  const response = await page.goto('https://example.com/');
  console.log(response.fromCache());

  await browser.close();
})();