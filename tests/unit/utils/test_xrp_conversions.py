from decimal import Decimal
from unittest import TestCase

import xahau.utils


class TestXAHConversions(TestCase):
    def test_1_xrp(self):
        self.assertEqual(xahau.utils.xah_to_drops(1), "1000000")

    def test_0_xrp(self):
        self.assertEqual(xahau.utils.xah_to_drops(0), "0")

    def test_min_xrp(self):
        self.assertEqual(xahau.utils.xah_to_drops(Decimal("0.000001")), "1")

    def test_max_xrp(self):
        self.assertEqual(xahau.utils.xah_to_drops(10**11), "100000000000000000")

    def test_too_small_xrp(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.xah_to_drops(Decimal(0.0000001))

    def test_too_big_xrp(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.xah_to_drops(10**11 + 1)

    def test_nan_xrp(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.xah_to_drops(Decimal("NaN"))

    def test_str_xrp(self):
        with self.assertRaises(TypeError):
            xahau.utils.xah_to_drops("1000000")

    def test_1_drop(self):
        self.assertEqual(xahau.utils.drops_to_xah("1"), Decimal("0.000001"))

    def test_0_drops(self):
        self.assertEqual(xahau.utils.drops_to_xah("0"), Decimal(0))

    def test_1mil_drops(self):
        self.assertEqual(xahau.utils.drops_to_xah("1000000"), Decimal(1))

    def test_1mil_drops_with_exponent(self):
        self.assertEqual(xahau.utils.drops_to_xah("1e6"), Decimal(1))

    def test_max_drops(self):
        self.assertEqual(xahau.utils.drops_to_xah(str(10**17)), Decimal(10**11))

    def test_float_drops(self):
        with self.assertRaises(TypeError):
            xahau.utils.drops_to_xah(10.1)

    def test_nan_drops(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.drops_to_xah("NaN")

    def test_emptystring_drops(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.drops_to_xah("")

    def test_too_many_drops(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.drops_to_xah(str(10**17 + 1))

    def test_negative_drops(self):
        with self.assertRaises(xahau.utils.XAHRangeException):
            xahau.utils.drops_to_xah("-1")
