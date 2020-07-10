const promise = new Promise((resolve, reject) => { 
    // setTimeout(() => { 
    //     resolve([89, 45, 323]); 
    // }, 3000); 
    setTimeout(() => { 
        reject([89, 45, 323]); 
    }, 2000); 
}); 

console.log('startedj');

promise
    .then(values => {console.log(values[1])})
    .catch(x=>{console.log('dfdf', x)});   // i. 요 .catch 가 없으면 에러뜸: Unhandled promise rejection. 모든 프라미스의 리젝션은 핸들링되어야함.

promise.catch(x => {console.log('j) catch executed. x[0]*3:', x[0]*100)});

console.log('endedj');