# -*- coding: utf-8 -*-
# from odoo import http


# class Tid7(http.Controller):
#     @http.route('/tid_7/tid_7', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tid_7/tid_7/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tid_7.listing', {
#             'root': '/tid_7/tid_7',
#             'objects': http.request.env['tid_7.tid_7'].search([]),
#         })

#     @http.route('/tid_7/tid_7/objects/<model("tid_7.tid_7"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tid_7.object', {
#             'object': obj
#         })
