"""Model for URITokenBurn transaction type."""
from dataclasses import dataclass, field

from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class URITokenCancelSellOffer(Transaction):
    """
    The URITokenCancelSellOffer transaction is used to remove the sell Amount on the
    URIToken
    """

    account: str = REQUIRED  # type: ignore
    """
    Identifies the AccountID that submitted this transaction. The account must
    be the present owner of the token or, if the lsfBurnable flag is set
    on the URIToken, either the issuer account or an account authorized by the
    issuer (i.e. MintAccount). This field is required.

    :meta hide-value:
    """

    uritoken_id: str = REQUIRED  # type: ignore
    """
    Identifies the URIToken to be burned. This field is required.

    :meta hide-value:
    """

    transaction_type: TransactionType = field(
        default=TransactionType.URITOKEN_CANCEL_SELL_OFFER,
        init=False,
    )
