# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tid-5(models.Model):
#     _name = 'tid-5.tid-5'
#     _description = 'tid-5.tid-5'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
