{
    'name':
        "sale order delivery custom",
    'summary':
        """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author':
        "",
    'website':
        "http://www.yourcompany.com",
    'category':
        'Uncategorized',
    'license':
        'Other proprietary',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version':
        '16.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','delivery','l10n_it_delivery_note'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv'
        'views/sale_order.xml'
    ],
    # only loaded in demonstration mode
}
