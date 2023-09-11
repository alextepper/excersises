const express = require('express');
const postsRoutes = require('./server/routes/posts');
const app = express();
const port = 3000;


app.use(express.json());
app.use('/posts', postsRoutes);

app.use(function(req, res, next) {
    res.status(404).json({ error: "Not Found" });
});

app.use((req, res, next) => {
    const error = new Error('Not Found');
    error.status = 404;
    next(error);
});

app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({ error: error.message });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});



