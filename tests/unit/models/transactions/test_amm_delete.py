from unittest import TestCase

from xahau.models.currencies import XAH, IssuedCurrency
from xahau.models.transactions import AMMDelete


class NoTestAMMDeposit(TestCase):
    def test_tx_valid(self):
        tx = AMMDelete(
            account="r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ",
            sequence=1337,
            asset=XAH(),
            asset2=IssuedCurrency(
                currency="ETH", issuer="rpGtkFRXhgVaBzC5XCR7gyE2AZN5SN3SEW"
            ),
        )
        self.assertTrue(tx.is_valid())
