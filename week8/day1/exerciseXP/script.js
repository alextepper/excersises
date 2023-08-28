const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// the output:
// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)


function displayStudentInfo({ first, last }){
    return `Your full name is ${first} ${last}`;
}

console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));



const users = { user1: 18273, user2: 92833, user3: 90315 };

const usersArray = Object.entries(users);

console.log(usersArray); 

const modifiedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);

console.log(modifiedUsersArray);


class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
  const member = new Person('John');
  console.log(typeof member);

//   output: 'object'


class Labrador extends Dog {
    constructor(name, size) {
      super(name); 
      this.size = size;
    }
  };

//   [2] === [2] // False
//   {} === {}   // False

const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)  // 4
console.log(object3.number)  // 4
console.log(object4.number)  // 5

// object2 and object3 both reference the same memory location
  

class Animal {
    constructor(name, type, color) {
      this.name = name;
      this.type = type;
      this.color = color;
    }
  }
  
  class Mamal extends Animal {
    sound(animalSound) {
      return `${animalSound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
  }
  
  const farmerCow = new Mamal("Lily", "cow", "brown and white");
  console.log(farmerCow.sound("Moooo")); 
  