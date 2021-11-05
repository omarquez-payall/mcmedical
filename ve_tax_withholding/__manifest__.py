# -*- coding: utf-8 -*-

{
    'name': 've - tax withholding',
    
    'summary': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'description': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'author': 'Payall',
    
    'website': 'https://payall.com.ve/',
    
    'category': 'Accounting',
    
    'version': '1.0.0',
    
    'depends': ['account_accountant','sale_management','report_xlsx'],
    
    'data': [
        "security/tax_withholding_security.xml",
        "security/ir.model.access.csv",
        "data/withholding_subjects_data.xml",
        "report/tax_withholding_report.xml",
        "report/tax_withholding_customer_report.xml",
        "report/tax_book_report.xml",
        "report/tax_book_excel_report.xml",
        "wizard/purchases_book_views.xml",
        "views/tax_withholding_subject_view.xml",
        "views/tax_withholding_views.xml",
        "views/tax_withholding_menuitems.xml",
        "views/account_move_inherit_view.xml",
        "views/tax_withholding_voucher_customer_views.xml",
        "views/tax_withholding_voucher_customer_menuitems.xml",
    ],
    
    'demo': [
        "data/withholding_subjects_demo.xml"
    ],
}