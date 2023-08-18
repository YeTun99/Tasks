# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-4(http.Controller):
#     @http.route('/tid-4/tid-4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-4/tid-4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-4.listing', {
#             'root': '/tid-4/tid-4',
#             'objects': http.request.env['tid-4.tid-4'].search([]),
#         })

#     @http.route('/tid-4/tid-4/objects/<model("tid-4.tid-4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-4.object', {
#             'object': obj
#         })
