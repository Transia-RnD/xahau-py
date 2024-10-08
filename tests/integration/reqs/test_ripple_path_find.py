from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from tests.integration.reusable_values import DESTINATION, WALLET
from xahau.models.requests import RipplePathFind


class TestRipplePathFind(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        response = await client.request(
            RipplePathFind(
                source_account=WALLET.address,
                destination_account=DESTINATION.address,
                destination_amount="100",
            ),
        )
        self.assertTrue(response.is_successful())
