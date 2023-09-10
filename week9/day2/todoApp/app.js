import { TodoList } from './todo.js';

const todoList = new TodoList();

// Add tasks
todoList.addTask('Buy groceries');
todoList.addTask('Go to the gym');
todoList.addTask('Read a book');

// Mark 'Go to the gym' as complete
todoList.markComplete('Go to the gym');

// List all tasks
todoList.listAllTasks();
