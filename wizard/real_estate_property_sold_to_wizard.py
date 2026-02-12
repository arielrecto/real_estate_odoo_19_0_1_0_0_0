# -*- coding: utf-8 -*-
from odoo import models, fields, api




class RealEstatePropertySoldToWizard(models.TransientModel):
    _name = 'real.estate.property.sold.to.wizard'
    _description = 'Real Estate Property Sold To Wizard'

    property_id = fields.Many2one('estate.property', string='Property', required=True, readonly=True)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', required=True)
    sold_to = fields.Many2one('res.partner', string='Sold To', required=True)
    date_sold = fields.Date(copy=False,default=fields.Date.today)
    agent_commission = fields.Float(string='Agent Commission (%)', default=6.0)

    def action_confirm_sold(self):
        active_id = self.env.context.get('active_id')
        property_record = self.env['estate.property'].browse(active_id)
        property_record.state = 'sold'
        property_record.owner = self.create_property_owner().id


    @api.onchange('property_id')
    def _compute_selling_price(self):
        for record in self:
            record.selling_price = record.property_id.selling_price


    @api.onchange('selling_price')
    def _compute_agent_commission(self):
        for record in self:
            record.agent_commission = (record.selling_price * 6) / 100


    def create_property_owner(self):
        owner = self.env['property.owner'].search([('partner_id', '=', self.sold_to.id)], limit=1)
        if not owner:
            owner = self.env['property.owner'].create({'partner_id': self.sold_to.id})
        return owner 
