"""Model for EscrowCancel transaction type."""

from dataclasses import dataclass, field

from xahau.models.required import REQUIRED
from xahau.models.transactions.transaction import Transaction
from xahau.models.transactions.types import TransactionType
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class EscrowCancel(Transaction):
    """
    Represents an `EscrowCancel <https://xrpl.org/escrowcancel.html>`_
    transaction, which returns escrowed XAH to the sender after the Escrow has
    expired.
    """

    owner: str = REQUIRED  # type: ignore
    """
    The address of the account that funded the Escrow. This field is required.

    :meta hide-value:
    """

    offer_sequence: int = REQUIRED  # type: ignore
    """
    Transaction sequence (or Ticket number) of the EscrowCreate transaction
    that created the Escrow. This field is required.

    :meta hide-value:
    """

    transaction_type: TransactionType = field(
        default=TransactionType.ESCROW_CANCEL,
        init=False,
    )
