from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import (
    sign_and_reliable_submission_async,
    test_async_and_sync,
)
from tests.integration.reusable_values import WALLET
from xahau.models.amounts import IssuedCurrencyAmount
from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import TrustSet, TrustSetFlag
from xahau.wallet import Wallet


class TestTrustSet(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        issuer_wallet = Wallet.create()
        response = await sign_and_reliable_submission_async(
            TrustSet(
                account=WALLET.address,
                flags=TrustSetFlag.TF_SET_NO_RIPPLE,
                limit_amount=IssuedCurrencyAmount(
                    issuer=issuer_wallet.address,
                    currency="USD",
                    value="100",
                ),
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())

    @test_async_and_sync(globals())
    async def test_special_chars_curr_codes(self, client):
        issuer_wallet = Wallet.create()
        response = await sign_and_reliable_submission_async(
            TrustSet(
                account=WALLET.address,
                flags=TrustSetFlag.TF_SET_NO_RIPPLE,
                limit_amount=IssuedCurrencyAmount(
                    issuer=issuer_wallet.address,
                    currency="$$$",
                    value="100",
                ),
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())

        response = await sign_and_reliable_submission_async(
            TrustSet(
                account=WALLET.address,
                flags=TrustSetFlag.TF_SET_NO_RIPPLE,
                limit_amount=IssuedCurrencyAmount(
                    issuer=issuer_wallet.address,
                    currency="^%#",
                    value="100",
                ),
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())

        response = await sign_and_reliable_submission_async(
            TrustSet(
                account=WALLET.address,
                flags=TrustSetFlag.TF_SET_NO_RIPPLE,
                limit_amount=IssuedCurrencyAmount(
                    issuer=issuer_wallet.address,
                    currency="a1@",
                    value="100",
                ),
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())

        # currency codes must have exactly 3 characters
        with self.assertRaises(XAHLModelException) as error:
            TrustSet(
                account=WALLET.address,
                flags=TrustSetFlag.TF_SET_NO_RIPPLE,
                limit_amount=IssuedCurrencyAmount(
                    issuer=issuer_wallet.address,
                    currency="abcd",
                    value="100",
                ),
            )
        self.assertEqual(
            error.exception.args[0],
            "{'currency': 'Invalid currency abcd'}",
        )
