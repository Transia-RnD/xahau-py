from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from tests.integration.reusable_values import WALLET
from xahau.models.requests import NoRippleCheck, NoRippleCheckRole


class TestNoRippleCheck(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_basic_functionality(self, client):
        response = await client.request(
            NoRippleCheck(
                account=WALLET.address,
                role=NoRippleCheckRole.USER,
            )
        )
        self.assertTrue(response.is_successful())
