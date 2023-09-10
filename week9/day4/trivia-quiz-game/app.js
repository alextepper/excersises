// app.js

const express = require('express');
const quizRoutes = require('./routes/quiz');
const app = express();
const PORT = 3000;

app.use(express.json()); // Parse JSON request body
app.use(quizRoutes);

app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});
