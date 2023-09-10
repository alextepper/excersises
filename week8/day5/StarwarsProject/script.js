document.addEventListener('DOMContentLoaded', function() {
    const loadCharacterBtn = document.getElementById('loadCharacter');
    const loader = document.querySelector('.loader');
    const errorMessage = document.querySelector('.error-message');
    const characterInfo = document.querySelector('.character-info');

    const name = document.getElementById('name');
    const height = document.getElementById('height');
    const gender = document.getElementById('gender');
    const birthYear = document.getElementById('birthYear');
    const homeWorld = document.getElementById('homeWorld');

    loadCharacterBtn.addEventListener('click', loadRandomCharacter);

    function loadRandomCharacter() {
        const randomId = Math.floor(Math.random() * 83) + 1;

        loader.style.display = 'block';
        characterInfo.style.display = 'none';
        errorMessage.textContent = '';

        fetch(`https://www.swapi.tech/api/people/${randomId}`)
            .then(response => response.json())
            .then(data => {
                if (data.result) {
                    name.textContent = data.result.properties.name;
                    height.textContent = data.result.properties.height;
                    gender.textContent = data.result.properties.gender;
                    birthYear.textContent = data.result.properties.birth_year;

                    return fetch(data.result.properties.homeworld)
                } else {
                    throw new Error("Failed to fetch character");
                }
            })
            .then(response => response.json())
            .then(data => {
                homeWorld.textContent = data.result.properties.name;
                loader.style.display = 'none';
                characterInfo.style.display = 'block';
            })
            .catch(err => {
                loader.style.display = 'none';
                errorMessage.textContent = 'Failed to load character. Please try again.';
            });
    }
});
