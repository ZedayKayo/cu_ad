from odoo import models,fields

class HrEmployee(models.Model):
    _inherit=['hr.employee']

    em_prenom = fields.Char(string="Prénom")
    em_matricule = fields.Char(string="Matricule")
    em_cin = fields.Char(string="CIN")


