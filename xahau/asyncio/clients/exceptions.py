"""General XAHL Client Exceptions."""

from __future__ import annotations

from typing import Any, Dict

from typing_extensions import Self

from xahau.constants import XAHLException


class XAHLRequestFailureException(XAHLException):
    """XAHL Request Exception, when the request fails."""

    def __init__(self: Self, result: Dict[str, Any]) -> None:
        """
        Initializes a XAHLRequestFailureException.

        Args:
            result: the error result returned by the ledger.
        """
        self.error = result["error"]
        self.error_message = None
        if "error_message" in result and result["error_message"] is not None:
            self.error_message = result["error_message"]
        elif "error_exception" in result:
            self.error_message = result["error_exception"]
        self.message = f"Request failed, {self.error}: {self.error_message}"
        super().__init__(self.message)


class XAHLWebsocketException(XAHLException):
    """
    XAHL Websocket Exception. Thrown when something goes wrong with the Web Socket
    client.
    """

    pass
