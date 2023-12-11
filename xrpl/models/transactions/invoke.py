"""Model for SetHook transaction type."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class Invoke(Transaction):
    """Invokes a hook."""

    destination: Optional[str] = None
    """
    If present, invokes the Hook on the Destination account.
    """

    blob: Optional[str] = None
    """
    Hex value representing a VL Blob.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.INVOKE,
        init=False,
    )

    def _get_errors(self: Invoke) -> Dict[str, str]:
        errors = super()._get_errors()
        return errors
