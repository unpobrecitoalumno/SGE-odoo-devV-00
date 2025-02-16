# -*- coding: utf-8 -*-

from odoo import models, fields

class Autor(models.Model):
    _name = 'sge_libreria.autor'
    _description = 'Autor'

    name = fields.Char('Nombre', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    nacionalidad_id = fields.Many2one('res.country', string='Nacionalidad')
    # Usar atajo oofmany2many, esta relación creará una tabla auxiliar que gestionará Odoo
    # El primer parámetro indica el nombre del modelo que es nuestro compañero en la relación (su valor _name)
    # El parámetro string es la etiqueta que verá el usuario
    # Por defecto la tabla auxiliar tomará el nombre concatenando el nombre de
    # las dos tablas relacionadas seguido del sufijo "_rel", lo cual puede generar nombres muy largos
    # Por ejemplo sge_libreria_autor_sge_libreria_libro_rel
    # El parámetro relation nos permite definir el nombre de esta tabla auxiliar
    libro_ids = fields.Many2many('sge_libreria.libro', relation="sge_libreria_autor_libro_rel", string='Libro')
    
    # ADVERTENCIA: Si se cometen muchos errores al definir campos relacionados
    # o se cambia varias veces los nombres o tipos de relación, es posible
    # que la base de datos quede inconsistente. En ese caso es mejor borrarla
    # y reinicializarla http://localhost:8069/web/database/manager 