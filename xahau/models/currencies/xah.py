"""
Specifies XAH as a currency, without a value. Normally, you will not use this
model as it does not specify an amount of XAH. In cases where you need to
specify an amount of XAH, you will use a string. However, for some book order
requests where currencies are specified without amounts, you may need to
specify the use of XAH, without a value. In these cases, you will use this
object.

See https://xrpl.org/currency-formats.html#specifying-currency-amounts
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Type, Union

from typing_extensions import Self

from xahau.models.base_model import BaseModel
from xahau.models.exceptions import XAHLModelException
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class XAH(BaseModel):
    """
    Specifies XAH as a currency, without a value. Normally, you will not use this
    model as it does not specify an amount of XAH. In cases where you need to
    specify an amount of XAH, you will use a string. However, for some book order
    requests where currencies are specified without amounts, you may need to
    specify the use of XAH, without a value. In these cases, you will use this
    object.

    See https://xrpl.org/currency-formats.html#specifying-currency-amounts
    """

    currency: str = field(default="XAH", init=False)

    @classmethod
    def from_dict(cls: Type[Self], value: Dict[str, Any]) -> Self:
        """
        Construct a new XAH from a dictionary of parameters.

        Args:
            value: The value to construct the XAH from.

        Returns:
            A new XAH object, constructed using the given parameters.

        Raises:
            XAHLModelException: If the dictionary provided is invalid.
        """
        if len(value) != 1 or "currency" not in value or value["currency"] != "XAH":
            raise XAHLModelException("Not a valid XAH type")
        return cls()

    def to_dict(self: Self) -> Dict[str, Any]:
        """
        Returns the dictionary representation of an XAH currency object.

        Returns:
            The dictionary representation of an XAH currency object.
        """
        return {**super().to_dict(), "currency": "XAH"}

    def to_amount(self: Self, value: Union[str, int, float]) -> str:
        """
        Converts value to XAH.

        Args:
            value: The amount of XAH.

        Returns:
            A string representation of XAH amount.
        """
        # import needed here to avoid circular dependency
        from xahau.utils.xah_conversions import xah_to_drops

        if isinstance(value, str):
            return xah_to_drops(float(value))
        return xah_to_drops(value)

    def __repr__(self: Self) -> str:
        """
        Generate string representation of XAH.

        Returns:
            A string representation of XAH currency.
        """
        return "XAH()"
