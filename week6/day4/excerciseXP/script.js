const people = ["Greg", "Mary", "Devon", "James"];

people.shift()

const index = people.indexOf("James");

if (index !== -1) {
    people[index] = "Jason";
}

people.push("Alex");

console.log(people.indexOf("Mary"))

const copy = people.slice(1, 3);

console.log(people.indexOf("Foo"))

const last = people[people.length - 1]

console.log(last); 

people.forEach(person => {
    console.log(person);
});


for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
        break;
    }
}

const colors = ["blue", "green", "red", "purple", "orange"];
const suffixes = ["1st", "2nd", "3rd", "4th", "5th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${suffixes[i]} choice is ${colors[i]}`);
}



let userInput = prompt("Please enter a number:");


console.log(`The data type of the input is: ${typeof userInput}`);


let numberInput;
let numValue;

do {
    numberInput = prompt("Please enter a number:");
    numValue = Number(numberInput);
} while (isNaN(numValue) || numValue < 10);

console.log(`You entered a number greater than or equal to 10.`);




const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors);

const apartmentsOnFirstAndThird = building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor;
console.log(apartmentsOnFirstAndThird);

const secondTenantName = building.nameOfTenants[1];
const secondTenantRooms = building.numberOfRoomsAndRent[secondTenantName.toLowerCase()][0];
console.log(`${secondTenantName} has ${secondTenantRooms} rooms in his apartment.`);


const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}


const family = {
    father: "John",
    mother: "Jane",
    son: "Jake",
    daughter: "Jill"
};

for (let member in family) {
    console.log(member);
}

for (let member in family) {
    console.log(family[member]);
}

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };
  
  let sentence = '';
  
  for (let key in details) {
      sentence += key + ' ' + details[key] + ' ';
  }
  
  console.log(sentence.trim());
  

  const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const firstLetters = names.map(name => name[0]);

const secretSocietyName = firstLetters.sort().join('');

console.log(secretSocietyName); 
