document.getElementById('gifForm').addEventListener('submit', async event => {
    event.preventDefault();

    const searchTerm = document.getElementById('gifInput').value;
    const gifContainer = document.getElementById('gifsContainer');

    if (searchTerm) {
        try {
            const response = await fetch(`https://api.giphy.com/v1/gifs/random?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&tag=${searchTerm}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            const gifUrl = data.data.images.original.url;

            const gifElement = document.createElement('div');
            gifElement.innerHTML = `
                <img src="${gifUrl}" alt="${searchTerm} gif">
                <button onclick="deleteGif(this)">DELETE</button>
            `;

            gifContainer.appendChild(gifElement);
        } catch (error) {
            console.error('Error fetching gif:', error);
        }
    }
});

document.getElementById('deleteAll').addEventListener('click', () => {
    document.getElementById('gifsContainer').innerHTML = '';
});

function deleteGif(buttonElement) {
    buttonElement.parentElement.remove();
}
