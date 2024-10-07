from unittest import TestCase

from xahau.models.currencies import XAH, IssuedCurrency
from xahau.models.requests import AMMInfo
from xahau.models.requests.request import _DEFAULT_API_VERSION

_ASSET = XAH()
_ASSET_2 = IssuedCurrency(currency="USD", issuer="rN6zcSynkRnf8zcgTVrRL8K7r4ovE7J4Zj")


class NoTestAMMInfo(TestCase):
    def test_populate_api_version_field(self):
        request = AMMInfo(
            asset=_ASSET,
            asset2=_ASSET_2,
        )
        self.assertEqual(request.api_version, _DEFAULT_API_VERSION)
        self.assertTrue(request.is_valid())

    def test_asset_asset2(self):
        request = AMMInfo(
            asset=_ASSET,
            asset2=_ASSET_2,
        )
        self.assertTrue(request.is_valid())
