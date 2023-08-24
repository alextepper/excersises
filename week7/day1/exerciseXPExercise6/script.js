
let divElement = document.getElementById('navBar');
divElement.setAttribute('id', 'socialNetworkNavigation');


let ulElement = divElement.querySelector('ul'); 

let newLi = document.createElement('li');
let newText = document.createTextNode('Logout');

newLi.appendChild(newText); 
ulElement.appendChild(newLi);


let firstLi = ulElement.firstElementChild;
let lastLi = ulElement.lastElementChild;

console.log('First li text:', firstLi.textContent);
console.log('Last li text:', lastLi.textContent);
