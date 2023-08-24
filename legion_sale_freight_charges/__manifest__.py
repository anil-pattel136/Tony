# -*- coding: utf-8 -*-

{
    "name": "Sale Freight Charges",
    'version': '16.0.0.0',
    "author": "Bytelegion",
    "website": "http://www.bytelegions.com",
    'depends': ['base', 'sale'],
    'license': 'LGPL-3',
    "category": 'Global Sales freight charges',
    'company': 'Bytelegion',
    "summary": 'Global Sales freight charges',
    "description": """This module provides the feature to calculate Freight Charges on sale orders and Invoice. Apply freight charges on overall sale order.""",

    'data': [
        'views/sale_and_invoice_view.xml',
        # 'report/sales_invoice_report.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png', 'static/description/Snap_1.jpeg'],
    'images': ['static/description/banner.gif']

}
