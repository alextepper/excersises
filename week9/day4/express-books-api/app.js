// app.js

const express = require('express');
const bookRoutes = require('./routes/books');

const app = express();
const PORT = 3000;

app.use(express.json()); // Middleware to parse JSON request body
app.use('/books', bookRoutes); // Use the book routes

app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});
