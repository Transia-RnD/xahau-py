import asyncio

from tests.integration.it_utils import (
    fund_wallet_async,
    sign_and_reliable_submission_async,
)
from xahau.models import IssuedCurrencyAmount, OfferCreate, PaymentChannelCreate
from xahau.wallet import Wallet


# TODO: use `asyncio.gather` for these, to parallelize
# TODO: set up wallet for each test instead of using one for all tests (now that it's
# faster)
async def _set_up_reusable_values():
    wallet = Wallet.create()
    await fund_wallet_async(wallet)
    destination = Wallet.create()
    await fund_wallet_async(destination)
    door_wallet = Wallet.create()
    await fund_wallet_async(door_wallet)
    witness_wallet = Wallet.create()
    await fund_wallet_async(witness_wallet)

    offer = await sign_and_reliable_submission_async(
        OfferCreate(
            account=wallet.address,
            taker_gets="13100000",
            taker_pays=IssuedCurrencyAmount(
                currency="USD",
                issuer=wallet.address,
                value="10",
            ),
        ),
        wallet,
    )

    payment_channel = await sign_and_reliable_submission_async(
        PaymentChannelCreate(
            account=wallet.address,
            amount="1",
            destination=destination.address,
            settle_delay=86400,
            public_key=wallet.public_key,
        ),
        wallet,
    )

    return (
        wallet,
        destination,
        offer,
        payment_channel,
    )


(
    WALLET,
    DESTINATION,
    OFFER,
    PAYMENT_CHANNEL,
) = asyncio.run(_set_up_reusable_values())
