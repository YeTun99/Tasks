# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tid_7(models.Model):
#     _name = 'tid_7.tid_7'
#     _description = 'tid_7.tid_7'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
