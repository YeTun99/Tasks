from odoo import fields,models,api

class TaskId_5(models.Model):
    _inherit="account.move"

    reference=fields.Char(string="Customer Reference")

class TaskId_5_Refernece(models.Model):
    _inherit="account.move.line"

    reference=fields.Char(string="Customer Reference")