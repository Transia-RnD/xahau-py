"""Model for SetHook transaction type."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class Invoke(Transaction):
    """Sets the an array of hooks on an account."""

    destination: str = REQUIRED  # type: ignore
    """
    The address of the account receiving the payment. This field is required.

    :meta hide-value:
    """

    transaction_type: TransactionType = field(
        default=TransactionType.INVOKE,
        init=False,
    )

    def _get_errors(self: Invoke) -> Dict[str, str]:
        errors = super()._get_errors()
        return errors
