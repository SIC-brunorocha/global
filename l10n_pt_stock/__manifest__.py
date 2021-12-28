##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - Stock",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "version": "14.0.1.0.1",
    "depends": [
        "l10n_pt",
        "stock_picking_invoice_link",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/fiscal_document.xml",
        "data/stock_picking_mail.xml",
        "report/deliveryslip_report.xml",
        "views/res_config_settings_views.xml",
        "views/report_deliveryslip.xml",
        "views/stock_picking_views.xml",
        "views/product_views.xml",
        "views/fiscal_document_views.xml",
        "wizards/webservice_failure.xml",
        # "wizards/wizard_inventory_statement.xml",  #TODO: 14.0 reenable
    ],
    "external_dependencies": {"python": ["unicodecsv"]},
    "demo": [],
    "installable": True,
}
