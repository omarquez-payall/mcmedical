# -*- coding: utf-8 -*-

{
    'name': 'Custom Salesperson',
    
    'summary': """
        This is a module to include a select-inputed field to the quotations, invoices and bills. 
    """,
    
    'description': """
        This is a module to include a select-inputed field to the quotations, invoices and bills.
    """,
    
    'author': 'Payall',
    
    'website': 'https://payall.com.ve/',
    
    'category': 'Sales',
    
    'version': '1.0.0',
    
    'depends': ['account_accountant','sale_management'],
    
    'data': [
        'security/salesperson_security.xml',
        'security/ir.model.access.csv',
        'views/custom_salesperson_menuitems.xml',
        'views/salesperson_views.xml',
        'views/sale_order_inherit.xml',
        'views/account_move_inherit.xml',
        'demo/custom_salesperson_demo.xml',
    ],
    
    'demo': [
        'demo/custom_salesperson_demo.xml',
    ],
}