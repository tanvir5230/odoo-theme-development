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
      this._renderBrands(data.images)
    }
  },

  _renderBrands(images) {
    const container = this.$('.brand-slider-inner');
    container.empty(); // Clear existing content for efficiency

    const imgElements = images
      .filter((brand) => brand.image) // Filter for brands with images
      .map((brand) => {
        const imgSrc = 'data:image/png;base64,' + brand.image;
        return `<img src="${imgSrc}" alt="${brand.name}" class="brand" width="100px" height="100px">`;
      });

    container.append(imgElements.join(''), imgElements.join(''));
  },
});

export default publicWidget.registry.brandItems;
