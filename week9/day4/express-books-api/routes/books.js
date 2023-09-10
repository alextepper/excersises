// routes/books.js

const express = require('express');
const router = express.Router();

// Sample in-memory database for storing books
const books = [];

router.get('/', (req, res) => {
    res.json(books);
});

router.post('/', (req, res) => {
    const book = req.body;
    books.push(book);
    res.json(book);
});

router.put('/:id', (req, res) => {
    const id = req.params.id;
    const updatedBook = req.body;
    const index = books.findIndex(book => book.id === parseInt(id));
    if (index !== -1) {
        books[index] = updatedBook;
        res.json(updatedBook);
    } else {
        res.status(404).json({ message: 'Book not found' });
    }
});

router.delete('/:id', (req, res) => {
    const id = req.params.id;
    const index = books.findIndex(book => book.id === parseInt(id));
    if (index !== -1) {
        books.splice(index, 1);
        res.json({ message: `Book with ID: ${id} deleted.` });
    } else {
        res.status(404).json({ message: 'Book not found' });
    }
});

module.exports = router;
