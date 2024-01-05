"""
The server_info command asks the server for a
human-readable version of various information
about the rippled server being queried.
"""
from dataclasses import dataclass, field

from xrpl.models.requests.request import Request, RequestMethod
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class ServerDefinitions(Request):
    """
    The server_definitions command asks the server for a
    human-readable version of features and definitions.
    """

    method: RequestMethod = field(default=RequestMethod.SERVER_DEFINITIONS, init=False)
