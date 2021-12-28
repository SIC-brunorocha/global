##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - E-Fatura",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "version": "14.0.1.0.0",
    "depends": ["l10n_pt_accounting"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_efatura.xml",
        "views/res_partner_views.xml",
        "views/account_move_views.xml",
        "views/res_config_views.xml",
        "wizards/dataport_import_efatura.xml",
        "wizards/account_move_efatura.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
