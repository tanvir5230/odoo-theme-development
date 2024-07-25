from odoo import http
from odoo.http import request, Response
import json


class BrandImageAPI(http.Controller):

    @http.route('/api/brands/get', type='json', auth='public', methods=['POST'], website=True)
    def get(self):
        brands = request.env['brand.image'].sudo().search([])
        brand_data = []

        for brand in brands:
            image_data = {
                'name': brand.name,
                'image': brand.image.decode("utf-8") if brand.image else ""
            }
            brand_data.append(image_data)

        return {
            "status": "success",
            "images": brand_data
        }
