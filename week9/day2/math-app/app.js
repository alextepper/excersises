const _ = require('lodash');
const math = require('./math.js');

// Use the math module
const sum = math.addition(5, 7);
console.log(`5 + 7 = ${sum}`);

const product = math.multiplication(5, 7);
console.log(`5 * 7 = ${product}`);

// Use lodash to demonstrate its utility
const array = [1, 2, 3, 4, 5];
const doubled = _.map(array, num => num * 2);
console.log(`Doubled array: ${doubled}`);
