import asyncio

from tests.integration.it_utils import (
    fund_wallet_async,
    sign_and_reliable_submission_async,
)
from xahau.models import (
    IssuedCurrencyAmount,
    OfferCreate,
    Payment,
    PaymentChannelCreate,
    TrustSet,
)
from xahau.wallet import Wallet


# TODO: use `asyncio.gather` for these, to parallelize
# TODO: set up wallet for each test instead of using one for all tests (now that it's
# faster)
async def _set_up_reusable_values():
    wallet = Wallet.create()
    await fund_wallet_async(wallet)
    destination = Wallet.create()
    await fund_wallet_async(destination)
    gateway = Wallet.create()
    await fund_wallet_async(gateway)

    await sign_and_reliable_submission_async(
        TrustSet(
            account=wallet.classic_address,
            limit_amount=IssuedCurrencyAmount(
                currency="USD",
                issuer=gateway.classic_address,
                value="10000",
            ),
        ),
        wallet,
    )

    await sign_and_reliable_submission_async(
        TrustSet(
            account=destination.classic_address,
            limit_amount=IssuedCurrencyAmount(
                currency="USD",
                issuer=gateway.classic_address,
                value="10000",
            ),
        ),
        destination,
    )

    await sign_and_reliable_submission_async(
        Payment(
            account=gateway.classic_address,
            destination=wallet.classic_address,
            amount=IssuedCurrencyAmount(
                currency="USD",
                issuer=gateway.classic_address,
                value="10000",
            ),
        ),
        gateway,
    )

    await sign_and_reliable_submission_async(
        Payment(
            account=gateway.classic_address,
            destination=destination.classic_address,
            amount=IssuedCurrencyAmount(
                currency="USD",
                issuer=gateway.classic_address,
                value="10000",
            ),
        ),
        gateway,
    )

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
        gateway,
        offer,
        payment_channel,
    )


(
    WALLET,
    DESTINATION,
    GATEWAY,
    OFFER,
    PAYMENT_CHANNEL,
) = asyncio.run(_set_up_reusable_values())
