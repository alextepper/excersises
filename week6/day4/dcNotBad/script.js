// Create a variable called sentence
let sentence = "The movie is not that bad, I like it";

// Find the position of the word "not"
let wordNot = sentence.indexOf("not");

// Find the position of the word "bad"
let wordBad = sentence.indexOf("bad");

// Check if "bad" comes after "not"
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    sentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log(sentence);
} else {
    console.log(sentence);
}