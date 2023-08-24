
let container = document.getElementById("container");
console.log(container);


let pete = document.querySelector("ul.list li:nth-child(2)");
pete.textContent = "Richard";

let secondUl = document.querySelectorAll("ul.list")[1];
let secondLi = secondUl.querySelector("li:nth-child(2)");
secondLi.remove();


let firstLiElements = document.querySelectorAll("ul.list li:first-child");
for(let li of firstLiElements) {
    li.textContent = "Alexander"; 
}

let uls = document.querySelectorAll("ul.list");
uls.forEach(ul => ul.classList.add("student_list"));

uls[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

let danLi = Array.from(document.querySelectorAll("li")).find(li => li.textContent === "Dan");
danLi.style.display = "none";

pete.style.border = "1px solid black";

document.body.style.fontSize = "18px";

if(container.style.backgroundColor === "lightblue") {
    let users = document.querySelectorAll("ul.list li:first-child");
    alert(`Hello ${users[0].textContent} and ${users[1].textContent}`);
}
