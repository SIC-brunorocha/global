##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - Sale",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "version": "14.0.1.0.1",
    "depends": ["sale_management", "l10n_pt"],
    "data": [
        "data/ir_sequence.xml",
        "data/fiscal_document.xml",
        "views/sale_order_views.xml",
        "views/res_config_views.xml",
        "views/report_sale_order.xml",
        "report/sale_order_report.xml",
    ],
    "demo": [],
    "auto_install": True,
    "installable": True,
}
