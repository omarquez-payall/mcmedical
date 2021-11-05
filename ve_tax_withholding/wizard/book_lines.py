# -*- coding: utf-8 -*-

from odoo import models, fields, api
class BookLinesWizard( models.TransientModel):
    _name = 'tax.purchases_book.lines_wizard'
    _description = 'Lines of purchases bill entry by period'

    related_book = fields.Many2one(comodel_name = 'tax.purchases_book_wizard')
    
    related_book_excel = fields.Many2one(comodel_name = 'report.ve_tax_withholding.report_book_excel')
    period = fields.Text(string='Periodo', default = '0')
    rif = fields.Char(string='RIF', default = '0')
    customer = fields.Char(string='Cliente', default = '0')
    prov_type = fields.Char(string='Tipo prov', default = '0')
    name = fields.Char(string = 'No de Documento')
    control_number = fields.Char(string = 'Numero de Control', default = '0')
    related_debit_note = fields.Char(string='No Nota de Debito', default = '0')
    related_credit_note = fields.Char(string='No Nota de Credito', default = '0')
    total_amount_with_taxes = fields.Float(string='Importe de factura', default = '0')
    untaxed_amount = fields.Float(string='Base Imponible', default = '0')
    
    tax_amount = fields.Float(string='Porcentaje de impuesto', default = '0')
    tax_amount_held = related_debit_note = fields.Float(string='Total impuesto retenido', default = '0')
    advance_payment = fields.Float(string='Anticipo de impuesto', default = '0')