# -*- coding: utf-8 -*-
# from odoo import http


# class InnoCategoryClient(http.Controller):
#     @http.route('/inno_category_client/inno_category_client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inno_category_client/inno_category_client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inno_category_client.listing', {
#             'root': '/inno_category_client/inno_category_client',
#             'objects': http.request.env['inno_category_client.inno_category_client'].search([]),
#         })

#     @http.route('/inno_category_client/inno_category_client/objects/<model("inno_category_client.inno_category_client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inno_category_client.object', {
#             'object': obj
#         })
