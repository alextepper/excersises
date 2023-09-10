const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' },
    // ... add more
];

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

app.get('/game', (req, res) => {
    const selectedEmoji = emojis[Math.floor(Math.random() * emojis.length)];

    const orderedChoices = [selectedEmoji.name, 'Cat', 'Burger', 'Tree'];

    const choices = shuffle(orderedChoices);

    res.render('game', {
        emoji: selectedEmoji.emoji,
        choices: choices
    });
});

app.post('/guess', (req, res) => {
    const userGuess = req.body.guess;
    
    res.redirect('/game');
});



const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
