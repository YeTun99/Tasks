from odoo import fields,models,api

class CustomerCode(models.Model):
    _inherit="res.partner"

    customer_code=fields.Char(string="Customer Code")
    @api.model
    def create(self,vals_list):
        if self._context.get('search_default_customer',False):
            vals_list['customer_code']=self.env['ir.sequence'].next_by_code('customer_code_seq') or '/'
        return super().create(vals_list)