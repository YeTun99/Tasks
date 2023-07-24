# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-1(http.Controller):
#     @http.route('/tid-1/tid-1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-1/tid-1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-1.listing', {
#             'root': '/tid-1/tid-1',
#             'objects': http.request.env['tid-1.tid-1'].search([]),
#         })

#     @http.route('/tid-1/tid-1/objects/<model("tid-1.tid-1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-1.object', {
#             'object': obj
#         })
