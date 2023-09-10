const express = require('express');
const app = express();


app.use(express.json());


let posts = [
  { id: 1, title: 'First Blog Post', content: 'This is the content of the first post' },
  { id: 2, title: 'Second Blog Post', content: 'This is the content of the second post' }
];

// Routes

// GET all posts
app.get('/posts', (req, res) => {
  res.json(posts);
});

// GET specific post
app.get('/posts/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).send('Post not found.');
  res.json(post);
});

// POST new post
app.post('/posts', (req, res) => {
  const post = {
    id: posts.length + 1,
    title: req.body.title,
    content: req.body.content
  };
  posts.push(post);
  res.status(201).json(post);
});

// PUT (update) a post
app.put('/posts/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).send('Post not found.');

  post.title = req.body.title || post.title;
  post.content = req.body.content || post.content;

  res.json(post);
});

// DELETE a post
app.delete('/posts/:id', (req, res) => {
  const postIndex = posts.findIndex(p => p.id === parseInt(req.params.id));
  if (postIndex === -1) return res.status(404).send('Post not found.');

  posts.splice(postIndex, 1);
  res.status(204).send();
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
