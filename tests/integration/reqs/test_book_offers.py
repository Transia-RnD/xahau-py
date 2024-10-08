from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from tests.integration.reusable_values import WALLET
from xahau.models.currencies import XAH, IssuedCurrency
from xahau.models.requests import BookOffers


class TestBookOffers(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        response = await client.request(
            BookOffers(
                taker=WALLET.address,
                taker_gets=XAH(),
                taker_pays=IssuedCurrency(
                    currency="USD",
                    issuer="rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
                ),
                ledger_index="validated",
            ),
        )
        self.assertTrue(response.is_successful())
