from unittest import TestCase

from xahau.models.amounts import IssuedCurrencyAmount
from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import Clawback

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"
_XAH_AMOUNT = "1000"
_ISSUED_CURRENCY_AMOUNT = IssuedCurrencyAmount(
    currency="BTC", value="1.002", issuer=_ACCOUNT
)


class NoTestClawback(TestCase):
    def test_amount_is_XAH(self):
        with self.assertRaises(XAHLModelException):
            Clawback(
                account=_ACCOUNT,
                amount=_XAH_AMOUNT,
            )

    def test_holder_is_issuer(self):
        with self.assertRaises(XAHLModelException):
            Clawback(
                account=_ACCOUNT,
                amount=_ISSUED_CURRENCY_AMOUNT,
            )
