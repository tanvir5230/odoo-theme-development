{
    'name': "Brand Slider",
    'summary': 'A module to display scrolling brand logos with an option to enable or disable the scrolling effect.',
    'description': """
    The Brand Slider module allows you to showcase brand logos in a slider format. 
    It features an optional scrolling effect that can be enabled or disabled as per the requirement.
    Perfect for highlighting brand partners or sponsors on your website.
    """,
    'version': '1.0',
    'category': 'Snippet',
    'depends': ['base', 'website'],
    'author': "Tanvir Ibn Touhid",
    'data': [
        'security/ir.model.access.csv',
        'views/snippets/snippet.xml',
        'views/snippets/brand_slider.xml',
        'views/brand_slider_views.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'snippet_brand_slider/static/src/css/brand_slider.css',
            'snippet_brand_slider/static/src/js/brand_slider_snippet.js',
            'snippet_brand_slider/static/src/js/brand_slider_snippet_options.js'
        ],
    },
    'images': [
        'static/src/img/*'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
