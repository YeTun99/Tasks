from odoo import fields,api,models

class CustomerFormReference(models.Model):
    _name="customer.form"
    _description="Customer Reference"
    _rec_name="customer_name"

    customer_reference_form=fields.Char(string='Customer Reference')
    nrc_no=fields.Char(string="NRC")
    customer_name=fields.Many2one('res.partner')
    address_no=fields.Text(string='Address')