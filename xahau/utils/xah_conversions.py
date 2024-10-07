"""Conversions between XAH drops and native number types."""
import re
from decimal import Decimal, InvalidOperation, localcontext
from typing import Pattern, Union

from typing_extensions import Final

from xahau.constants import DROPS_DECIMAL_CONTEXT, XAHLException

ONE_DROP: Final[Decimal] = Decimal("0.000001")
"""Indivisible unit of XAH"""

MAX_XAH: Final[Decimal] = Decimal(10**11)
"""100 billion decimal XAH"""

MAX_DROPS: Final[Decimal] = Decimal(10**17)
"""Maximum possible drops of XAH"""

# Drops should be an integer string. MAY have (positive) exponent.
# See also: https://xrpl.org/currency-formats.html#string-numbers
_DROPS_REGEX: Final[Pattern[str]] = re.compile("(?:[1-9][0-9Ee-]{0,17}|0)")


def xah_to_drops(xrp: Union[int, float, Decimal]) -> str:
    """
    Convert a numeric XAH amount to drops of XAH.

    Args:
        xrp: Numeric representation of whole XAH

    Returns:
        Equivalent amount in drops of XAH

    Raises:
        TypeError: if ``xrp`` is given as a string
        XAHRangeException: if the given amount of XAH is invalid
    """
    if type(xrp) == str:  # type: ignore
        # This protects people from passing drops to this function and getting
        # a million times as many drops back.
        raise TypeError(
            "XAH provided as a string. Use a number format" "like Decimal or int."
        )
    with localcontext(DROPS_DECIMAL_CONTEXT):
        try:
            xrp_d = Decimal(xrp)
        except InvalidOperation:
            raise XAHRangeException(f"Not a valid amount of XAH: '{xrp}'")

        if not xrp_d.is_finite():  # NaN or an Infinity
            raise XAHRangeException(f"Not a valid amount of XAH: '{xrp}'")

        if xrp_d < ONE_DROP and xrp_d != 0:
            raise XAHRangeException(f"XAH amount {xrp} is too small.")
        if xrp_d > MAX_XAH:
            raise XAHRangeException(f"XAH amount {xrp} is too large.")

        drops_amount = (xrp_d / ONE_DROP).quantize(Decimal(1))
        drops_str = str(drops_amount).strip()

        # This should never happen, but is a precaution against Decimal doing
        # something unexpected.
        if not _DROPS_REGEX.fullmatch(drops_str):
            raise XAHRangeException(
                f"xah_to_drops failed sanity check. Value "
                f"'{drops_str}' does not match the drops regex"
            )

    return drops_str


def drops_to_xah(drops: str) -> Decimal:
    """
    Convert from drops to decimal XAH.

    Args:
        drops: String representing indivisible drops of XAH

    Returns:
        Decimal representation of the same amount of XAH

    Raises:
        TypeError: if ``drops`` not given as a string
        XAHRangeException: if the given number of drops is invalid
    """
    if type(drops) != str:
        raise TypeError(f"Drops must be provided as string (got {type(drops)})")
    drops = drops.strip()
    with localcontext(DROPS_DECIMAL_CONTEXT):
        if not _DROPS_REGEX.fullmatch(drops):
            raise XAHRangeException(f"Not a valid amount of drops: '{drops}'")
        try:
            drops_d = Decimal(drops)
        except InvalidOperation:
            raise XAHRangeException(f"Not a valid amount of drops: '{drops}'")
        xrp_d = drops_d * ONE_DROP
        if xrp_d > MAX_XAH:
            raise XAHRangeException(f"Drops amount {drops} is too large.")
        return xrp_d


class XAHRangeException(XAHLException):
    """Exception for invalid XAH amounts."""

    pass
