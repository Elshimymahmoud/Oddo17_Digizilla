from odoo import fields, models

class CustomerData(models.Model):
    _name = 'dev.assessment.customer'
    _description = 'Customer Data for Assessment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', tracking=True)
    country_id = fields.Many2one('res.country', string='Country', tracking=True)
    joining_date = fields.Date(string='Joining Date', tracking=True)

    company_ids = fields.Many2many('res.company', string='Customer Companies', tracking=True)
    comment_notes = fields.Text(string='Notes/Comments')

    last_update_date = fields.Datetime(
        string='Last Update Date',
        readonly=True,
        default=fields.Datetime.now
    )

    def write(self, values):
        tracked_fields = ['name', 'gender', 'country_id', 'joining_date', 'company_ids']

        if any(field_name in values for field_name in tracked_fields):
            values['last_update_date'] = fields.Datetime.now()

        return super(CustomerData, self).write(values)