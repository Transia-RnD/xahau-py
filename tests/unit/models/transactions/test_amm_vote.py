from sys import maxsize
from unittest import TestCase

from xahau.models.currencies import XAH, IssuedCurrency
from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import AMMVote

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"
_ASSET = XAH()
_ASSET2 = IssuedCurrency(currency="ETH", issuer="rpGtkFRXhgVaBzC5XCR7gyE2AZN5SN3SEW")
_TRADING_FEE = 234


class NoTestAMMVote(TestCase):
    def test_tx_valid(self):
        tx = AMMVote(
            account=_ACCOUNT,
            asset=_ASSET,
            asset2=_ASSET2,
            trading_fee=_TRADING_FEE,
        )
        self.assertTrue(tx.is_valid())

    def test_trading_fee_too_high(self):
        with self.assertRaises(XAHLModelException) as error:
            AMMVote(
                account=_ACCOUNT,
                asset=_ASSET,
                asset2=_ASSET2,
                trading_fee=maxsize,
            )
        self.assertEqual(
            error.exception.args[0],
            "{'trading_fee': 'Must be between 0 and 1000'}",
        )

    def test_trading_fee_negative_number(self):
        with self.assertRaises(XAHLModelException) as error:
            AMMVote(
                account=_ACCOUNT,
                asset=_ASSET,
                asset2=_ASSET2,
                trading_fee=-1,
            )
        self.assertEqual(
            error.exception.args[0],
            "{'trading_fee': 'Must be between 0 and 1000'}",
        )
