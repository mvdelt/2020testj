const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: './userDataDir_j',
    // executablePath: "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  // i. 이런식으로해주는거 맞나?.. (크로미움이 아닌)크롬 실행되긴하는데 구글계정로긴안된상태의 초기화된 크롬이 실행되네..
    // args: [
    //   '--no-sandbox',
    //   '--disable-setuid-sandbox',
    //   '--disable-gpu'
    // ]
  });
  const page = await browser.newPage();

  const urlj = "https://www.naver.com"   

  // const currentChromeUAj = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
  // const setUAresultj = await page.setUserAgent(currentChromeUAj)
  // console.log('setUAresultj:',setUAresultj)

  const UAj = await browser.userAgent()
  console.log('j) browser.userAgent():',UAj)  

  const responsej = await page.goto(
    urlj,
    {waitUntil: 'networkidle2'}, // i. 뭐 이코드 없어도 잘되긴하는데 걍 넣어줘봄.
  );

  console.log('j) responsej.fromCache():',responsej.fromCache());

  await page.screenshot({path: 'naverMain.png', fullPage: true});

  await page.waitForSelector("#NM_RTK_VIEW_list_wrap > ul:nth-child(2) > li:nth-child(1) > a > span") // i. 뭐 이코드 없어도 잘되긴하는데 걍 넣어줘봄.

 
  
  let kw_arr = await page.evaluate(()=>{
    // searchKeywordj = document.querySelector("#NM_RTK_VIEW_list_wrap > ul:nth-child(2) > li:nth-child(1) > a > span").innerText    
    
    // document.querySelector("#NM_RTK_ROLLING_WRAP > div > div > a").click() // i. 없어도상관없네.
    kw_arr = []

    // i. 급상승검색어 1~10위.
    // document.querySelector("#NM_RTK_VIEW_list_wrap > div > a:nth-child(1)").click() // i. 없어도상관없네.
    num_kw_tab1 = document.querySelector("#NM_RTK_VIEW_list_wrap > ul:nth-child(2)").childElementCount // i. 걍 10 으로 하드코딩해도되는데 걍 일케해봄.
    for (let i = 0; i < num_kw_tab1; i++) {
      const kw = document.querySelector(`#NM_RTK_VIEW_list_wrap > ul:nth-child(2) > li:nth-child(${i+1}) > a > span`).textContent
      kw_arr.push(kw)
    }    
    // i. 급상승검색어 11~20위.
    // document.querySelector("#NM_RTK_VIEW_list_wrap > div > a:nth-child(2)").click() // i. 없어도상관없네.
    num_kw_tab2 = document.querySelector("#NM_RTK_VIEW_list_wrap > ul:nth-child(3)").childElementCount // i. 걍 10 으로 하드코딩해도되는데 걍 일케해봄.
    for (let i = 0; i < num_kw_tab2; i++) {
      const kw = document.querySelector(`#NM_RTK_VIEW_list_wrap > ul:nth-child(3) > li:nth-child(${i+1}) > a > span`).innerHTML
      kw_arr.push(kw)
    }    
    return kw_arr
  });

  console.log('kw_arr:',kw_arr)

  // await browser.close();
})();

