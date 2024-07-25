from odoo import models, fields


class Brand(models.Model):
    _name = 'brand.image'
    _description = 'Brand Image'

    name = fields.Char(string='Brand Name', required=True)
    image = fields.Binary(string='Image', attachment=True)
