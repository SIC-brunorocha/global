##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author

{
    "name": "Portugal - Self-billing",
    "version": "14.0.1.0.0",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "depends": [
        "l10n_pt",
    ],
    "data": [
        "data/fiscal_document.xml",
        "views/report_self_billing_invoice.xml",
        "views/report_templates.xml",
        "views/res_partner_views.xml",
        "views/fiscal_document_views.xml",
        "views/account_invoice_views.xml",
    ],
    "demo": [],
    "auto_install": False,
    "installable": False,
}
