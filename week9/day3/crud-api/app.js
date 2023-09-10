const express = require('express');
const { fetchPosts } = require('./data/dataService');
const app = express();

app.get('/api/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log('Data successfully retrieved and sent as a response.');
    res.json(posts);
  } catch (error) {
    res.status(500).send('Server Error');
  }
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
