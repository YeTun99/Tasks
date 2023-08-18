from odoo import fields,api,models

class EditedVersion(models.Model):
    _inherit="sale.order"

    edit_name=fields.Integer(default="0")

    # @api.model_create_multi
    # def create(self,vals_list):
       
    #     res=super().create(vals_list)
    #     if not self.order_name:
    #         order_name=vals_list[0]['name']
    #     return res

    def write(self,vals_list):

        # self.edit_name+=1
        if self.state=="sale":
            result=self.name.split(" ")[-1].replace("(","").replace(")","")
            vals_list['name']="Edited Version"+" "+"("+result+")" 
        return super().write(vals_list)
    
    # def name_get(self):
    #     result=[]
    #     for order in self:
    #         instrustors=order.teacher_ids.mapped('name')
    #         name_list =','.join(instrustors)    
    #         result.append((order.id,order.name+f"({name_list})"))
    #     return result