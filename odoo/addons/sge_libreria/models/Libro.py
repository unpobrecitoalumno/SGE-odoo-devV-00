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
    # Ahora que sabemos hacer relaciones many2one podemos usar campos Monetary en lugar de Float
    # Usar atajo oofmonetary, esto permite que el módulo sea multidivisa
    precio = fields.Monetary('Precio')
    # Los campos Monetary requieren que hagamos una relación con un modelo que viene de base con Odoo res.currency
    # Se pueden ver otros modelos interesantes del módulo base https://github.com/odoo/odoo/tree/17.0/odoo/addons/base/data
    # como res.country, res.lang, ...
    # Si damos un nombre diferente a currency_id deberemos indicarlo como segundo parámetro a la definición anterior con fields.Monetary
    currency_id = fields.Many2one('res.currency', string='Moneda')
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
    
    # Usar atajo oofmany2one
    # Por convención en odoo los campos relacionales many2one tienen como sufijo "_id"
    # El primer parámetro indica el nombre del modelo que es nuestro compañero en la relación (su valor _name)
    # El parámetro string es la etiqueta que verá el usuario
    # Cuando tenemos relaciones entre clases, es conveniente tener un atributo llamado exactamente name, no confundir con _name
    categoria_id = fields.Many2one('sge_libreria.categoria', string='Categoría')

    # Usar atajo oofmany2many, esta relación creará una tabla auxiliar que gestionará Odoo
    # El primer parámetro indica el nombre del modelo que es nuestro compañero en la relación (su valor _name)
    # El parámetro string es la etiqueta que verá el usuario
    # Por defecto la tabla auxiliar tomará el nombre concatenando el nombre de
    # las dos tablas relacionadas seguido del sufijo "_rel", lo cual puede generar nombres muy largos
    # Por ejemplo sge_libreria_autor_sge_libreria_libro_rel
    # El parámetro relation nos permite definir el nombre de esta tabla auxiliar
    autor_ids = fields.Many2many('sge_libreria.autor', relation="sge_libreria_autor_libro_rel", string='Autores')
        
    # ADVERTENCIA: Si se cometen muchos errores al definir campos relacionados
    # o se cambia varias veces los nombres o tipos de relación, es posible
    # que la base de datos quede inconsistente. En ese caso es mejor borrarla
    # y reinicializarla http://localhost:8069/web/database/manager 