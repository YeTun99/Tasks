from odoo import fields,api,models

class EditedVersion(models.Model):
    _inherit="sale.order"

   
    def write(self,vals_list):
        result=self.name.split(" ")[-1].replace("(","").replace(")","")
    
        vals_list['name']=(self.env['ir.sequence'].next_by_code('edited_version')+" "+"("+result+")" or '/')
        return super().write(vals_list)
    
    # def name_get(self):
    #     result=[]
    #     for order in self:
    #         instrustors=order.teacher_ids.mapped('name')
    #         name_list =','.join(instrustors)    
    #         result.append((order.id,order.name+f"({name_list})"))
    #     return result