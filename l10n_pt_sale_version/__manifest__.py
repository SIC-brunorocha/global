# Copyright 2018 Exo Software, Lda. (<https://exo.pt>)
# Copyright 2013 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Portugal - Sale order version",
    "version": "14.0.1.0.1",
    "category": "Sale Management",
    "author": "EXO Software,"
    "Agile Business Group,"
    "Camptocamp,"
    "Akretion,"
    "Odoo Community Association (OCA), "
    "Serpent Consulting Services Pvt. Ltd.",
    "website": "https://exo.pt",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "l10n_pt_sale",
    ],
    "data": [
        "data/sale_order_sequence_data.xml",
        "views/sale_order_views.xml",
        "views/report_sale_order.xml",
    ],
    "installable": True,
    "post_init_hook": "populate_unversioned_name",
}
