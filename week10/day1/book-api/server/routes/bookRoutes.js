const express = require('express');
const router = express.Router();
const { getAllBooks, getBookById, addBook } = require('../models/bookModel');

router.get('/api/books', async (req, res) => {
    const books = await getAllBooks();
    res.json(books);
});

router.get('/api/books/:bookId', async (req, res) => {
    const bookId = parseInt(req.params.bookId, 10);
    const book = await getBookById(bookId);
    
    if (book) {
        res.json(book);
    } else {
        res.status(404).json({ message: 'Book not found' });
    }
});

router.post('/api/books', async (req, res) => {
    const newBook = await addBook(req.body);
    res.status(201).json(newBook);
});

module.exports = router;
