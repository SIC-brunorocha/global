##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author

{
    "name": "Portugal - SAF-T PT Statement",
    "version": "14.0.1.0.1",
    "license": "OPL-1",
    "depends": ["l10n_pt"],
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "data": [
        "security/ir.model.access.csv",
        "wizards/dataport_export_saft.xml",
    ],
    "external_dependencies": {
        "python": [
            "unicodecsv",
        ],
    },
    "installable": True,
    "auto_install": True,
    "application": False,
}
