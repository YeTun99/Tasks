# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-10(http.Controller):
#     @http.route('/tid-10/tid-10', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-10/tid-10/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-10.listing', {
#             'root': '/tid-10/tid-10',
#             'objects': http.request.env['tid-10.tid-10'].search([]),
#         })

#     @http.route('/tid-10/tid-10/objects/<model("tid-10.tid-10"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-10.object', {
#             'object': obj
#         })
