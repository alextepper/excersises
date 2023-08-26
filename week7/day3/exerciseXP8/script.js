function makeJuice(size) {
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        const output = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}.`;
        document.body.innerHTML += `<p>${output}</p>`;
    }

    addIngredients('apple', 'orange', 'banana');
}

makeJuice('large');

function makeJuice(size) {
    const ingredients = [];

    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    function displayJuice() {
        const output = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
        document.body.innerHTML += `<p>${output}</p>`;
    }

    addIngredients('apple', 'orange', 'banana');
    addIngredients('mango', 'pineapple', 'kiwi');
    displayJuice();
}

makeJuice('medium');
