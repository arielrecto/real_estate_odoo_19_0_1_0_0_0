# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyType(models.Model):
    _name = 'real.estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')