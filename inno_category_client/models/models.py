# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime


class CategoryPartnerField(models.Model):
    _inherit = 'res.partner'

    partner_category = fields.Many2one(comodel_name="inno.category.client", string="", required=False, )


class CategoryClient(models.Model):
    _name = 'inno.category.client'

    name = fields.Char(string="", required=False, )
    image_128 = fields.Binary(string="", )
    state = fields.Selection(string="", selection=[('red', 'Rouge'), ('green', 'Vert'), ('orange', 'Orange'), ],
                             required=False, )
    start_duration = fields.Integer(string="Duree de", required=False, )
    end_duration = fields.Integer(string="Duree a", required=False, )
    nbr_client = fields.Integer(string="", required=False, compute="_get_infos")
    total_payment = fields.Float(string="", required=False, compute="_get_infos")

    @api.depends("name")
    def _get_infos(self):
        self.total_payment = 0
        partners = self.env['res.partner'].search([('is_customer', '=', True)])
        counting = 0
        total_payment = 0
        for partner in partners:
            orders = self.env['sale.order'].search([('partner_id', '=', partner.id), ('state', 'in', ['done', 'sale'])],
                                                   order='date_order desc')
            payments = self.env['account.payment'].search([('partner_id', '=', partner.id), ('state', '=', 'posted')],
                                                          order='date desc')
            order = None
            payment = None
            if orders:
                order = orders[0]
            if payments:
                payment = payments[0]
            difference = 0
            if order and payment:
                dt = order.date_order
                d_as_datetime = datetime.combine(payment.date, datetime.min.time())
                difference = (d_as_datetime - dt).days
            elif order and not payment:
                dt = order.date_order
                difference = (datetime.now() - dt).days
            if self.start_duration <= difference <= self.end_duration:
                counting += 1
                partner.write({'partner_category': self.id})
                if payment:
                    total_payment += payment.amount
        self.nbr_client = counting

    def get_clients_categories(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'List Client : '+self.name,
            'view_mode': 'tree,form',
            'res_model': 'res.partner',
            'context': {
                'partner_category': self.id,
            }
        }
