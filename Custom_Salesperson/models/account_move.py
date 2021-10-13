# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'
    
    salesperson_id = fields.Many2one(comodel_name='custom_salesperson.salesperson', string='Vendedor', ondelete='set null')