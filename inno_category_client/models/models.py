# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CategoryClient(models.Model):
    _name = 'inno.category.client'

    name = fields.Char(string="", required=False, )
    image_128 = fields.Binary(string="", )
    state = fields.Selection(string="", selection=[('red', 'Rouge'), ('green', 'Vert'), ('orange', 'Orange'), ],
                             required=False, )
    duration = fields.Integer(string="Duree", required=False, )
