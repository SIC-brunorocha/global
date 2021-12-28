##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=manifest-required-author
{
    "name": "Portugal - Asset Management CE",
    "license": "AGPL-3",
    "author": "Exo Software",
    "website": "https://exosoftware.pt",
    "category": "Accounting & Finance",
    "version": "14.0.1.0.0",
    "depends": ["account_asset_management", "l10n_pt_accounting"],
    "data": [
        "views/account_asset_views.xml",
        "views/account_asset_legal_rate_views.xml",
    ],
    "demo": [],
    "installable": True,
    # 'auto_install': True,
}
