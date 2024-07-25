{
    'name': "Snippet Partners",
    'description': """
      Snippet Partners
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
            'snippet_brand_slider/static/src/js/brand_slider_snippet.js'
        ],
    },
    'images': [
        'static/src/img/*'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
