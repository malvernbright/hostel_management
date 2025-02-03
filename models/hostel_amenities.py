from email.policy import default

from odoo import fields, models, api


class HostelAmenities(models.Model):
    _name = 'hostel.amenities'
    _description = 'Hostel amenities'

    name = fields.Char("Name", help="Provided hostel amenities")
    active = fields.Boolean("Active", default=True,
                            help="Activate/Deactivate whether the amenity should be given or not")
