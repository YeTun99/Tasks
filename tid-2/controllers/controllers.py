# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-2(http.Controller):
#     @http.route('/tid-2/tid-2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-2/tid-2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-2.listing', {
#             'root': '/tid-2/tid-2',
#             'objects': http.request.env['tid-2.tid-2'].search([]),
#         })

#     @http.route('/tid-2/tid-2/objects/<model("tid-2.tid-2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-2.object', {
#             'object': obj
#         })
