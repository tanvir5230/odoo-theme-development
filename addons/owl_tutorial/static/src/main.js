/** @odoo-module **/

import { mount } from "@odoo/owl"
import { templates } from "@web/core/assets"
import { App } from "./app"

owl.whenReady(() => {
  mount(App, document.body, { templates, dev: true })
})