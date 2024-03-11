"""Model for EscrowCancel transaction type."""

from dataclasses import dataclass, field
from typing import Optional

from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class EscrowCancel(Transaction):
    """
    Represents an `EscrowCancel <https://xrpl.org/escrowcancel.html>`_
    transaction, which returns escrowed XRP to the sender after the Escrow has
    expired.
    """

    owner: str = REQUIRED  # type: ignore
    """
    The address of the account that funded the Escrow. This field is required.

    :meta hide-value:
    """

    offer_sequence: Optional[int] = None
    """
    Transaction sequence (or Ticket number) of the EscrowCreate transaction
    that created the Escrow. This field is required.

    :meta hide-value:
    """

    escrow_id: Optional[str] = None
    """
    The ID of the `Escrow ledger object
    <https://xrpl.org/escrow.html>`_ to cancel, as a 64-character
    hexadecimal string.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.ESCROW_CANCEL,
        init=False,
    )
