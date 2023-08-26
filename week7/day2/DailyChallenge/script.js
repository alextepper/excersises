const formElement = document.getElementById("libform");

const nounInput = document.getElementById('noun');
const adjectiveInput = document.getElementById('adjective');
const personInput = document.getElementById('person');
const verbInput = document.getElementById('verb');
const placeInput = document.getElementById('place');

function createAStory(noun, adjective, person, verb, place) {
    return `In a land far away, there existed a ${adjective} ${noun}. Many believed it was just a myth, but ${person} knew it was real. One day, driven by curiosity, ${person} decided to embark on a quest to ${place} in hopes of discovering this legendary ${noun}. After days of searching, ${person} encountered a strange old man who claimed to have seen the ${noun}. The old man advised ${person} to ${verb} cautiously, as the ${noun}, though ${adjective}, was known to be unpredictable. Inspired and filled with hope, ${person} continued the journey, knowing that the adventure had only just begun.`;
}

formElement.addEventListener("submit", function(event) {
    event.preventDefault();

    const storyElement = document.getElementById("story");


    if (nounInput.value.trim() && adjectiveInput.value.trim() && personInput.value.trim() && verbInput.value.trim() && verbInput.value.trim()) {
        storyElement.append(createAStory(nounInput.value, adjectiveInput.value, personInput.value, verbInput.value, placeInput.value)) 
    } else {
        alert("Please fill out all fields.");
    }
});