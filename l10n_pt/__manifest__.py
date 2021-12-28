##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author

{
    "name": "Portugal - Invoicing",
    "version": "14.0.1.1.0",
    "license": "OPL-1",
    "depends": [
        "base_vat",
        "account",
        "account_tax_python",
    ],
    "excludes": [
    ],
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "summary": "Portuguese Invoices & Payments",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/account_chart_template.xml",
        "data/account.account.template-common.csv",
        "data/account.account.template-micro.csv",
        "data/account.account.template-base.csv",
        "data/account.account.template-esnl.csv",
        "data/account_chart_template_accounts.xml",
        "data/account_tax_data.xml",
        # "data/account.tax.template-wht.csv",
        "data/account_fiscal_position.xml",
        "data/account_chart_template_init.xml",
        "data/certification_service.xml",
        "data/backends.xml",
        "data/res_country.xml",
        "data/fiscal_document.xml",
        "views/assets.xml",
        "views/account_views.xml",
        "views/dataport_log.xml",
        "views/layout.xml",
        "views/fiscal_document.xml",
        "views/account_tax_views.xml",
        "views/res_company_views.xml",
        "views/res_config_views.xml",
        "views/account_move_views.xml",
        "views/product_views.xml",
        "views/res_users_views.xml",
        "views/account_payment_views.xml",
        "views/report_payment.xml",
        "views/report_templates.xml",
        # "wizards/account_invoice_debit.xml",
        "report/invoice_report.xml",
        "views/report_invoice.xml",
        "report/payment_report.xml",
        "wizards/dataport_import.xml",
        "wizards/dataport_export.xml",
        "wizards/webservice_failure.xml",
    ],
    "external_dependencies": {
        "python": ["xmlschema", "unicodecsv", "zeep"],
    },
    "post_init_hook": "post_init_hook",
    "installable": True,
    "auto_install": False,
    "application": False,
}
