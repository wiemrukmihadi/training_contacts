# -*- coding: utf-8 -*-
{
    'name': "TrainingContacts",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "phaalawnbreotpneg",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contact',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/trainingcontacts_approval_view.xml',
        'views/purchase_order_view.xml',
        'views/trainingcontacts_approval_view.xml',
        'views/trainingcontacts_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

