from odoo import fields,api,models

class InventoryReport(models.Model):
    _inherit = "stock.quant"
  
    product_new_field=fields.Char(string="Product Name" ,related='product_id.name',store=True)
