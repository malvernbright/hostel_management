from odoo import fields, models, api


class HostelStudent(models.Model):
    _name = 'hostel.student'
    _description = 'Hostel Student'

    name = fields.Char("Student Name")
    gender = fields.Selection(selection=[("male", "Male"),
                                         ("female", "Female"),
                                         ("other", "Other")],
                              string="Gender", help="Student Gender")
    active = fields.Boolean("Active", default=True,
                            help="Activate/Deactivate hostel record")
    room_id = fields.Many2one("hostel.room", "Room",
                              help="Select Hostel room")
