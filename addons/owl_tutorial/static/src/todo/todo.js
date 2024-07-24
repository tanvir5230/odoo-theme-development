/** @odoo-module **/

import { Component } from "@odoo/owl"
import { TodoList } from "./todoList";
import { useAutoFocus } from "../utils";

export class Todo extends Component {
  static props = {
    todo: {
      type: Array,
      element: {
        type: Object,
        shape: {
          id: Number,
          name: String,
          isCompleted: Boolean
        }
      }
    },
    addTodo: Function
  }
  setup() {
    useAutoFocus("input");
  }
  static template = "owl_tutorial.Todo";
  static components = { TodoList };
}