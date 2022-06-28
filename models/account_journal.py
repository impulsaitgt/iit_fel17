from odoo import api, models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    fel_tipo_registro = fields.Selection([('No', 'No'), ('Si', 'Si')], default='No', string='Emite FEL')
    fel_tipo_fel = fields.Char(string='Documento SAT')
    fel_retencion_isr = fields.Float(string='Retencion ISR (%)', default=0.00)
