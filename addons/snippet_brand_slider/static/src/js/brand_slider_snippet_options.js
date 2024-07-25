odoo.define("brand_slider_snippet.options", function (require) {
  "use strict";

  const options = require("web_editor.snippets.options");

  options.registry.BrandSliderSnippetScrollOption = options.Class.extend({
    start: function () {
      console.log("Hello frotm options");
    },
    selectClass: function (ev) {
      console.log("helllo")
      // ev.preventDefault();
      // var $button = $(ev.currentTarget);
      // var selectClass = $button.data('select-class');
      // this.$sBrands.toggleClass('s_brands_scroll_yes', selectClass === 's_brands_scroll_yes');
      // this.$sBrands.toggleClass('s_brands_scroll_no', selectClass === 's_brands_scroll_no');
    },
  });

});
