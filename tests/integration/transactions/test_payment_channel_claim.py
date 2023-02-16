from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import (
    sign_and_reliable_submission_async,
    submit_transaction_async,
    test_async_and_sync,
)
from tests.integration.reusable_values import DESTINATION, GATEWAY, WALLET
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.transactions import PaymentChannelClaim, PaymentChannelCreate


class TestPaymentChannelClaim(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_xrp_claim(self, client):
        payment_channel = await sign_and_reliable_submission_async(
            PaymentChannelCreate(
                account=WALLET.classic_address,
                sequence=WALLET.sequence,
                amount="1",
                destination=DESTINATION.classic_address,
                settle_delay=86400,
                public_key=WALLET.public_key,
            ),
            WALLET,
        )
        WALLET.sequence += 1
        response = await submit_transaction_async(
            PaymentChannelClaim(
                account=WALLET.classic_address,
                sequence=WALLET.sequence,
                channel=payment_channel.result["tx_json"]["hash"],
            ),
            WALLET,
        )
        self.assertTrue(response.is_successful())
        WALLET.sequence += 1

    @test_async_and_sync(globals())
    async def test_token_claim(self, client):
        payment_channel = await sign_and_reliable_submission_async(
            PaymentChannelCreate(
                account=WALLET.classic_address,
                sequence=WALLET.sequence,
                amount=IssuedCurrencyAmount(
                    currency="USD",
                    issuer=GATEWAY.classic_address,
                    value="100",
                ),
                destination=DESTINATION.classic_address,
                settle_delay=86400,
                public_key=WALLET.public_key,
            ),
            WALLET,
        )
        WALLET.sequence += 1
        response = await submit_transaction_async(
            PaymentChannelClaim(
                account=WALLET.classic_address,
                sequence=WALLET.sequence,
                channel=payment_channel.result["tx_json"]["hash"],
            ),
            WALLET,
        )
        self.assertTrue(response.is_successful())
        WALLET.sequence += 1
