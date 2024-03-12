"""Model for URITokenMint transaction type."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, List, Union

from typing_extensions import Final

from xrpl.models.amounts import AmountEntry
from xrpl.models.flags import FlagInterface
from xrpl.models.base_model import BaseModel
from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init

_MAX_BLOB_LENGTH: Final[int] = 256
_MAX_URI_LENGTH: Final[int] = 512
_DIGEST_LENGTH: Final[int] = 64

@require_kwargs_on_init
@dataclass(frozen=True)
class MintURIToken(BaseModel):
    """Represents a uritoken object."""

    uri: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    digest: Optional[str] = None
    """
    """

    flags: Union[Dict[str, bool], int, List[int]] = 0
    """
    The flags that are set on the uri token.
    This field is required.

    :meta hide-value:
    """


@require_kwargs_on_init
@dataclass(frozen=True)
class Remit(Transaction):
    """The Remit transaction"""

    destination: str = REQUIRED  # type: ignore
    """
    The address of the account receiving the payment. This field is required.

    :meta hide-value:
    """

    destination_tag: Optional[int] = None
    """
    An arbitrary `destination tag
    <https://xrpl.org/source-and-destination-tags.html>`_ that
    identifies the reason for the Payment, or a hosted recipient to pay.
    """

    amounts: Optional[List[AmountEntry]] = None

    mint_uri_token: Optional[MintURIToken] = None

    uri_token_ids: Optional[List[str]] = None

    invoice_id: Optional[str] = None  # TODO: should be a 256 bit hash
    """
    Arbitrary 256-bit hash representing a specific reason or identifier for
    this Check.
    """

    blob: Optional[str] = None
    """
    Hex value representing a VL Blob.
    """

    inform: Optional[str] = None
    """
    If present, can trigger a hook on a third party account.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.REMIT,
        init=False,
    )

    def _get_errors(self: "Remit") -> Dict[str, str]:
        return {
            key: value
            for key, value in {
                **super()._get_errors(),
                "destination": self._get_destination_error(),
                "inform": self._get_inform_error(),
                "amounts": self._get_amounts_error(),
                "uri_token_ids": self._get_uri_token_ids_error(),
                "uri": self._get_uri_error(),
                "digest": self._get_digest_error(),
                "blob": self._get_blob_error(),
            }.items()
            if value is not None
        }
    
    def _get_amounts_error(self: "Remit") -> Optional[str]:
        if self.amounts is not None:
            seen = set()
            seen_xrp = False
            for amount in self.amounts:
                if isinstance(amount.amount_entry.amount, str):
                    if seen_xrp:
                        return "Duplicate Native amounts are not allowed"
                    seen_xrp = True 
                else:
                    amount_key = (amount.amount_entry.amount.currency, amount.amount_entry.amount.issuer)
                    if amount_key in seen:
                        return "Duplicate amounts are not allowed"
                    seen.add(amount_key)
        return None
    
    def _get_uri_token_ids_error(self: "Remit") -> Optional[str]:
        if self.uri_token_ids is not None:
            seen = set()
            for token_id in self.uri_token_ids:
                if not isinstance(token_id, str) or len(token_id) != 64:
                    return "Each URI token ID must be a 64-character hash256 string"
                if token_id in seen:
                    return "Duplicate URI token IDs are not allowed"
                seen.add(token_id)
        return None

    def _get_destination_error(self: "Remit") -> Optional[str]:
        if self.destination == self.account:
            return "Must not be equal to the account"
        return None

    def _get_inform_error(self: "Remit") -> Optional[str]:
        if self.inform == self.account or self.inform == self.destination:
            return "Must not be equal to the account or destination"
        return None
    
    def _get_uri_error(self: "Remit") -> Optional[str]:
        if self.mint_uri_token is not None and len(self.mint_uri_token.uri) > _MAX_URI_LENGTH:
            return f"Must not be longer than {_MAX_URI_LENGTH} characters"
        return None
    
    def _get_digest_error(self: "Remit") -> Optional[str]:
        if self.mint_uri_token is not None and self.mint_uri_token.digest is not None and len(self.mint_uri_token.digest) != _DIGEST_LENGTH:
            return f"Must be exactly {_DIGEST_LENGTH} characters"
        return None
    
    def _get_blob_error(self: "Remit") -> Optional[str]:
        if self.blob is not None and len(self.blob) > _MAX_BLOB_LENGTH:
            return f"Must not be longer than {_MAX_BLOB_LENGTH} characters"
        return None
