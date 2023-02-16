"""Model for URITokenMint transaction type."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xrpl.models.flags import FlagInterface
from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


class URITokenMintFlag(int, Enum):
    """
    Transactions of the URITokenMint type support additional values in the Flags
    field. This enum represents those options.

    `See URITokenMint Flags
    <https://xrpl.org/uritokenmint.html#uritokenmint-flags>`_
    """

    TF_BURNABLE = 0x00000001
    """
    If set, indicates that the minted token may be burned by the issuer even
    if the issuer does not currently hold the token. The current holder of
    the token may always burn it.
    """


class URITokenMintFlagInterface(FlagInterface):
    """
    Transactions of the URITokenMint type support additional values in the Flags
    field. This TypedDict represents those options.

    `See URITokenMint Flags
    <https://xrpl.org/uritokenmint.html#uritokenmint-flags>`_
    """

    TF_BURNABLE: bool


@require_kwargs_on_init
@dataclass(frozen=True)
class URITokenMint(Transaction):
    """The URITokenMint transaction creates an URIToken object."""

    uri: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    digest: Optional[str] = None
    """
    """

    transaction_type: TransactionType = field(
        default=TransactionType.URITOKEN_MINT,
        init=False,
    )
