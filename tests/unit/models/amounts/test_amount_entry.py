from unittest import TestCase

from xrpl.models.amounts import IssuedCurrencyAmount, AmountEntry
from xrpl.models.currencies import IssuedCurrency

_ISSUER = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"


class TestAmountEntry(TestCase):
    def test_to_currency(self):
        currency = "USD"
        amount = "12"
        expected = IssuedCurrency(currency=currency, issuer=_ISSUER)

        amount_entry = AmountEntry(amount_entry=IssuedCurrencyAmount(
            currency=currency, issuer=_ISSUER, value=amount
        ))
        result = amount_entry.amount_entry.to_currency()

        self.assertEqual(result, expected)
