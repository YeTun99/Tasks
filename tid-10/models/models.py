# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tid-10(models.Model):
#     _name = 'tid-10.tid-10'
#     _description = 'tid-10.tid-10'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
