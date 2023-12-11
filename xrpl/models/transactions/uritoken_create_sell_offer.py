"""Model for URITokenMint transaction type."""
from dataclasses import dataclass, field
from typing import Optional

from xrpl.models.amounts import Amount
from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class URITokenCreateSellOffer(Transaction):
    """
    The URITokenCreateSellOffer transaction creates either an offer to buy a
    Token the submitting account does not own, or an offer to sell a Token
    the submitting account does own.
    """

    uritoken_id: str = REQUIRED  # type: ignore
    """
    Identifies the TokenID of the URIToken object that the
    offer references. This field is required.

    :meta hide-value:
    """

    amount: Amount = REQUIRED  # type: ignore
    """
    Indicates the amount expected or offered for the Token.

    The amount must be non-zero, except when this is a sell
    offer and the asset is XRP. This would indicate that the current
    owner of the token is giving it away free, either to anyone at all,
    or to the account identified by the Destination field. This field
    is required.

    :meta hide-value:
    """

    destination: Optional[str] = None
    """
    If present, indicates that this offer may only be
    accepted by the specified account. Attempts by other
    accounts to accept this offer MUST fail.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.URITOKEN_CREATE_SELL_OFFER,
        init=False,
    )
