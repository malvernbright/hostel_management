# -*- coding: utf-8 -*-

{
    'name': 'Hostel Management',
    'description': 'Hostel Management',
    'author': 'Malvern Gondo',
    'website': 'https://malvernbright.co.zw',
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        # SECURITY
        # 'security/hostel_security.xml',
        # 'security/hostel_room_security.xml',
        'security/ir.model.access.csv',

        # data
        'data/data.xml',
        # VIEWS
        'views/hostel.xml',
        'views/hostel_room.xml',
        'views/hostel_student.xml',
        'views/hostel_amenities.xml',
        'views/menuitems.xml',

        # REPORT
        'report/hostel_report.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
