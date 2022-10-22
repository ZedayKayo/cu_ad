from email.policy import default
from odoo import fields,models

class HospitalPatient(models.Model):
    _name='hospital.patient'
    _description = 'hospital management system'

    _inherit=['mail.thread','mail.activity.mixin']

    pat_name= fields.Char('Full Name')
    pat_age= fields.Integer('Age')
    pat_gender= fields.Selection([
        ('male','Male'),
        ('female','Female')
    ],required=True,default='male',string='Gender')
    pat_img= fields.Binary('Image')



    