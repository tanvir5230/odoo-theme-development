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
        'views/snippets/snippet.xml',
        'views/snippets/partners.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'snippet_partners/static/src/css/partners.css'
        ],
    },
    'images': [
        'static/src/img/*'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
