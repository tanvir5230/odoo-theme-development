{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Tanvir",
    'category': 'Technical',
    'description': """
    Real estate
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
