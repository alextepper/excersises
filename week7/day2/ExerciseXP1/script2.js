
const formElement = document.querySelector("form");
console.log(formElement);


const firstNameInput = document.getElementById("fname");
const lastNameInput = document.getElementById("lname");
console.log(firstNameInput, lastNameInput);


const inputsByName = document.querySelectorAll("input[name='firstname'], input[name='lastname']");
inputsByName.forEach(input => console.log(input));

formElement.addEventListener("submit", function(event) {
    event.preventDefault();

    const ulElement = document.querySelector(".usersAnswer");


    if (firstNameInput.value.trim() && lastNameInput.value.trim()) {

        let firstNameLi = document.createElement("li");
        firstNameLi.textContent = firstNameInput.value;
        ulElement.appendChild(firstNameLi);

        let lastNameLi = document.createElement("li");
        lastNameLi.textContent = lastNameInput.value;
        ulElement.appendChild(lastNameLi);
    } else {
        alert("Please fill out both fields.");
    }
});