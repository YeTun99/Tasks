# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-3(http.Controller):
#     @http.route('/tid-3/tid-3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-3/tid-3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-3.listing', {
#             'root': '/tid-3/tid-3',
#             'objects': http.request.env['tid-3.tid-3'].search([]),
#         })

#     @http.route('/tid-3/tid-3/objects/<model("tid-3.tid-3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-3.object', {
#             'object': obj
#         })
