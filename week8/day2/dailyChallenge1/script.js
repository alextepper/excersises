function makeAllCaps(words) {
    let promise = new Promise((resolve, reject) => {
        if (words.every(i => typeof i === "string")) {
            words = words.map(function(x){ return x.toUpperCase(); })
            resolve(words)
        } else {
            reject('Bad array')
        }
    })
    return promise
}

function sortWords(words) {
    let promise = new Promise((resolve, reject) => {
        if (words.length > 4) {
            resolve(words.sort())
        } else {
            reject('Too short')
        }
    })
    return promise

}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))