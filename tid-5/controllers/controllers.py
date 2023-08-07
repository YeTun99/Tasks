# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-5(http.Controller):
#     @http.route('/tid-5/tid-5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-5/tid-5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-5.listing', {
#             'root': '/tid-5/tid-5',
#             'objects': http.request.env['tid-5.tid-5'].search([]),
#         })

#     @http.route('/tid-5/tid-5/objects/<model("tid-5.tid-5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-5.object', {
#             'object': obj
#         })
