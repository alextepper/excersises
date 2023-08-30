function compareToTen(number) {
    let promise = new Promise((resolve, reject) => {
        if (number >= 10) {
            resolve('The promised task was performed successfully.');
        } else {
            reject('The promised task was not performed.');
        }
    });
    return promise
}

compareToTen(15)
    .then(result => console.log(result))
    .catch(error => console.log(error))

compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error))


const delayedPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("success");
    }, 4000);
});

delayedPromise.then(result => {
    console.log(result); 
  }).catch(error => {
    console.log(error);
  });

  const resolvePromise = Promise.resolve(3);

resolvePromise.then(result => {
  console.log(result); 
}).catch(error => {
  console.log(error);
});

const rejectPromise = Promise.reject("Boo!");

rejectPromise.then(result => {
  console.log(result);
}).catch(error => {
  console.log(error); 
});