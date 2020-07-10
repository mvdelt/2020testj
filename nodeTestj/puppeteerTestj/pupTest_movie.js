const puppeteer = require('puppeteer');
const mkdirj = require('../nodeCodesj/makeDirJ'); // i. 아놔 ㅋㅋ 여기도 세미콜론 없으니까 실행시키면 컴파일러(?)가 여기에다가 아래쪽코드의 (...)를 갖다붙여버리네 ㅋㅋㅋ



// console.log(__dirname)
// mkdirj('./posterImagesj', 0744, function(err) {
//   const dirpathj = __dirname + '/posterImagesj'
//   if (err){
//       // handle folder creation error
//       console.error(err)
//   } 
//   else{ // we're all good
//       console.log(`j) make dir '${dirpathj}' successfully finished.`)
//   }
// }); // i. js 에서도 세미콜론이 필요할때가 있네!!!!!! 지금같은경우 필요!!!!!! 여기 세미콜론이 없으면 바로아래코드랑 연결된것으로 간주됨!!!
//     // 즉, 요 세미콜론을 없애고 돌려보면, 컴파일러(?)가 요 mkdirj 함수의 리턴값(리턴값없음)에다가 이 아래코드의 ()를 붙인걸로 이해함!!
//     // 따라서 (async () => {...  의 시작지점을 가리키면서 다음과같은 에러가 뜸. TypeError: mkdirj(...) is not a function
//     // 이해 완료.


(async () => {
  const browser = await puppeteer.launch({headless:false});
  const page = await browser.newPage();

  const urlj = "https://www.themoviedb.org/?language=en-US" 

  await page.goto(
    urlj,
    {waitUntil: 'networkidle2'}
  );
  await page.screenshot({path: 'moviedbMain.png', fullPage: true});  
  
  const fs = require('fs');
  const request = require('request');

  const downloadFct = function(uri, filename, callback){
    request.head(uri, function(err, res, body){
      console.log('res.headers[\'content-type\']:', res.headers['content-type']);
      console.log('res.headers[\'content-length\']:', res.headers['content-length']);
      request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
    });
  };  
  // i. 호출예시.
  // downloadFct(
  //   'https://www.google.com/images/srpr/logo3w.png',
  //   'google.png',
  //   function(){
  //     console.log('done');
  //   }
  // );
  
  
  let posterImg_url_arrj = await page.evaluate(()=>{      
    const num_moviesj = document.querySelector("#popular_scroller > div").childElementCount-2 // i. 보니까 맨마지막엘리먼트들 몇개는 머 다른거인듯. 
    let posterImg_url_arrj = []

    console.log(document.querySelector("#popular_scroller > div > div:nth-child(3) > div.image > div.wrapper > a > img"))
    for (let i=0; i<num_moviesj; i++){ //

      // i. for loop 을 위한 async await 같은게 필요한건가???

      let url = document.querySelector(`#popular_scroller > div > div:nth-child(${i+1}) > div.image > div.wrapper > a > img`).dataset.src
      posterImg_url_arrj.push(url)
    }

    // idxj = 2
    // console.log(document.querySelector("#popular_scroller > div > div:nth-child(3) > div.image > div.wrapper > a > img"))
    // url = document.querySelector(`#popular_scroller > div > div:nth-child(${idxj+1}) > div.image > div.wrapper > a > img`).dataset.src
    // posterImg_url_arrj.push(url)



    return posterImg_url_arrj
  });


  console.log('__dirname:',__dirname);
  mkdirj('./posterImagesj', 0744, function(err) {
    const dirpathj = __dirname + '/posterImagesj'
    if (err){
        // handle folder creation error
        console.error(err)
    } 
    else{ // we're all good
        console.log(`j) make dir '${dirpathj}' successfully finished.`)
    }
  }); // i. js 에서도 세미콜론이 필요할때가 있네!!!!!! 지금같은경우 필요!!!!!! 여기 세미콜론이 없으면 바로아래코드랑 연결된것으로 간주됨!!!
      // 즉, 요 세미콜론을 없애고 돌려보면, 컴파일러(?)가 요 mkdirj 함수의 리턴값(리턴값없음)에다가 이 아래코드의 (...)를 붙인걸로 이해함!!(지금은 코드 위치를 바꿔서 아래에 (...)가 없고 for문이 나오는데, 예전위치에선 그랬음.)
      // 따라서 (async () => {...  의 시작지점을 가리키면서 다음과같은 에러가 뜸. TypeError: mkdirj(...) is not a function
      // 이해 완료.


  // i. var 말고 let 을 사용하면 변수 i 를 각 for에 한정시키는것 바로 해결됨. 죠 아래 붙여논 링크 글 참고했음.
  for(let i=0; i<posterImg_url_arrj.length; i++){    
    downloadFct(posterImg_url_arrj[i], `./posterImagesj/poster${i}.png`, ()=>{
      console.log(`j) poster image ${i} was successfully downloaded.`)
    })
  }

  // i. let 이 아닌, var 를 쓰면서 변수를 각 for에 대해 한정시키는 방법. 다음 글 참고했음: https://www.pluralsight.com/guides/javascript-callbacks-variable-scope-problem
  // for(var i=0; i<posterImg_url_arrj.length; i++){
  //   downloadFct(posterImg_url_arrj[i], `./posterImagesj/poster${i}.png`, (
  //       function(){ var j=i; return function(){
  //         console.log(`j) poster image ${j} was successfully downloaded.`)
  //       }}
  //     )()
  //   )
  // }

  // await browser.close();
})();

