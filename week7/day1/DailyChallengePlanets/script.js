const planets = [
    {
        name: "Mercury",
        color: "gray",
        moons: 0
    },
    {
        name: "Venus",
        color: "goldenrod",
        moons: 0
    },
    {
        name: "Earth",
        color: "blue",
        moons: 1
    },
    {
        name: "Mars",
        color: "red",
        moons: 2
    },
    {
        name: "Jupiter",
        color: "orange",
        moons: 79
    },
    {
        name: "Saturn",
        color: "gold",
        moons: 82
    },
    {
        name: "Uranus",
        color: "lightseagreen",
        moons: 27
    },
    {
        name: "Neptune",
        color: "blueviolet",
        moons: 14
    }
];


const section = document.querySelector('.listPlanets');


planets.forEach(planet => {
    const planetDiv = document.createElement('div');
    planetDiv.classList.add('planet');
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;


    for (let i = 0; i < planet.moons; i++) {
        const moonDiv = document.createElement('div');
       

        moonDiv.classList.add('moon');
        
        
        moonDiv.style.left = `${i * 40}px`;
        moonDiv.style.top = `${i * 20}px`;

        planetDiv.appendChild(moonDiv);
    }

    section.appendChild(planetDiv);
});