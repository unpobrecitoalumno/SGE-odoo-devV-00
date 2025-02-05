# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    # Estos atributos vienen heredados de la clase madre models.Model
    # El valor _name condiciona el nombre de la tabla y es interno de Odoo
    # conviene siempre que usemos como prefijo el nombre técnico de nuestro módulo seguido de un punto
    # Debemos usar siempre minúsculas
    _name = 'sge_libreria.categoria'
    # El valor _description es un texto legible en algunas partes de la aplicación
    # por ejemplo desde Ajustes > Técnico > Modelo
    _description = 'Categoría' 
    
    # Atributos propios de la clase, que Odoo creará como columnas de la tabla
    # nombre_del_campo = fields.TipoDatosOdoo('Etiqueta')
    # otros parámetros opcionales:
    #   help='Tooltip de ayuda UI'
    #   required=True si queremos que el campo sea obligatorio
    name = fields.Char('Nombre', help="Introduzca nombre de categoría", required=True)
    description = fields.Char('Descripción')
    
    # Además Odoo creará otros atributos internos por defecto
    # id servirá de clave primaria
    # create_uid indicará el usuario que creo un elemento de esta clase
    # create_date indicará la fecha
    # etc...
