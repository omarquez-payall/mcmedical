# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomSalesperson( models.Model):
    _name = 'custom_salesperson.salesperson'
    _description = 'Salesperson information'


    name = fields.Char(string='Nombre', required=True)
    
    description = fields.Text(string='Descripcion')
    
    active = fields.Boolean(string='Activo', default=True)