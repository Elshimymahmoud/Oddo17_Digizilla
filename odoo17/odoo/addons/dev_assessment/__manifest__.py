{
    'name': 'Digizilla',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['base', 'mail', 'web'],
    'assets': {
        'web.assets_backend': [
            'dev_assessment/static/src/js/hide_create_button.js',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/customer_data_views.xml',
        'report/customer_report_templates.xml',
        'report/customer_report.xml',
    ],
    'installable': True,
    'application': True,
}