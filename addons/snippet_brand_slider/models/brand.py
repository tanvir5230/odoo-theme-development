from odoo import models, fields


class Brand(models.Model):
    _name = 'snippet_brand_slider.brand'
    _description = 'Brands'

    name = fields.Char(string='Brand Name', required=True)
    link = fields.Char(string='Brand Link', required=True)
    image = fields.Binary(string='Image', attachment=True)
