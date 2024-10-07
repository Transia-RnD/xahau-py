"""Model for OracleDelete transaction type."""

from __future__ import annotations

from dataclasses import dataclass, field

from xahau.models.required import REQUIRED
from xahau.models.transactions.transaction import Transaction
from xahau.models.transactions.types import TransactionType
from xahau.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class OracleDelete(Transaction):
    """Delete an Oracle ledger entry."""

    account: str = REQUIRED  # type: ignore
    """This account must match the account in the Owner field of the Oracle object."""

    oracle_document_id: int = REQUIRED  # type: ignore
    """A unique identifier of the price oracle for the Account."""

    transaction_type: TransactionType = field(
        default=TransactionType.ORACLE_DELETE,
        init=False,
    )
