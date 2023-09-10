const products = require('./products.js');

function findProductByName(productName) {
  const product = products.find(p => p.name === productName);
  return product;
}

const product1 = findProductByName('Laptop');
console.log(product1);  

const product2 = findProductByName('Shirt');
console.log(product2);  

const product3 = findProductByName('Coffee');
console.log(product3); 
