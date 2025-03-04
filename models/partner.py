# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    approver_id = fields.Many2one('res.users', string='Approved By', required=False)
    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', string="Approval Status")

    is_admin = fields.Boolean(compute="_compute_is_admin")

    @api.depends('approval_status')
    def _compute_is_admin(self):
        """Check if the current user is an admin."""
        for rec in self:
            rec.is_admin = self.env.user.has_group('training_contacts.contact_approval_admin')

    def action_approve(self):
        for rec in self:
            rec.approver_id = self.env.user
            rec.approval_status = 'approved'
    def action_cancel(self):
        for rec in self:
            rec.approval_status = 'rejected'
    def action_reset(self):
        for rec in self:
            rec.approval_status = 'draft'
            rec.approver_id = False

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

