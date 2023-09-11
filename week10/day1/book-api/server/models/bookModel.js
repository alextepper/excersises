const db = require('../config/db');

const getAllBooks = async () => {
    return await db.select('*').from('books');
};

const getBookById = async (id) => {
    return await db.select('*').from('books').where({ id }).first();
};

const addBook = async (book) => {
    const { title, author, publishedYear } = book;
    return await db('books').insert({
        title: title,
        author: author,
        publishedyear: publishedYear
    })
    .returning('*')
    .then(rows => rows[0])
    .catch(err => console.log(err.message));
};

module.exports = { getAllBooks, getBookById, addBook };
