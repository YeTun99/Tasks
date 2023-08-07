from odoo import fields,api,models

class OnHandQuantityMail(models.Model):
    _inherit="product.product"

    
    def mail_schedule_action(self):
        # product_quantity=[{
        #     'product':product.name,
       
        #     'quantity':product.qty_available
        
        # }for product in self.env["product.product"].search([])
        # ]
        product_quantity=[]

        for product in self.env["product.product"].search([]):          
            product_quantity.append({
                   'product':product.name,
                   'quantity':product.qty_available
            }                 
            )
        product1={
            'user':self.env.user.name,       
            'email_from':self.env.company.email,
            'email_to':self.env.user.email
        }

        self.env.ref('tid-10.mail_product_quantity').with_context(
            quantity=product_quantity, product=product1
        ).send_mail(self.id)
        return True