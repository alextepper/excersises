const express = require('express');
const todosRoutes = require('./routes/todos');

const app = express();
const PORT = 3000;

app.use(express.json());  // Middleware to parse JSON request body
app.use('/', todosRoutes);

app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});
