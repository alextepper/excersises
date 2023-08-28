const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];


colors.forEach((color, index) => {
    console.log(`${index + 1}# choice is ${color}.`);
});


if (colors.includes("Violet")) {
    console.log("Yeah");
} else {
    console.log("No...");
}

const ordinal = ["th","st","nd","rd"];

colors.forEach((color, index) => {
    let suffix = 
        (index + 1) > 3 ? ordinal[0] : 
        ordinal[index + 1];
    
    console.log(`${index + 1}${suffix} choice is ${color}.`);
});