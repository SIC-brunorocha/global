##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author

{
    "name": "Portugal - Credit Notes",
    "version": "14.0.1.0.1",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "depends": ["l10n_pt", "account_invoice_refund_link"],
    "data": [
        "views/account_move_views.xml",
        "wizards/account_move_reversal_views.xml",
    ],
    "demo": [],
    "auto_install": True,
    "installable": True,
}
