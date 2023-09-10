export class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    addTask(task) {
      this.tasks.push({ name: task, completed: false });
    }
  
    markComplete(taskName) {
      const task = this.tasks.find(t => t.name === taskName);
      if (task) {
        task.completed = true;
      } else {
        console.log('Task not found!');
      }
    }
  
    listAllTasks() {
      this.tasks.forEach(task => {
        console.log(`${task.name} - ${task.completed ? 'Completed' : 'Pending'}`);
      });
    }
  }
  