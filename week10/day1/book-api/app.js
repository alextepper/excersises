const express = require('express');
const bookRoutes = require('./server/routes/bookRoutes');

const app = express();

app.use(express.json());
app.use(bookRoutes);

app.listen(5000, () => {
    console.log('Server is running on port 5000');
});
