from odoo import models, fields, api




class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'


    name = fields.Char(string='Title', required=True)
    image = fields.Binary(string='Upload Image')
    description = fields.Text(string='Description')
    location = fields.Char(string='Location')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(copy=False,default=fields.Date.today)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', copy=False)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Number of Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    active = fields.Boolean(string='Active', default=True)
    property_type_id = fields.Many2one('real.estate.property.type', string='Property Type')
    owner = fields.Many2one('property.owner', string='Owner', copy=False)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='Status', default='new', copy=False, required=True)



    def action_open_sold_wizard(self):
        return {
            'name': 'Mark as Sold',
            'type': 'ir.actions.act_window',
            'res_model': 'real.estate.property.sold.to.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_property_id': self.id,
                'default_expected_price': self.expected_price,
            }
        }

    def action_cancel(self):
        for record in self:
            record.state = 'canceled'

    def action_offer_received(self):
        for record in self:
            record.state = 'offer_received'

    def action_accept_offer(self):
        for record in self:
            record.state = 'offer_accepted'

