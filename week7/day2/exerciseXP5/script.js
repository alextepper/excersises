
const form = document.getElementById("MyForm");
const radiusInput = document.getElementById("radius");
const volumeInput = document.getElementById("volume");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    
    const radius = parseFloat(radiusInput.value);
    if (isNaN(radius)) {
        alert("Please enter a valid number for radius.");
        return;
    }

    const volume = (4/3) * Math.PI * Math.pow(radius, 3);
    volumeInput.value = volume.toFixed(4);
});

form.addEventListener("click", function() {
    this.style.backgroundColor = "lightblue";
});

form.addEventListener("mouseover", function() {
    this.style.fontSize = "1.1em";
});

form.addEventListener("mouseout", function() {
    this.style.fontSize = "1em";
    this.style.backgroundColor = "transparent";
});

form.addEventListener("dblclick", function() {
    this.style.transform = "scale(1.1)";
});