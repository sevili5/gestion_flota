# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class GsieNeumatico(models.Model):
    _name = "gsie.neumatico"
    
    name = fields.Char("Nombre")
    costo = fields.Float("Costo")
    fecha = fields.Date("Fecha")
    transmision = fields.Selection([('manual', 'Manual'), ('automatico', 'Automático')], string="Transmisión", default="manual")
    fecha_ultima = fields.Date("Ultima Inspección")
    pisada_neumatico = fields.Char("Pisada")
    maximo_desgaste = fields.Char("Máximo Desgaste")
    alerta_maximo_desgaste = fields.Char("Alerta Máximo Desgaste")
    imagen_neumatico = fields.Binary("Image")
    descripcion = fields.Text("Descripción")

    #Many2one
    proveedores_id = fields.Many2one("res.partner", "Proveedor")
    modelo_id = fields.Many2one("gsie.modelo", "Vehículo")


    

 




   