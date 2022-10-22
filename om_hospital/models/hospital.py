from email.policy import default
from odoo import fields,models,api





class HospitalPatient(models.Model):
    _name='hospital.patient'
    _description = 'hospital management system'

    _inherit=['mail.thread','mail.activity.mixin']

    pat_name= fields.Char('Full Name')
    pat_age= fields.Integer(string='Age',tracking=True)
    pat_gender= fields.Selection([
        ('male','Male'),
        ('female','Female')
    ],required=True,default='male',string='Gender')
    pat_img= fields.Binary('Image')
    responsible_id = fields.Many2one(comodel_name='res.partner',string='Responsible')


    state = fields.Selection([('draft','Draft'),('confirm','Confirmed'),
                              ('done','Done'),('cancel','Cancel')],default='draft',string='status',tracking=True)
    

    def action_confirm(self):
        self.state = 'confirm'
    def action_draft(self):
        self.state = 'draft'
    def action_done(self):
        self.state = 'done'
    def action_cancel(self):
        self.state = 'cancel'


    @api.model
    def create(self, vals_list):
        #check if patient age field is empty
        if not vals_list.get('pat_age'):
            vals_list['pat_age'] = 18
        res = super(HospitalPatient,self).create(vals_list)
        return res


    