from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import (
    sign_and_reliable_submission_async,
    test_async_and_sync,
)
from tests.integration.reusable_values import WALLET
from xahau.models.transactions import SetRegularKey
from xahau.wallet import Wallet


class TestSetRegularKey(IntegrationTestCase):
    @test_async_and_sync(globals())
    async def test_all_fields(self, client):
        regular_key = Wallet.create().address
        response = await sign_and_reliable_submission_async(
            SetRegularKey(
                account=WALLET.address,
                regular_key=regular_key,
            ),
            WALLET,
            client,
        )
        self.assertTrue(response.is_successful())
