from odoo import fields, models, api


class HostelRoom(models.Model):
    _name = 'hostel.room'
    _description = 'Hostel Room'

    name = fields.Char("Room Name")
    room_number = fields.Integer("Room Number")
    floor_number = fields.Integer("Floor Number")
    currency_id = fields.Many2one("res.currency", string="Currency")
    rent_amount = fields.Monetary("Rent Amount",
                                  help="Enter rent amount per month",
                                  currency_field="currency_id")
    hostel_id = fields.Many2one("hostel.hostel", "Hostel",
                                help="Name of the Hostel")
    student_ids = fields.One2many("hostel.student",
                                  "room_id", string="Students",
                                  help="Enter students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities",
                                            "hostel_room_amenities_rel",
                                            "room_id", string="Amenities",
                                            domain="[('active', '=', True)]",
                                            help="Select hostel room amenities")
