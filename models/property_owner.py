# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PropertyOwner(models.Model):
    _name = 'property.owner'
    _description = 'Property Owner'
    _inherits = {'res.partner': 'partner_id'}


    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')

    property_ids = fields.One2many('estate.property', 'owner', string='Properties Owned')
    total_properties = fields.Integer(string='Total Properties', compute='_compute_total_properties')


    @api.depends('property_ids')
    def _compute_total_properties(self):
        for owner in self:
            owner.total_properties = len(owner.property_ids)
    


