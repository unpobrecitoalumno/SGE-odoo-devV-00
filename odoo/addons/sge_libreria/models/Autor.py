# -*- coding: utf-8 -*-

from odoo import models, fields

class Autor(models.Model):
    _name = 'sge_libreria.autor'
    _description = 'Autor'

    name = fields.Char('Nombre', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    nacionalidad_id = fields.Many2one('res.country', string='Nacionalidad')
    