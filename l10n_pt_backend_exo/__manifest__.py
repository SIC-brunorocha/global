##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exo.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - Exo Certification Backend",
    "license": "OPL-1",
    "author": "EXO Software",
    "website": "https://exo.pt",
    "category": "Localization",
    "version": "14.0.1.0.1",
    "depends": ["l10n_pt"],
    "external_dependencies": {
        "python": ["cryptography"],
    },
    "data": [
        "data/backends.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": True,
}
