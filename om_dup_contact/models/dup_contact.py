from odoo import models,fields

class DupContact(models.Model):
    _name='dup.contact'

    name = fields.Char("Name")
