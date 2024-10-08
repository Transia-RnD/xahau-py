from unittest import TestCase

import xahau.core.binarycodec.types.currency as currency
from xahau.core.binarycodec.exceptions import XAHLBinaryCodecException

XAH_HEX_CODE = "0000000000000000000000000000000000000000"
ILLEGAL_XAH_HEX_CODE = "0000000000000000000000005841480000000000"
USD_HEX_CODE = "0000000000000000000000005553440000000000"
NONSTANDARD_HEX_CODE = "015841551A748AD2C1F76FF6ECB0CCCD00000000"
NOT_RECOMMENDED_HEX_CODE = "0000000000414C6F676F30330000000000000000"
XAH_ISO = "XAH"
USD_ISO = "USD"


class TestCurrency(TestCase):
    def test_is_iso_code(self):
        valid_code = "ABC"
        valid_code_numeric = "123"
        invalid_code_long = "LONG"
        invalid_code_short = "NO"
        self.assertTrue(currency._is_iso_code(valid_code))
        self.assertTrue(currency._is_iso_code(valid_code_numeric))
        self.assertFalse(currency._is_iso_code(invalid_code_long))
        self.assertFalse(currency._is_iso_code(invalid_code_short))

    def test_is_hex(self):
        # Valid = 40 char length and only valid hex chars
        valid_hex = "0000000000000000000000005553440000000000"
        invalid_hex_long = "0000000000000000000000005553440000000000123455"
        invalid_hex_short = "1234"
        invalid_hex_chars = "USD0000000000000000000005553440000000000"
        self.assertTrue(currency._is_hex(valid_hex))
        self.assertFalse(currency._is_hex(invalid_hex_long))
        self.assertFalse(currency._is_hex(invalid_hex_short))
        self.assertFalse(currency._is_hex(invalid_hex_chars))

    def test_iso_to_bytes(self):
        # Valid non-XAH
        usd_iso_bytes = currency._iso_to_bytes(USD_ISO)
        # convert bytes to hex string for comparison to expectation
        self.assertEqual(usd_iso_bytes.hex(), USD_HEX_CODE)

        # Valid XAH
        xrp_iso_bytes = currency._iso_to_bytes(XAH_ISO)
        # convert bytes to hex string for comparison to expectation
        self.assertEqual(xrp_iso_bytes.hex(), XAH_HEX_CODE)

        # Error case
        invalid_iso = "INVALID"
        self.assertRaises(XAHLBinaryCodecException, currency._iso_to_bytes, invalid_iso)

    def test_construction_from_hex_standard(self):
        # XAH case
        currency_object = currency.Currency.from_value(XAH_HEX_CODE)
        self.assertEqual(currency_object.to_json(), XAH_ISO)

        # General case
        currency_object = currency.Currency.from_value(USD_HEX_CODE)
        self.assertEqual(currency_object.to_json(), USD_ISO)

    def test_construction_from_iso_code_standard(self):
        # XAH case
        currency_object = currency.Currency.from_value(XAH_ISO)
        self.assertEqual(currency_object.to_hex(), XAH_HEX_CODE)

        # General case
        currency_object = currency.Currency.from_value(USD_ISO)
        self.assertEqual(currency_object.to_hex(), USD_HEX_CODE)

    def test_construction_from_hex_nonstandard(self):
        currency_object = currency.Currency.from_value(NONSTANDARD_HEX_CODE)
        self.assertEqual(currency_object.to_json(), NONSTANDARD_HEX_CODE)

    def test_construction_from_hex_nonrecommended(self):
        currency_object = currency.Currency.from_value(NOT_RECOMMENDED_HEX_CODE)
        self.assertEqual(currency_object.to_json(), NOT_RECOMMENDED_HEX_CODE)

    def test_raises_invalid_value_type(self):
        invalid_value = [1, 2, 3]
        self.assertRaises(
            XAHLBinaryCodecException, currency.Currency.from_value, invalid_value
        )

    def test_raises_invalid_xrp_encoding(self):
        self.assertRaises(
            XAHLBinaryCodecException, currency.Currency.from_value, ILLEGAL_XAH_HEX_CODE
        )
