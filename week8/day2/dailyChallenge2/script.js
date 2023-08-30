const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

  function toJs() {
    return new Promise((resolve, reject) => {
        const morseJsObject = JSON.parse(morse);
        if (Object.keys(morseJsObject).length === 0) {
            reject(new Error("Morse JavaScript object is empty."));
        } else {
            resolve(morseJsObject);
        }
    });
}

function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const userInput = prompt("Please enter a word or a sentence:").toLowerCase();
        let morseCode = '';

        for (let char of userInput) {
            if (!morseJS[char]) {
                reject(new Error(`Character ${char} doesn't exist in the Morse code mapping.`));
                return;
            } else {
                morseCode += morseJS[char] + ' ';
            }
        }

        resolve(morseCode.trim()); 
    });
}


function joinWords(morseTranslation) {
    const displayElement = document.createElement('div');
    displayElement.textContent = morseTranslation.split(' ').join('\n');  // Assuming that each Morse word is separated by space
    document.body.appendChild(displayElement);
}


toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.error(error.message));
