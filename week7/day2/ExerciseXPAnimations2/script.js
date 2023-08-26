function myMove() {
    const animate = document.getElementById("animate");
    const containerWidth = 400; // Width of the container as defined in the CSS
    const boxWidth = 50; // Width of the animate box as defined in the CSS

    let pos = 0;  // Starting position
    const id = setInterval(frame, 1);  // Move the box every millisecond

    function frame() {
        if (pos >= containerWidth - boxWidth) {  // Check if box has reached or exceeded the end of the container
            clearInterval(id);  // Stop the box from moving
        } else {
            pos++;  // Increase the position by 1 pixel
            animate.style.left = pos + "px";  // Move the box to the new position
        }
    }
}