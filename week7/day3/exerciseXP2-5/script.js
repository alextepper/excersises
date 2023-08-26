const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

const isString = value => typeof value === 'string';

const sum = (a, b) => a + b;

function kgToGramsDeclaration(kg) {
    return kg * 1000;
}

const kgToGramsExpression = function(kg) {
    return kg * 1000;
}

// A function declaration defines a named function and can be hoisted, allowing it to be used before it's defined. A function expression defines a function as part of a larger expression syntax (typically a variable assignment). Functions defined by function expressions aren't hoisted, which means that you can't use them before they're defined.

const kgToGramsArrow = kg => kg * 1000;
