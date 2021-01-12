# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class GsieOdometro(models.Model):
    _name = "gsie.odometro"
    
    name = fields.Char("Nombre")
    imagen_odometro = fields.Binary("Image")
    valor_odometro = fields.Float("Valor del Odometro")
    fecha = fields.Date("Fecha")

    #Many2one
    modelo_id = fields.Many2one("gsie.modelo", "Vehículo")


    
    







    
