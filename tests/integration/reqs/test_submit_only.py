from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from tests.integration.reusable_values import WALLET
from xahau.asyncio.transaction import autofill_and_sign
from xahau.core.binarycodec import encode
from xahau.models.amounts import IssuedCurrencyAmount
from xahau.models.requests import SubmitOnly
from xahau.models.transactions import OfferCreate

TX = OfferCreate(
    account=WALLET.address,
    taker_gets="13100000",
    taker_pays=IssuedCurrencyAmount(
        currency="USD",
        issuer=WALLET.address,
        value="10",
    ),
)


class TestSubmitOnly(IntegrationTestCase):
    @test_async_and_sync(globals(), ["xahau.transaction.autofill_and_sign"])
    async def test_basic_functionality(self, client):
        transaction = await autofill_and_sign(TX, client, WALLET)

        tx_json = transaction.to_xrpl()
        tx_blob = encode(tx_json)
        response = await client.request(
            SubmitOnly(
                tx_blob=tx_blob,
            )
        )
        self.assertTrue(response.is_successful())
