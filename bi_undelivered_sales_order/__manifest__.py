# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Undelivered Sales Order",
    "version" : "16.0.0.1",
    "category" : "Sales",
    'summary': 'Sales Order Undelivered Sale Order order Undelivered order Sales Undelivered product filter Undelivered sales order product Undelivered SO Undelivered Sales Undelivered order group by Undeliver Sales non complete so late sales delivery late sale delivery',
    "description": """
    		This odoo app helps user to quickly find undelivered sales order. User can see all undelivered sales order line and quantity, invoiced quantity and delivered quantity, discounts of sale order, User can filter undelivered sales order by order date, Also can group by undelivered sale order with order, order customer and order products and view in form view also.
    		
    	Undelivered Orders
    	Undelivered Sales Orders
    	Filter Undelivered Orders
    	Group By Undelivered Orders
    	Filter Undelivered Sales Orders
    	Group By Undelivered Sales Orders
    
    """,
    "author": "BrowseInfo",
    'website': 'https://www.browseinfo.in',
    "depends" : ['base','sale_management','stock'],
    "data": [
        'views/view_undelivered_so.xml',
    ],
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/uXFq_ReGEe4',
    "images":["static/description/Banner.gif"],
    'license': 'OPL-1',
}

