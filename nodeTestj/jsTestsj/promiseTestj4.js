const fruitBasket = {
    apple: 27,
    grape: 0,
    pear: 14
}

const sleep = ms => {
    return new Promise(resolve => setTimeout(()=>{resolve('KA_KA')}, ms))
}
  
const getNumFruit = fruit => {
    console.log('sleep(1000):',sleep(1000))
    console.log('sleep(1000).then(v => fruitBasket[fruit]):',sleep(1000).then(v => {
        console.log('v:',v)
        return fruitBasket[fruit]
    }))
    return sleep(1000).then(v => {console.log('v2:',v); return fruitBasket[fruit]})  // i. .then 은 항상 Promise 를 리턴한다.
    // .then(...)관련해서 MDN에 설명 상세하게 잘나와있음. Promise 및 resolve 등에 대해서도 잘 나와잇음.
}
  
getNumFruit('apple')
    .then(num => console.log(num)) // 27    




// i. MDN 의 Promise.prototype.then() 설명글 중 발췌.
// Return value
// Once a Promise is fulfilled or rejected, the respective handler function (onFulfilled or onRejected) will be called asynchronously (scheduled in the current thread loop). The behavior of the handler function follows a specific set of rules. If a handler function:

// returns a value, the promise returned by then gets resolved with the returned value as its value.
// doesn't return anything, the promise returned by then gets resolved with an undefined value.
// throws an error, the promise returned by then gets rejected with the thrown error as its value.
// returns an already fulfilled promise, the promise returned by then gets fulfilled with that promise's value as its value.
// returns an already rejected promise, the promise returned by then gets rejected with that promise's value as its value.
// returns another pending promise object, the resolution/rejection of the promise returned by then will be subsequent to the resolution/rejection of the promise returned by the handler. Also, the resolved value of the promise returned by then will be the same as the resolved value of the promise returned by the handler.