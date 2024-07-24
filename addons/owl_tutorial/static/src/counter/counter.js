/** @odoo-module **/

import { Component, useState } from "@odoo/owl"

export class Counter extends Component {
  static template = "owl_tutorial.Counter";

  setup() {
    this.state = useState({
      counter: 0
    })
  }

  increment() {
    this.state.counter++;
  }
}