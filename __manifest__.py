{
    'name': 'LOAN Custom Module',
    'version': '1.0',
    'category': 'Loan Custom Modules',
    'summary': 'Created custom Module to handle Loans',
    'description': """
        This modules is created for Handling loans and integrate with payroll
    """,
    'author': 'Michael Lejano',
    'company': 'Blackpearl Technology Solutions Corporation',
    'depends': ['base','hr','payroll'],  # Depends on event and product modules
    'data': [
        "security/ir.model.access.csv",
        "views/employee_loan_view_form.xml",
        "views/lending_institution_view_form.xml",
    ],
    'installable': True,
    'application': True,
}
