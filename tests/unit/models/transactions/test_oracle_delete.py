from unittest import TestCase

from xahau.models.transactions import OracleDelete

_ACCOUNT = "rsA2LpzuawewSBQXkiju3YQTMzW13pAAdW"


class TestDeleteOracle(TestCase):
    def test_valid(self):
        tx = OracleDelete(
            account=_ACCOUNT,
            oracle_document_id=1,
        )
        self.assertTrue(tx.is_valid())
