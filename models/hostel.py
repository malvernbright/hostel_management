# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'Hostel management'
    _order = 'id desc, name'
    _rec_name = 'hostel_code'
    _rec_names_search = ['name', 'hostel_code']

    name = fields.Char(string="Hostel Name")
    hostel_code = fields.Char(string="Code")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    state_id = fields.Many2one("res.country.state", string="State")
    zip = fields.Char(string='Zip', change_default=True)
    city = fields.Char(string="City")
    country_id = fields.Many2one("res.country", string="Country")
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary(string="Hostel Image")
    active = fields.Boolean(string="Active", default=True,
                            help="Activate/Deactivate Hostel record")
    type = fields.Selection(selection=[("male", "Boys"),
                                       ("female", "Girls"),
                                       ("common", "Common")],
                            required=True, default="common",
                            help="Type of Hostel")
    other_info = fields.Text(string="Other information",
                             help="Enter more information")
    description = fields.Html("Description", sanitize=True)
    hostel_rating = fields.Float("Hostel average rating",
                                 digits="Rating Value")

    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f'{name} ({record.hostel_code})'
            record.display_name = name
