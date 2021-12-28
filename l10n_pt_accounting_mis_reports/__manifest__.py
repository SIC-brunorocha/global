##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - Management Reports",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["l10n_pt_accounting", "mis_builder"],
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "data": [
        "data/mis_report_styles.xml",
        "data/mis_report_trial_balance.xml",
        "views/mis_report_views.xml",
    ],
    "installable": True,
    "auto_install": True,
    "application": False,
}
