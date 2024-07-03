/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class Todo extends Component {
  static template = "owl_playground.todo";

  setup() {
    this.state = useState({
      todos: [{ id: 1, name: "Brush Teeth", isCompleted: false }],
      taskInput: "",
    });
    this.removeTask = this.removeTask.bind(this);
  }

  addTask() {
    if (this.state.taskInput.trim().length > 0) {
      const newTask = {
        id: this.state.todos.length + 1,
        name: this.state.taskInput,
        isCompleted: false,
      };
      this.state.todos = [...this.state.todos, newTask];
    } else {
      alert("Please give an input...");
    }
  }

  removeTask(id) {
    this.state.todos = this.state.todos.filter((item) => item.id !== id);
  }
}
