(function(username) {
    const userDetailsDiv = document.getElementById('userDetails');

    const userNameDiv = document.createElement('div');
    userNameDiv.id = "userName";
    userNameDiv.innerText = username;

    const userImage = document.createElement('img');
    userImage.id = "userImage";
    userImage.src = "panda.jpg"; // Replace this with the actual path to the user's profile picture

    userDetailsDiv.appendChild(userNameDiv);
    userDetailsDiv.appendChild(userImage);

})('John');
