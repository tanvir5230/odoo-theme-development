from odoo import http
from odoo.http import request, route


class OwlTutorial(http.Controller):
    @http.route(['/owl_tutorial'], type='http', auth='public')
    def show_tutorial(self):
        return request.render('owl_tutorial.tutorial')
