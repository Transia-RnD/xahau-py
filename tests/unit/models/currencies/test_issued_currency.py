from unittest import TestCase

from xahau.models.currencies import IssuedCurrency
from xahau.models.exceptions import XAHLModelException

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"


class TestIssuedCurrency(TestCase):
    def test_correct_currency_code_format(self):
        obj = IssuedCurrency(
            currency="USD",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_lower_currency_code_format(self):
        obj = IssuedCurrency(
            currency="usd",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_lower_currency_code_special_chars(self):
        obj = IssuedCurrency(
            currency="$$$",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

        obj = IssuedCurrency(
            currency="^%#",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

        obj = IssuedCurrency(
            currency="a1@",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_incorrect_currency_code_format(self):
        # the "+" is not allowed in a currency format"
        with self.assertRaises(XAHLModelException):
            IssuedCurrency(
                currency="+XX",
                issuer=_ACCOUNT,
            )

    def test_correct_hex_format(self):
        obj = IssuedCurrency(
            currency="0158415500000000C1F76FF6ECB0BAC600000000",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_incorrect_hex_format(self):
        # the "+" is not allowed in a currency format"
        with self.assertRaises(XAHLModelException):
            IssuedCurrency(
                currency="+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                issuer=_ACCOUNT,
            )

    def test_invalid_currency_length(self):
        # length of currency must be either 3 or 40
        with self.assertRaises(XAHLModelException):
            IssuedCurrency(
                currency="XXXX",
                issuer=_ACCOUNT,
            )

    def test_xrp_currency_is_invalid(self):
        # issued currencies can't use XAH (just use a string amount then)
        with self.assertRaises(XAHLModelException):
            IssuedCurrency(
                currency="XAH",
                issuer=_ACCOUNT,
            )

    def test_xrp_lower_currency_is_invalid(self):
        # issued currencies can't use XAH (just use a string amount then)
        with self.assertRaises(XAHLModelException):
            IssuedCurrency(
                currency="xah",
                issuer=_ACCOUNT,
            )

    def test_to_amount(self):
        currency = "USD"
        amount = "12"
        issued_currency = IssuedCurrency(currency=currency, issuer=_ACCOUNT)
        issued_currency_amount = issued_currency.to_amount(amount)

        self.assertEqual(issued_currency_amount.currency, currency)
        self.assertEqual(issued_currency_amount.issuer, _ACCOUNT)
        self.assertEqual(issued_currency_amount.value, amount)
