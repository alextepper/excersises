const express = require('express');
const router = express.Router();
const triviaQuestions = require('../model');

let currentQuestion = 0;
let score = 0;

router.get('/quiz', (req, res) => {
    if (currentQuestion < triviaQuestions.length) {
        res.json(triviaQuestions[currentQuestion]);
    } else {
        res.json({ message: 'Quiz finished. Check your score!' });
    }
});

router.post('/quiz', (req, res) => {
    const userAnswer = req.body.answer;
    
    if (userAnswer === triviaQuestions[currentQuestion].answer) {
        score++;
        res.json({ message: 'Correct!' });
    } else {
        res.json({ message: 'Incorrect!' });
    }

    currentQuestion++;
    
    if (currentQuestion < triviaQuestions.length) {
        res.json(triviaQuestions[currentQuestion]);
    } else {
        res.json({ message: 'Quiz finished. Check your score!' });
    }
});

router.get('/quiz/score', (req, res) => {
    res.json({ score: score });
});

module.exports = router;
