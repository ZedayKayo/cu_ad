from odoo import models,fields

class ResPartner(models.Model):
    _inherit='res.partner'

    con_prenom = fields.Char(string="Prénom")
    con_age = fields.Char(string="Age")
z