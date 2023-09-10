
const GIPHY_ENDPOINT = 'https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';


fetch(GIPHY_ENDPOINT)
    .then(response => {

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {

        console.log(data);


    })
    .catch(error => {

        console.error('Fetch error:', error.message);
    });


    async function fetchStarship() {
        try {
            const response = await fetch("https://www.swapi.tech/api/starships/9/");
    
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
    
            const objectStarWars = await response.json();
            console.log(objectStarWars.result);
    
        } catch (error) {
            console.error('Error fetching starship:', error.message);
        }
    }
    
    fetchStarship();
    