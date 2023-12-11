"""Model for ClaimReward transaction type."""
from dataclasses import dataclass, field
from typing import Optional

from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class ClaimReward(Transaction):
    """
    Represents a `ClaimReward <https://xrpl.org/claimreward.html>`_ transaction,
    which triggers the reward hook. You can also use this trasaction to opt out 
    of rewards
    """

    issuer: Optional[str] = None
    """
    The address of the `issuer
    <https://xrpl.org/accounts.html>`_ where the reward.c hook is installed.
    """

    transaction_type: TransactionType = field(
        default=TransactionType.CLAIM_REWARD,
        init=False,
    )
