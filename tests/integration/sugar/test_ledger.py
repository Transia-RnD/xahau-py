from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import test_async_and_sync
from xahau.asyncio.ledger import get_fee
from xahau.utils import drops_to_xah


class TestLedger(IntegrationTestCase):
    @test_async_and_sync(globals(), ["xahau.ledger.get_fee"])
    async def test_get_fee_max(self, client):
        expected = "1"
        max_fee = drops_to_xah(expected)
        result = await get_fee(client, max_fee=max_fee)
        self.assertEqual(result, expected)
