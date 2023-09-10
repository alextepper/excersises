const express = require('express');
const app = express();

app.use(express.json());

let books = [
  { id: 1, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', publishedYear: 1925 },
  { id: 2, title: 'Moby Dick', author: 'Herman Melville', publishedYear: 1851 }
];

app.get('/api/books', (req, res) => {
  res.json(books);
});

app.get('/api/books/:bookId', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.bookId));
  
  if (!book) {
    return res.status(404).send('Book not found');
  }

  res.json(book);
});

app.post('/api/books', (req, res) => {
  const newBook = {
    id: books.length + 1, 
    title: req.body.title,
    author: req.body.author,
    publishedYear: req.body.publishedYear
  };

  books.push(newBook);
  res.status(201).json(newBook);
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
