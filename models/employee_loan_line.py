# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class EmployeeLoanLine(models.Model):
    _name = 'hr.employee.loan.line'
    _description = 'Loan Amortization Line'

    loan_id = fields.Many2one('hr.employee.loan', required=True, ondelete='cascade')
    date = fields.Date(required=True, string='Payment Date')
    amount = fields.Float(required=True, string='Amount')
    paid = fields.Boolean(default=False, string='Paid')
