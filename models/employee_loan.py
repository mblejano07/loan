# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class EmployeeLoan(models.Model):
    _name = 'hr.employee.loan'
    _description = 'Employee Loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Loan Reference', required=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', required=True, string='Employee')
   
    loan_amount = fields.Float(string='Loan Amount', required=True)
    balance_amount = fields.Float(string='Remaining Balance', compute='_compute_balance', store=True)
    monthly_amortization = fields.Float(string='Monthly Amortization')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
   
    loan_line_ids = fields.One2many('hr.employee.loan.line', 'loan_id', string='Loan Lines')
    # New Many2one field for Lending Institution
    institution_id = fields.Many2one('hr.lending.institution', string='Lending Institution')

    state = fields.Selection(
    [
        ("draft", "Draft"),
        ("verify", "Waiting for Approval"),
        ("approved", "Approved"),
        ("released", "Released"),
        ("done", "Paid"), 
        ("cancel", "Rejected"),
    ],
    string="Status",
    default="draft",
    tracking=True,
    readonly=True,
    )

    
    # Buttons logic
    def action_loan_draft(self):
        return self.write({"state": "draft"})

    def action_loan_verify(self):
        return self.write({"state": "verify"})

    def action_loan_approve(self):
        return self.write({"state": "approved"})

    def action_loan_release(self):
        return self.write({"state": "released"})

    def action_loan_paid(self):
        return self.write({"state": "done"})

    def action_loan_cancel(self):
        return self.write({"state": "cancel"})

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hr.employee.loan') or _('New')
        return super().create(vals)

    @api.depends('loan_line_ids.amount', 'loan_line_ids.paid')
    def _compute_balance(self):
        for rec in self:
            paid_amount = sum(line.amount for line in rec.loan_line_ids if line.paid)
            rec.balance_amount = rec.loan_amount - paid_amount