const express = require('express');
const router = express.Router();

// Sample in-memory database for storing to-do items
const todos = [];

router.get('/todos', (req, res) => {
    res.json(todos);
});

router.post('/todos', (req, res) => {
    const todo = req.body;
    todos.push(todo);
    res.json(todo);
});

router.put('/todos/:id', (req, res) => {
    const id = req.params.id;
    const updatedTodo = req.body;
    const index = todos.findIndex(todo => todo.id === parseInt(id));
    todos[index] = updatedTodo;
    res.json(updatedTodo);
});

router.delete('/todos/:id', (req, res) => {
    const id = req.params.id;
    const index = todos.findIndex(todo => todo.id === parseInt(id));
    todos.splice(index, 1);
    res.json({ message: `Todo with ID: ${id} deleted.` });
});

module.exports = router;
