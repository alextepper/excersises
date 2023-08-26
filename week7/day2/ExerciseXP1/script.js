
const h1Element = document.querySelector("h1");
console.log(h1Element.textContent);


const articleElement = document.querySelector("article");
const lastParagraph = articleElement.lastElementChild;
if (lastParagraph.tagName.toLowerCase() === 'p') {
    lastParagraph.remove();
}

const h2Element = document.querySelector("h2");
h2Element.addEventListener("click", function() {
    this.style.backgroundColor = "red";
});


const h3Element = document.querySelector("h3");
h3Element.addEventListener("click", function() {
    this.style.display = "none";
});

const buttonElement = document.querySelector("button");
buttonElement.addEventListener("click", function() {
    const paragraphs = document.querySelectorAll("p");
    paragraphs.forEach(p => {
        p.style.fontWeight = "bold";
    });
});

h1Element.addEventListener("mouseover", function() {
    const randomSize = Math.floor(Math.random() * 101);
    this.style.fontSize = `${randomSize}px`;
});


const fadeParagraph = document.querySelector(".fade-target");
fadeParagraph.addEventListener("mouseover", function() {
    this.style.animation = "fadeOut 1s forwards";
});
