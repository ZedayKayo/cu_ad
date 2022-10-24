from odoo import models,fields

class ResPartner(models.Model):
    _inherit=['res.partner','hr.employee']

    con_prenom = fields.Char(string="Prénom")
    con_age = fields.Char(string="Age")
    con_n_cin = fields.Char(string="N° CIN")

    em_prenom = fields.Char(string="Prénom")
    em_matricule = fields.Char(string="Matricule")



    
