from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.it_utils import sign_and_reliable_submission, test_async_and_sync
from tests.integration.reusable_values import WALLET
from xahau.asyncio.transaction.main import autofill, sign
from xahau.models.requests import SubmitMultisigned
from xahau.models.transactions import AccountSet, SignerEntry, SignerListSet
from xahau.transaction.multisign import multisign
from xahau.utils.str_conversions import str_to_hex
from xahau.wallet import Wallet

FIRST_SIGNER = Wallet.from_seed("sEdTLQkHAWpdS7FDk7EvuS7Mz8aSMRh")
SECOND_SIGNER = Wallet.from_seed("sEd7DXaHkGQD8mz8xcRLDxfMLqCurif")
SIGNER_ENTRIES = [
    SignerEntry(
        account=FIRST_SIGNER.address,
        signer_weight=1,
    ),
    SignerEntry(
        account=SECOND_SIGNER.address,
        signer_weight=1,
    ),
]
LIST_SET_TX = sign_and_reliable_submission(
    SignerListSet(
        account=WALLET.address,
        signer_quorum=2,
        signer_entries=SIGNER_ENTRIES,
    ),
    WALLET,
)
EXAMPLE_DOMAIN = str_to_hex("example.com")
EXPECTED_DOMAIN = "6578616D706C652E636F6D"


class TestSubmitMultisigned(IntegrationTestCase):
    @test_async_and_sync(
        globals(),
        [
            "xahau.transaction.sign",
            "xahau.transaction.autofill",
        ],
    )
    async def test_basic_functionality(self, client):
        tx = AccountSet(account=WALLET.address, domain=EXAMPLE_DOMAIN)

        autofilled_tx = await autofill(tx, client, len(SIGNER_ENTRIES))

        tx_1 = sign(autofilled_tx, FIRST_SIGNER, multisign=True)
        tx_2 = sign(autofilled_tx, SECOND_SIGNER, multisign=True)

        multisigned_tx = multisign(autofilled_tx, [tx_1, tx_2])

        # submit tx
        response = await client.request(
            SubmitMultisigned(
                tx_json=multisigned_tx,
            )
        )
        self.assertTrue(response.is_successful())
        self.assertEqual(response.result["tx_json"]["Domain"], EXPECTED_DOMAIN)
