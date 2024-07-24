{
    'name': "Odoo Tutorial",
    'version': '1.0',
    'depends': ['website'],
    'author': "Tanvir Ibn Touhid",
    'category': 'Tutorial',
    'description': "Tutorial",
    'data': [
        'views/templates.xml'
    ],
    'application': True,
    'installable': True,
    'assets': {
        'owl_tutorial.assets_tutorial': [
            # bootstrap
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/src/legacy/js/promise_extension.js',
            'web/static/src/boot.js',
            'web/static/src/env.js',
            'web/static/src/session.js',
            'web/static/lib/owl/owl.js',  # owl library
            'web/static/lib/owl/odoo_module.js',  # to be able to import "@odoo/owl"
            'web/static/src/core/utils/functions.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/assets.js',
            'owl_tutorial/static/src/**/*',
        ]
    }
}
