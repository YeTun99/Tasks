from odoo import fields,api,models


class Reference(models.Model):
    _inherit="account.partner.ledger.report.handler"

  
    # @api.model
    # def _get_aml_values(self, options, partner_ids, offset=0, limit=None):