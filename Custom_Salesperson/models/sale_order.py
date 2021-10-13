# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    salesperson_id = fields.Many2one(comodel_name='custom_salesperson.salesperson', string='Vendedor', ondelete='set null')