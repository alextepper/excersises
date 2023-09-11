const express = require('express');
const app = express();
const PORT = 3000;
const db = require('./server/config/db')
const userController = require('./server/controllers/userController')

app.set("db", db);
app.use(express.json());

app.get('/users', userController.getUsers);
app.post('/register', userController.register);
app.post('/login', userController.login);
app.get('/users/:id', userController.getUserById);
app.put('/users/:id', userController.updateUser);


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
