"""Model for DIDDelete transaction type."""

from __future__ import annotations

from dataclasses import dataclass, field

from xahau.models.transactions.transaction import Transaction
from xahau.models.transactions.types import TransactionType
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class DIDDelete(Transaction):
    """Represents a DIDDelete transaction."""

    transaction_type: TransactionType = field(
        default=TransactionType.DID_DELETE,
        init=False,
    )
