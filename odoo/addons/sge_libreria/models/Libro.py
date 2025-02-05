# -*- coding: utf-8 -*-

from odoo import models, fields

# Usar atajo oomodel para generar fragmento de código
class Libro(models.Model):
    # Estos atributos vienen heredados de la clase madre models.Model
    # El valor _name condiciona el nombre de la tabla y es interno de Odoo
    # conviene siempre que usemos como prefijo el nombre técnico de nuestro módulo seguido de un punto
    # Debemos usar siempre minúsculas
    _name = 'sge_libreria.libro'
    # El valor _description es un texto legible en algunas partes de la aplicación
    # por ejemplo desde Ajustes > Técnico > Modelo
    _description = 'Libro' 
    
    # Conviene que siempre tengamos un atributo llamado literalmente name
    # Usar atajo oofchar para generar fragmento de código
    name = fields.Char('Título', required=True)
    # Usar atajo ooffloat para generar fragmento de código
    precio = fields.Float('Precio')
    # Usar atajo oofinteger para generar fragmento de código
    ejemplares = fields.Integer('Ejemplares')
    # Usar atajo oofdate para generar fragmento de código
    fecha_compra = fields.Date('Fecha compra')
    # Usar atajo oofboolean para generar fragmento de código
    segmano = fields.Boolean('Segunda mano')
    # Usar atajo oofselection para generar fragmento de código
    estado = fields.Selection([ # esto es una lista de tuplas, como en toda lista, los valores se separan por comas
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Mano'),        
    ], string='Estado', default='0') # Etiqueta y valor por defecto