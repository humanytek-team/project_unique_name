from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    _sql_constraints = [
        (
            "project_date_greater",
            "check(date >= date_start)",
            "Error! project start-date must be lower than project end-date.",
        ),
        (
            "project_name_unique",
            "UNIQUE(company_id, name)",
            "Error! project name must be unique.",
        ),
    ]
