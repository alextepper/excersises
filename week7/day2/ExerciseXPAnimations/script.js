setTimeout(function() {
    alert("Hello World");
}, 2000);

setTimeout(function() {
    const container = document.getElementById("container");
    const pElement = document.createElement("p");
    pElement.innerHTML = "Hello World";
    container.appendChild(pElement);
}, 2000);

let count = 0;
const intervalId = setInterval(function() {
    const container = document.getElementById("container");
    const pElement = document.createElement("p");
    pElement.innerHTML = "Hello World";
    container.appendChild(pElement);
    count++;
    
    if (count === 4) {
        clearInterval(intervalId);
    }
}, 2000);

document.getElementById("clear").addEventListener("click", function() {
    clearInterval(intervalId);
});