const p1 = new Promise((resolvej, rejectj)=>{
    console.log('inside p1 before')
    resolvej('p1 resolved!!', 'kkkk') // i. 인풋인자 2개 집어넣어봄. -> 첫번째 인풋인자만 유효하네.
    console.log('inside p1 after')
})

// i. 2020.07.08.현재, 개오랜만에 다시 Promise 복습해서 깨달은바로는, resolve, reject 는 그저 콜백함수들일뿐임. 이름도 맘대로 해도 상관없을듯.
//    resolve는 .then 에 넣어주는 콜백함수를 의미하고, reject는 .catch 에 넣어주는 콜백함수를 의미하는것같음.
const p2 = new Promise((resolvejjj, rejectj)=>{ 
    console.log('inside p2 before')
    resolvejjj('p2 resolved!!')
    console.log('inside p2 after')
})
const p3 = new Promise((resolveyeah, rejectj)=>{
    console.log('inside p3 before')
    resolveyeah('p3 resolved!!')
    console.log('inside p3 after')
})

p1.then((a,b)=>{console.log(a,b)})

Promise.all([p1,p2,p3])
    .then(
        (a)=>{console.log('jdjdjdjdjd',a)}
    )