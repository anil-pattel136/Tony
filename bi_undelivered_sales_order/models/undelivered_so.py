# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('date_order')
    def _default_order_date(self):
        for record in self:
            record.write({'order_date':record.order_id.date_order}) 

    date_order = fields.Datetime(string='Order Date', related='order_id.date_order')
    order_date = fields.Datetime(string='Date Order', compute='_default_order_date',store=True)
    
    