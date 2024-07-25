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
        'views/snippets/partners.xml',
        'views/brand.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'snippet_brand_slider/static/src/css/partners.css',
            'snippet_brand_slider/static/src/js/brand_snippet.js'
        ],
    },
    'images': [
        'static/src/img/*'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
