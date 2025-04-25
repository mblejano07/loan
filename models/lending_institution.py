# -*- coding: utf-8 -*-
from odoo import models, fields, _

class LendingInstitution(models.Model):
    _name = 'hr.lending.institution'
    _description = 'Lending Institution'
    
    name = fields.Char(string="Institution Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True, string="Active")
