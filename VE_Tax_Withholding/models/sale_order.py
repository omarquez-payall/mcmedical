# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder( models.Model):
    _inherit = 'sale.order'
    
    related_vendor = fields.Selection(string='Vendedor',
                             selection=[('Karen Ramirez', 'Karen Ramirez'),
                                       ('Miguel Duran', 'Miguel Duran'),
                                       ('Mercado Libre', 'Mercado Libre'),
                                       ('Instagram', 'Instagram'),
                                       ('Dainet Chauran', 'Dainet Chauran')],
                             copy=False)
                                                