# This file is part of an Adiczion's Module.
# The COPYRIGHT and LICENSE files at the top level of this repository
# contains the full copyright notices and license terms.
{
    'name': 'Delivery Common',
    'version': '14.0.1',
    'author': 'Adiczion SARL',
    'category': 'Adiczion',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'delivery',
    ],
    'demo': [],
    'website': 'http://adiczion.com',
    'description': """
Delivery Common
===============

Does nothing on its own, addition of fields and libraries for use by modules
which depend on him, mainly:

   * a4o_delivery_colissimo
   * a4o_delivery_maydelivengo
   * a4to_delivery_chronopost

    """,
    'data': [
        # 'security/objects_security.xml',
        # 'security/ir.model.access.csv',
        # 'wizard/your_wizard_name.xml',
        # 'data/data_for_your_module.xml',
        'views/stock_quant_views.xml',
        'views/delivery_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
