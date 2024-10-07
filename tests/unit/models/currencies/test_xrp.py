from unittest import TestCase

from xahau.models.currencies import XAH
from xahau.utils import xah_to_drops


class TestXAH(TestCase):
    def test_to_dict(self):
        self.assertEqual(XAH().to_dict()["currency"], "XAH")

    def test_to_amount(self):
        amount = 12
        expected = xah_to_drops(amount)
        result = XAH().to_amount(amount)

        self.assertEqual(result, expected)
