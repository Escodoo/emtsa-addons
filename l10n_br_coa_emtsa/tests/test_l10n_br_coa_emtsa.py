# Copyright 2025 - TODAY, Wesley Oliveira <wesley.oliveira@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class L10nBrCoaEmtsa(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.l10n_br_coa_generic = cls.env.ref(
            "l10n_br_coa_emtsa.account_template_emtsa"
        )
        cls.l10n_br_company = cls.env["res.company"].create(
            {"name": "EMTSA - Chart of Accounts"}
        )

    def test_l10n_br_coa_emtsa(self):
        """Test to install the chart of accounts template in a new company"""
        self.env.user.company_ids += self.l10n_br_company
        self.env.user.company_id = self.l10n_br_company
        self.l10n_br_coa_generic.try_loading()

        self.assertEqual(
            self.l10n_br_coa_generic, self.l10n_br_company.chart_template_id
        )
