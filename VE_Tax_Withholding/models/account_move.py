# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove( models.Model):
    _inherit = 'account.move'


    control_number = fields.Char(string='Numero de control', required=True, default='0000')
    
    related_vendor = fields.Selection(string='Vendedor',
                             selection=[('Karen Ramirez', 'Karen Ramirez'),
                                       ('Miguel Duran', 'Miguel Duran'),
                                       ('Mercado Libre', 'Mercado Libre'),
                                       ('Instagram', 'Instagram'),
                                       ('Dainet Chauran', 'Dainet Chauran')],
                             copy=False)
                                                