# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class GsieCombustibleControl(models.Model):
    _name = "gsie.combustible.control"
    
    name = fields.Char("Nombre")
    litro_galon = fields.Char("Litro/Galón")
    precio = fields.Float("Precio")
    precio_total = fields.Float("Precio Total")
    comprador = fields.Float("Precio Total")
    fecha_compra = fields.Date("Fecha de Compra")

    #Many2one
    proveedores_id = fields.Many2one("res.partner", "Proveedor")
    modelo_id = fields.Many2one("gsie.modelo", "Vehículo")
    #One2many
    combustible_control_ids = fields.One2many("gsie.detalle.combustible.control", "combustible_control_id", "combustible_control_ids")
    



class GsieDetalleCombustibleControl(models.Model):
    _name = "gsie.detalle.combustible.control"
    
    fecha_inicial = fields.Date("Fecha Inicial")
    odometro = fields.Float("Odomentro")
    km_recorrido = fields.Float("Km Recorridos")
    galones = fields.Float("Galones")
    km_galon = fields.Float("Km/Galón")
    factura = fields.Char("Factura")

    #Many2one
    combustible_control_id = fields.Many2one("gsie.combustible.control", "Combustible")




class GsieTipoCombustible(models.Model):
    _name = "gsie.tipo.combustible"
    
    name = fields.Char("Tipo de Combustible", required=True)





