# -*- coding: utf-8 -*-
{
    'name': "Stock inventory",
    'summary': """
        Ce module permet de faire un inventaire de stock""",

    'description': """
    Ce module permet de faire un inventaire de stock
    """,
    "author": "medconsultantweb@gmail.com",
    "website": "https://tunisie_innovation.tn",
    "license": "Other proprietary",

    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    "development_status": "Alpha",
	'price': 15,
	'currency': "EUR",
    # any module necessary for this one to work correctly
    'depends': ['base','purchase', 'sale', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_inventory_stock_views.xml',
        'reports/report_stockinventory.xml',
        'reports/report_stock_valorization.xml',
    ],

}
