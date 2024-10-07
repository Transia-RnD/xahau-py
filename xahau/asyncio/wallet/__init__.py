"""Async methods for working with XAHL wallets."""
from xahau.asyncio.wallet.wallet_generation import (
    XAHLFaucetException,
    generate_faucet_wallet,
)

__all__ = ["XAHLFaucetException", "generate_faucet_wallet"]
