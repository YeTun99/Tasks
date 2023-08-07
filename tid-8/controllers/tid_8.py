from odoo import http   
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager 



class Main(http.Controller):

    def pager_info(self,pager,count):
        return{
            "page_count":pager["page_count"],
            "item_count":count,
            "self":{
                "url":pager['page']['url']},
            "first":{
                "url":pager['page_first']['url']},
            "prev":{
                "url":pager['page_previous']['url']},
            "next":{
                "url":pager['page_next']['url']},
            "last":{
                "url":pager['page_last']['url']}
        }

    @http.route(["/api/v1/contact",'/api/v1/contact/page/<int:page>'],type="json",auth="none",methods=['POST'],csrf=False)
    def contacts_json(self,page=1):
        contact_count=request.env['res.partner'].sudo().search_count([])
        pager= portal_pager(url="/api/v1/contact",total=contact_count,page=page,step=10)
        contact_list= request.env['res.partner'].sudo().search_read([],fields=['name'],limit=10,offset=pager['offset'])
        if pager['page_count'] < page:
            links={}
            contact_list= []
        else:
            links= self.pager_info(pager,contact_count)
            # Links =pager
        
        data={"Links":links,"status":200,"data":contact_count,'contact_list':contact_list}
        return data
        
    



  