# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class GsieServicios(models.Model):
    _name = "gsie.servicios"
    
    name = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
    costo = fields.Char("Costo")
    valor_odometro = fields.Float("Valor del Odometro")
    pieza = fields.Char("Pieza")

    #Many2one
    tipo_servicio_id = fields.Many2one("gsie.tipo.servicios", "Tipo de Servicio")
    proveedores_id = fields.Many2one("res.partner", "Proveedor")
    modelo_id = fields.Many2one("gsie.modelo", "Vehículo")
    conductores_id = fields.Many2one("hr.employee", "Conductor")




class GsieTipoServicios(models.Model):
    _name = "gsie.tipo.servicios"
    
    name = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
