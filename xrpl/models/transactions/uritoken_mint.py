"""Model for URITokenMint transaction type."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

from typing_extensions import Final

from xrpl.models.amounts import Amount
from xrpl.models.flags import FlagInterface
from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init

_MAX_URI_LENGTH: Final[int] = 512
_MAX_DIGEST_LENGTH: Final[int] = 64


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

    destination: Optional[str] = None
    """
    If present, indicates that this offer may only be
    accepted by the specified account. Attempts by other
    accounts to accept this offer MUST fail.
    """

    amount: Optional[Amount] = None
    """
    Indicates the amount expected or offered for the Token.

    The amount must be non-zero, except when this is a sell
    offer and the asset is XRP. This would indicate that the current
    owner of the token is giving it away free, either to anyone at all,
    or to the account identified by the Destination field.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.URITOKEN_MINT,
        init=False,
    )

    def _get_errors(self: "URITokenMint") -> Dict[str, str]:
        return {
            key: value
            for key, value in {
                **super()._get_errors(),
                "uri": self._get_uri_error(),
                "amount": self._get_amount_error(),
                "destination": self._get_destination_error(),
                "digest": self._get_digest_error(),
            }.items()
            if value is not None
        }

    def _get_uri_error(self: "URITokenMint") -> Optional[str]:
        if self.uri is not None and len(self.uri) > _MAX_URI_LENGTH:
            return f"Must not be longer than {_MAX_URI_LENGTH} characters"
        return None
    
    def _get_amount_error(self: "URITokenMint") -> Optional[str]:
        if self.amount == 0 and not self.destination:
            return f"Cannot be 0 without destination"
        return None

    def _get_destination_error(self: "URITokenMint") -> Optional[str]:
        if self.destination == self.account:
            return "Must not be equal to the account"
        return None

    def _get_digest_error(self: "URITokenMint") -> Optional[str]:
        if self.digest is not None and len(self.digest) > _MAX_DIGEST_LENGTH:
            return f"Must not be longer than {_MAX_DIGEST_LENGTH} characters"
        return None
