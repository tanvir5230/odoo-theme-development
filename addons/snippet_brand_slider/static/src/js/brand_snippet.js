/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.brandItems = publicWidget.Widget.extend({
  selector: '.s_brands',

  start() {
    console.log('brand snippet ready');
    this._fetchBrandImages();
  },

  async _fetchBrandImages() {
    const data = await this._rpc({
      route: "/api/brands/get",
      params: {}
    })
    if (data && data?.status === "success") {
      this._renderBrands(data)
    }
  },

  _renderBrands(data) {
    const container = this.$('.brand-slider-inner');
    if (data.images.length === 0) {
      container.text("Please upload brands!!!")
    } else {
      data.images.forEach(brand => {
        if (brand.image) {
          const imgSrc = 'data:image/png;base64,' + brand.image;
          const imgElement = `<img src="${imgSrc}" alt="${brand.name}" class="brand" style="width:100px;height:100px;">`;
          container.append(imgElement);
        }
      });
    }
  },
});

export default publicWidget.registry.brandItems;
