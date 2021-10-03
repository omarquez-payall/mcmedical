# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaxWithholdingVoucher( models.Model):

    _name = 'tax.withholding_voucher'
    _description = 'Tax Withholding Voucher Info'


    code = fields.Char( string = 'Identifier Code', required = True)

    subject = fields.Char( string = 'Concepto', required = True)

    notes = fields.Text( string = 'Internal Notes about Voucher')

    active = fields.Boolean( string = 'Active', default = True)

    related_invoice = fields.Many2one( string = 'Referencia de la Factura',
                                        comodel_name = 'account.move',
                                        required = True)

    amount_by_group = fields.Binary(string='Porcentaje de impuesto', related='related_invoice.amount_by_group')

    customer = fields.Many2one(string='Cliente', related='related_invoice.partner_id')

    tax_amount = fields.Float(string='Porcentaje de impuesto retenido', readonly=True)
    
    untaxed_amount = fields.Float(string='Base Imponible', readonly=True)
    
    taxed_amount_held = fields.Float(string='Impuesto Retenido', readonly=True)
    
    total_net_amount = fields.Float(string='Importe Neto', readonly=True)
    
    total_amount = fields.Float(string='Importe de factura', readonly=True)


    @api.onchange('related_invoice')
    def _onchange_tax_amount(self):
        for record in self:
            if record.amount_by_group:
                
                #record.amount_by_group.append(('0.00%', 0.0, 1.0, '0', '0',0 ,0))
                
                self.untaxed_amount = record.amount_by_group[1][2]
                
                self.taxed_amount_held = -record.amount_by_group[1][1]
                
                self.total_amount = self.untaxed_amount + record.amount_by_group[0][1]
                
                self.total_net_amount = self.total_amount - self.taxed_amount_held
                
                self.tax_amount = record.amount_by_group[1][1]*(-100/record.amount_by_group[1][2])
            else:
                self.tax_amount = 0.00
