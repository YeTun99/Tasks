# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-6(http.Controller):
#     @http.route('/tid-6/tid-6', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-6/tid-6/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-6.listing', {
#             'root': '/tid-6/tid-6',
#             'objects': http.request.env['tid-6.tid-6'].search([]),
#         })

#     @http.route('/tid-6/tid-6/objects/<model("tid-6.tid-6"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-6.object', {
#             'object': obj
#         })
