const puppeteer = require('puppeteer');
require('dotenv').config();
const mouse_helperj = require('./mouse_helper')['installMouseHelper'];

titlej = '이거슨 제목이당';

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: './userDataDir_j',
  });
  const page = await browser.newPage();
  await page.goto("https://www.naver.com");  //네이버메인.
  await page.click("#account > a") //로그인버튼클릭.
  await page.click('#id')
  await page.type('#id', process.env.NAVER_IDj, {delay: 50})
  await page.click('#pw')
  await page.type('#pw', process.env.NAVER_PWj, {delay: 50})
  
  //// i. 퍼펫티어 공홈에서, waitForNavigation 쓸때는 race condition 발생할수있으니 아래처럼 Promise.all 로 묶으라했는데, 왠 레이스컨디션?? 내생각엔 묶을필요 없음.

  // const p_all_1 = await Promise.all([
  //   // page.waitForSelector('#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(3) > a'),

  //   // i. 이 두줄 순서는 상관없는건가?? 그리고, 이렇게 Promise.all 안해도 되려나?(지금 되다 안되다 그럼;; inconsistent 함;;; 아디랑 비붠입력하는 직전에 각각 클릭 넣으니까 괜찮아진것같긴한데..)
  //   page.click("#log\\.login"), //(아듸븨붠입력후)로그인버튼클릭.
  //   page.waitForNavigation(),
  // ]);
  // console.log('p_all_1:',p_all_1);

  await page.click("#log\\.login"); //(아듸븨붠입력후)로그인버튼클릭.
  await page.waitForNavigation();

  // await Promise.all([
  //   page.click('#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(3) > a'), //블로그 클릭.
  //   page.waitForNavigation(),
  // ]);

  await page.click('#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(3) > a'); //블로그 클릭.
  await page.waitForNavigation();

  // 글쓰기 클릭하면 "새창"으로 뜬다!!!!!!!! ->새창 객체를 가져와야함!! 아래 코드 살짝바꿔 사용하니 잘 됨!!! https://github.com/puppeteer/puppeteer/issues/3718
  // this._page 또는 this._browser 는 뭔지모르겟는데 해보니 안돼서 걍 page, browser 로 하니 잘됨!

  // const pageTarget = this._page.target(); //save this to know that this was the opener
  // await resultItem.element.click(); //click on a link
  // const newTarget = await this._browser.waitForTarget(target => target.opener() === pageTarget); //check that you opened this page, rather than just checking the url
  // const newPage = await newTarget.page(); //get the page object
  // // await newPage.once("load",()=>{}); //this doesn't work; wait till page is loaded
  // await newPage.waitForSelector("body"); //wait for page to be loaded

  const origPageTargetj = page.target(); //save this to know that this was the opener  
  // await Promise.all([
  //   page.click('#container > div > aside > div > div:nth-child(1) > nav > a:nth-child(2)'), //글쓰기 클릭. https://blog.naver.com/looiv?Redirect=Write 로 새창열림.
  //   page.waitForNavigation(),
  // ]);
  await page.click('#container > div > aside > div > div:nth-child(1) > nav > a:nth-child(2)'); //글쓰기 클릭. https://blog.naver.com/looiv?Redirect=Write 로 새창열림.
  
  const newTarget = await browser.waitForTarget(target => target.opener() === origPageTargetj); //check that you opened this page, rather than just checking the url
  const newPage = await newTarget.page(); //get the page object

  // await newPage.waitForSelector("body"); //wait for page to be loaded
  await newPage.waitForNavigation(); // i. waitForNavigation 굳이 promise.all 로 안감싸도 아주 잘 작동!! 공홈에선 뭔소릴하는건지몰겟네;;

  await newPage.screenshot({path: 'blogWrite.png', fullPage: true}); // i. waitForNavigation을 써주니까 스크린샷이 제대로 찍힘. 안써주면 화면 아직 다 안떴는데(로딩중) 벌써 스샷이 찍혀버림.

  // 참고로, 제목 마우스위치는 x,y : 186,255


  // // i. 이렇게 프라미스.all 로 묶어주면, 얘네 완전 "동시에" 실행된다!!! 즉, 요 타이핑하는것들이 죄다 섞여서 써진다!!!(딜레이50줘서그런지 되게 딱딱맞춰서 섞이긴하지만 아무튼.)
  // await Promise.all([
  //   newPage.keyboard.type('xxxxyyyyzzzzvvvvqqqqppppssssrrrruuuu', {delay: 50}),
  //   newPage.keyboard.type('123456789011223344556677889900', {delay: 50}),
  //   newPage.keyboard.type('aaaabbbbccccddddeeeeffffgggghhhhiiii', {delay: 50}),
  //   newPage.keyboard.press('ArrowUp'), // 디폴트로 커서가 본문에 위치해있음. 윗쪽화살표 눌러서 제목쓰는곳으로 커서 이동.  
  // ]);

  await newPage.keyboard.press('ArrowUp'); // 디폴트로 커서가 본문에 위치해있음. 윗쪽화살표 눌러서 제목쓰는곳으로 커서 이동.  
  await newPage.keyboard.type('한글도 되나?', {delay: 50});
  await newPage.keyboard.press('ArrowDown'); // 아래화살표 눌러서 본문쓰는곳으로 커서 이동.  
  await newPage.keyboard.type('오오 한글도 잘 되네!!! English typing is also good, 한국말도 굿! \n줄바꿈도 \n될까?? \nlets try!! \n     들여쓰기까지되고 다 겁나잘됨!!!', {delay: 50});
  
  // await page.keyboard.press('ArrowDown'); // 본문으로 커서 이동 이렇게하면 될라나?
  // await page.keyboard.type(titlej, {delay: 10})     



  // await browser.close();
})();

