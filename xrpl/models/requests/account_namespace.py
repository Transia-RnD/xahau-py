"""
This request retrieves the namespace for an account.

All information retrieved is relative to a particular version of the ledger.

`See account_info <https://xrpl.org/account_namespace.html>`_
"""
from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class AccountNamespace(Request):
    """
    This request retrieves the namespace for an account.

    All information retrieved is relative to a particular version of the ledger.

    `See account_info <https://xrpl.org/account_namespace.html>`_
    """

    account: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    namespace_id: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    method: RequestMethod = field(default=RequestMethod.ACCOUNT_NAMESPACE, init=False)
