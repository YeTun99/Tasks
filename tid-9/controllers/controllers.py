# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-9(http.Controller):
#     @http.route('/tid-9/tid-9', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-9/tid-9/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-9.listing', {
#             'root': '/tid-9/tid-9',
#             'objects': http.request.env['tid-9.tid-9'].search([]),
#         })

#     @http.route('/tid-9/tid-9/objects/<model("tid-9.tid-9"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-9.object', {
#             'object': obj
#         })
