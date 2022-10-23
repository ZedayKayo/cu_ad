# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital-Management',
    'version': '1.3',
    'category': 'Hidden',
    'description': """
Hospital.
===================================================
""",
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
    ],
    'sequence':'-100',
    'demo': [
    ],
    'test': [],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}
