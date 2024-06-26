# -*- coding: utf-8 -*-
{
    'name': "odoo_inheritance",

    'description': """
        Módulo para modificar y mejorar los módulos predeterminados de odoo
    """,

    'sequence': -1200,
    'author': "nico",
    'application': True,
    'installable': True,
    'auto_install': False,

    'category': 'Sin Categoría',
    'version': '1.0',

    'depends': [
        'sale', 'sale_management'
    ],

    'data': [
        'views/sale_order_view.xml',
    ],
    'demo': [
    ],
    'license': 'LGPL-3',  # Esta es la que viene por defecto

}
