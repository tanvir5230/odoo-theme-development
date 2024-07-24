/** @odoo-module **/

import { Component, useState } from "@odoo/owl"
import { HelloWorld } from "./helloWorld";
import { Counter } from "./counter/counter";
import { Todo } from "./todo/todo";

export class App extends Component {
  static template = "owl_tutorial.App";
  static components = { HelloWorld, Counter, Todo };

  setup() {
    this.state = useState({
      todo: []
    })
    this.addTodo = this.addTodo.bind(this);
  }

  addTodo(ev) {
    const inputText = ev.target.value;
    if (ev.keyCode === 13) {
      if (inputText.length > 0) {
        const newTodo = { id: this.state.todo.length + 1, name: inputText, isCompleted: false };
        this.state.todo = [...this.state.todo, newTodo];
        ev.target.value = '';
      }
    }
  }

  toggleState(id) {

  }

}