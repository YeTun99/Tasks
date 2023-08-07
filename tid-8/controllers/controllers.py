# -*- coding: utf-8 -*-
# from odoo import http


# class Tid-8(http.Controller):
#     @http.route('/tid-8/tid-8', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid-8/tid-8/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid-8.listing', {
#             'root': '/tid-8/tid-8',
#             'objects': http.request.env['tid-8.tid-8'].search([]),
#         })

#     @http.route('/tid-8/tid-8/objects/<model("tid-8.tid-8"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid-8.object', {
#             'object': obj
#         })
