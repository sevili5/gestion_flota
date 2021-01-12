# -*- coding: utf-8 -*-
from odoo import models, fields, api, _



class HrEmployee(models.Model):
    _inherit= "hr.employee"
    
    es_conductor = fields.Boolean("Es Conductor")
    numero_licencia = fields.Char("# Licencia de conducir")
    fecha_emision = fields.Date("Fecha de Emisión")
    tipo_licencia = fields.Selection([('liviana', 'Liviana'), ('pesada', 'Pesada')], string="Tipo de Licencia", default="liviana")
    tipo_sangre = fields.Selection([
                                    ('apositivo', 'A Positivo'),
                                    ('anegativo', 'A Negativo'),
                                    ('bpositivo', 'B Positivo'),
                                    ('bnegativo', 'B Negativo'),
                                    ('onegativo', 'O Negativo'),
                                    ('opositivo', 'O Positivo'),
                                    ('abpositivo', 'AB Positivo'),
                                    ('abnegativo', 'AB Negativo')], string="Típo de Sangre", default="apositivo")
 






    
