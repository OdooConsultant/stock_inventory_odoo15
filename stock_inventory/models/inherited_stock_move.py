# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models

class StockMove(models.Model):
    _inherit = "stock.move"

    inventory_id = fields.Many2one('stock.inventory', 'Inventory', check_company=True)
