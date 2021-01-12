
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class GsieContratos(models.Model):
    _name = "gsie.contratos"
    
    name = fields.Char("Nombre")
    costo_activacion = fields.Float("Costo de Activación")
    fecha_factura = fields.Date("Fecha de factura")
    fecha_inicio = fields.Date("Fecha de Inicio de Contrato")
    fecha_expiracion = fields.Date("Fecha de Expiraciíon Contrato")
    descripcion = fields.Text("Descripción")
    servicios_id = fields.Many2one("hr.employee", "Servicios")

    #Many2one
    responsable_id = fields.Many2one("hr.employee", "Responsable")
    proveedores_id = fields.Many2one("res.partner", "Proveedor")
    conductores_id = fields.Many2one("hr.employee", "Conductor")
    modelo_id = fields.Many2one("gsie.modelo", "Vehiculo")
