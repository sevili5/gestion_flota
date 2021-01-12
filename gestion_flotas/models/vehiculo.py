# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class GsieVehiculo(models.Model):
    _name = "gsie.vehiculo"
    
    name = fields.Char("Placa Vehicular", required=True)
    vin = fields.Char("VIN")
    cil = fields.Char("Cilindraje")
    unidad_refrigerada = fields.Char("Unidad Refrigerada")
    capacidad_carga = fields.Float("Capacidad de Carga")
    transmision = fields.Selection([('manual', 'Manual'), ('automatico', 'Automático')], string="Transmision", default="manual")
    n_serie = fields.Char("# de Serie")
    chassis = fields.Char("Chasis")
    n_asientos = fields.Char("Número de Asientos")
    n_puertas = fields.Char("Número de Puertas")
    color = fields.Char("Color")
    año = fields.Integer("Año")
    active = fields.Boolean("Activo", default=True)
    caballo_potencia = fields.Char("Caballo de Potencia")
    caballo_potencia_fiscales = fields.Char("Cabellos de Potencia Fiscales")
    potencia_motor = fields.Char("Potencia del Motor")
    placa_motor = fields.Char("Número de motor")
    
    fecha_proxima_matricula = fields.Date("Fecha próxima matricula")
    ultimo_odometro = fields.Float("Último Odómetro")
    imagen_vehiculo = fields.Binary("Imagén")
    descripcion = fields.Text("Descripción")

    #Compra
    fecha_compra = fields.Date("Fecha de compra")
    valor_compra = fields.Float("Valor de compra")
    valor_residual = fields.Float("Valor residual")
    odometro_adquisicion = fields.Integer("Odo. Adquisición")
    proveedor_id = fields.Many2one("res.partner", "Proveedor", domain=[('supplier', '=', True)])
    
    #Many2one
    
    modelo_id = fields.Many2one("gsie.modelo", "Modelo")
    tipo_combustible_id = fields.Many2one("gsie.tipo.combustible", "Tipo de Combustible")
    conductor_ids = fields.One2many("gsie.vehiculo.detalle", "objeto_padre", "Conductor")
    ubicacion_id = fields.Many2one("gsie.ubicacion", "Ubicación Vehiculo")

    #Odometro
    lectura_odometro = fields.Integer("Última marcación de Odometro")

    #One2many
    matricula_ids = fields.One2many("gsie.matricula", "vehiculo_id", "Matriculas")




class GsieVehiculoDetalle(models.Model):
    _name = "gsie.vehiculo.detalle"
    
    name = fields.Char("nombre")
    conductor_id = fields.Many2one("hr.employee", "Conductor")
    fecha_asignacion = fields.Date("Fecha")
    objeto_padre = fields.Many2one("gsie.vehiculo", "Vehiculo")



class GsieModelo(models.Model):
    _name = "gsie.modelo"
    
    name = fields.Char("Nombre del Modelo", required=True)
    tipo_vehiculo = fields.Selection([('car', 'Car'), ('bike', 'Bike')], string="Tipo de Vehiculo", default="car")
    imagen_modelo = fields.Binary("Image")
    
    #Many2one
    conductores_id = fields.Many2one("hr.employee", "Conductor")
    proveedores_id = fields.Many2one("res.partner", "Proveedor")
    modelo_id = fields.Many2one("gsie.fabricante.marca", "Fabricante")


    
class GsieFabricanteMarca(models.Model):
    _name = "gsie.fabricante.marca"
    
    name = fields.Char("Marca", required=True)
    imagen_marca = fields.Binary("Image")



class GsieMatricula(models.Model):
    _name = "gsie.matricula"
    
    name = fields.Char("# Matrícula")
    vehiculo_id = fields.Many2one("gsie.vehiculo", "Vehículo")
    fecha_matricula = fields.Date("Fecha de Matrícula")
    monto_pago = fields.Float("Valor de Matrícula")
    state = fields.Selection([('borrador', 'No pagado'), ('pagado', 'Pagado')], 
        "Estado", default='borrador')


class GsieUbicacion(models.Model):
    _name = "gsie.ubicacion"
    
    name = fields.Char("Ubicación", required=True)



class GsiePermisosVehiculo(models.Model):
    _name = "gsie.permisos.vehiculo"
    
    name = fields.Char("Permisos de Vehiculo")










    
