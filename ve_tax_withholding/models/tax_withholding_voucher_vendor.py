# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaxWithholdingVoucherVendor( models.Model):

    _name = 'tax.withholding_voucher_vendor'
    _description = 'Tax Withholding Voucher Info'

    code = fields.Char( string = 'Codigo de la Retencion', required = True, index=True, default=lambda self: self._get_next_sequence_number() )
    subject = fields.Many2one( string = 'Concepto de la Retencion', comodel_name = 'tax.withholding_subject', required = True)
    notes = fields.Text( string = 'Internal Notes about Voucher')
    active = fields.Boolean( string = 'Activo', default = True)
    related_invoice = fields.Many2one( string = 'Referencia de la Factura', comodel_name = 'account.move', required = True)
    amount_by_group = fields.Binary(string='Porcentaje de impuesto',related='related_invoice.amount_by_group')
    tax_amount = fields.Float(string='Porcentaje de impuesto retenido', store=True )
    untaxed_amount = fields.Float(string='Base Imponible', store=True)
    taxed_amount_held = fields.Float(string='Impuesto Retenido', store=True)
    total_net_amount = fields.Float(string='Importe Neto' , store=True)
    total_amount = fields.Float(string='Importe de factura', store=True )
    period_date = fields.Date(string='Fecha de período', default=fields.Date.today, store=True)
    period = fields.Text(string='Periodo', store=True)
    creation_date = fields.Date(string='Fecha de creacion', default=fields.Date.today)
    
    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('ret_number')
        result = super(TaxWithholdingVoucherVendor, self).create(vals)
        return result 

    @api.model
    def _get_next_sequence_number(self):
        sequence = self.env['ir.sequence'].search([('code','=','ret_number')])
        next= sequence.get_next_char(sequence.number_next_actual)
        return next
    
    
    
    @api.onchange('period_date')
    def _compute_period(self):
        for record in self:
            months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
            
            self.period = months[record.period_date.month-1] + ' ' + str(record.period_date.year)



    @api.onchange('related_invoice')
    def _onchange_tax_amount(self):
        for record in self:
            if record.amount_by_group:
                
                record.amount_by_group.append(('0.00%', 0.0, 1.0, '0', '0',0 ,0))
                self.untaxed_amount = record.amount_by_group[1][2]
                self.taxed_amount_held = -record.amount_by_group[1][1]
                self.total_amount = self.untaxed_amount + record.amount_by_group[0][1]
                self.total_net_amount = self.total_amount - self.taxed_amount_held
                self.tax_amount = round(record.amount_by_group[1][1]*(-100/record.amount_by_group[1][2]))

            else:
                self.tax_amount = 0.00