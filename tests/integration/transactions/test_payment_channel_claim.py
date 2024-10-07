from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import (
    sign_and_reliable_submission_async,
    test_async_and_sync,
)
from tests.integration.reusable_values import PAYMENT_CHANNEL, WALLET
from xahau.models.transactions import PaymentChannelClaim


class TestPaymentChannelClaim(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_receiver_claim(self, client):
        response = await sign_and_reliable_submission_async(
            PaymentChannelClaim(
                account=WALLET.address,
                channel=PAYMENT_CHANNEL.result["tx_json"]["hash"],
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())
