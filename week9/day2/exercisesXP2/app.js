import persons from './data.js';

function calculateAverageAge() {
  const totalAge = persons.reduce((acc, person) => acc + person.age, 0);
  return totalAge / persons.length;
}

const averageAge = calculateAverageAge();
console.log(`The average age of all persons is: ${averageAge}`);
