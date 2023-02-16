from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import (
    sign_and_reliable_submission_async,
    test_async_and_sync,
)
from tests.integration.reusable_values import DESTINATION, GATEWAY, WALLET
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.models.requests import ChannelVerify
from xrpl.models.transactions import PaymentChannelCreate


class TestChannelVerify(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_xrp_functionality(self, client):

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

        response = await client.request(
            ChannelVerify(
                channel_id=payment_channel.result["tx_json"]["hash"],
                amount="1",
                public_key=WALLET.public_key,
                signature="304402204EF0AFB78AC23ED1C472E74F4299C0C21",
            ),
        )
        self.assertTrue(response.is_successful())

    @test_async_and_sync(globals())
    async def test_token_functionality(self, client):

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

        response = await client.request(
            ChannelVerify(
                channel_id=payment_channel.result["tx_json"]["hash"],
                amount="1",
                public_key=WALLET.public_key,
                signature="304402204EF0AFB78AC23ED1C472E74F4299C0C21",
            ),
        )
        self.assertTrue(response.is_successful())
