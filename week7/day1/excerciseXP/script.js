function displayNumbersDivisibleBy(divisor) { 
    let sum = 0;
    let numbers = [];

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            sum += i;
            numbers.push(i);
        }
    }

    console.log(`Outcome: ${numbers.join(" ")}`);
    console.log(`Sum: ${sum}`);
}

displayNumbersDivisibleBy(23);


const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
} 

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;
    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            total += prices[item];
            stock[item]--; 
        }
    }
    return total;
}

console.log(myBill()); 

function changeEnough(itemPrice, amountOfChange) {
    const totalChange = (amountOfChange[0] * 0.25) + 
                        (amountOfChange[1] * 0.10) + 
                        (amountOfChange[2] * 0.05) + 
                        (amountOfChange[3] * 0.01);
    
    return totalChange >= itemPrice;
}


function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    if (destination === "London") {
        return 183;
    } else if (destination === "Paris") {
        return 220;
    } else {
        return 300;
    }
}


function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) {
        cost = cost * 0.95; 
    }
    return cost;
}


function totalVacationCost() {
    
    let nights;
    while (isNaN(nights) || nights === null) {
        nights = parseInt(prompt("How many nights would you like to stay in the hotel?"));
    }
    const hotelTotal = hotelCost(nights);

    
    let destination = "";
    while (!destination || typeof destination !== "string") {
        destination = prompt("Where is your destination? (e.g., London, Paris)");
    }
    const planeTotal = planeRideCost(destination);

    let days;
    while (isNaN(days) || days === null) {
        days = parseInt(prompt("How many days would you like to rent the car?"));
    }
    const carTotal = rentalCarCost(days);
    const totalCost = hotelTotal + planeTotal + carTotal;
    const result = `The car cost: $${carTotal}, the hotel cost: $${hotelTotal}, the plane tickets cost: $${planeTotal}. Total: $${totalCost}`;
    console.log(result);
    return totalCost;
}

totalVacationCost();


