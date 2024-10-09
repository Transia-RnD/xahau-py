"""Model for SetHook transaction type."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from xahau.models.transactions.transaction import Transaction
from xahau.models.transactions.types import TransactionType
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class Import(Transaction):
    """Imorts an xpop into the account."""

    issuer: Optional[str] = None
    """
    If present, invokes the Hook on the Issuer account.
    """

    blob: Optional[str] = None
    """
    Hex value representing a VL Blob.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.IMPORT,
        init=False,
    )

    def _get_errors(self: Import) -> Dict[str, str]:
        errors = super()._get_errors()
        return errors
