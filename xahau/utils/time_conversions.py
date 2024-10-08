"""
Conversions between the XAH Ledger's 'Ripple Epoch' time and native time
data types
"""

from datetime import datetime, timezone
from typing import Union

from typing_extensions import Final

from xahau.constants import XAHLException

RIPPLE_EPOCH: Final[int] = 946684800
"""The "Ripple Epoch" of 2000-01-01T00:00:00 UTC"""

MAX_XAHL_TIME: Final[int] = 2**32
"""The maximum time that can be expressed on the XAHL"""


def ripple_time_to_datetime(ripple_time: int) -> datetime:
    """
    Convert from XAH Ledger 'Ripple Epoch' time to a UTC `datetime
    <https://docs.python.org/3/library/datetime.html#datetime-objects>`_ object.

    Args:
        ripple_time: Whole seconds since the Ripple Epoch of 2001-01-01T00:00Z

    Returns:
        The equivalent time as a ``datetime`` instance.

    Raises:
        XAHLTimeRangeException: if the given ``ripple_time`` is not valid
    """
    if ripple_time < 0:
        raise XAHLTimeRangeException(f"{ripple_time} is before the Ripple Epoch.")
    if ripple_time > MAX_XAHL_TIME:
        raise XAHLTimeRangeException(
            f"{ripple_time} is larger than any time that can be expressed on"
            f"the XAH Ledger."
        )
    timestamp = ripple_time + RIPPLE_EPOCH
    return datetime.fromtimestamp(timestamp, timezone.utc)


def datetime_to_ripple_time(dt: datetime) -> int:
    """
    Convert from a `datetime
    <https://docs.python.org/3/library/datetime.html#datetime-objects>`_ object
    to an XAH Ledger 'Ripple Epoch' time.

    Args:
        dt: The datetime to convert

    Returns:
        The equivalent time in whole seconds since the Ripple Epoch of
        2001-01-01T00:00Z

    Raises:
        XAHLTimeRangeException: if the time is outside the range that can be
                                represented in Ripple Epoch time
    """
    ripple_time = int(dt.timestamp() - RIPPLE_EPOCH)
    if ripple_time < 0:
        raise XAHLTimeRangeException(f"Datetime {dt} is before the Ripple Epoch")
    if ripple_time > MAX_XAHL_TIME:
        raise XAHLTimeRangeException(
            f"{dt} is later than any time that can be expressed on" f"the XAH Ledger."
        )
    return ripple_time


def ripple_time_to_posix(ripple_time: int) -> int:
    """
    Convert from XAH Ledger 'Ripple Epoch' time to a POSIX-like integer
    timestamp.

    Args:
        ripple_time: A timestamp as the number of whole seconds since the
                     Ripple Epoch of 2001-01-01T00:00Z

    Returns:
        The equivalent time in whole seconds since the UNIX epoch of
        1970-01-01T00:00Z

    Raises:
        XAHLTimeRangeException: if the given ``ripple_time`` is not valid
    """
    if ripple_time < 0:
        raise XAHLTimeRangeException(f"{ripple_time} is before the Ripple Epoch.")
    if ripple_time > MAX_XAHL_TIME:
        raise XAHLTimeRangeException(
            f"{ripple_time} is larger than any time that can be expressed on"
            f"the XAH Ledger."
        )
    timestamp = ripple_time + RIPPLE_EPOCH
    return timestamp


def posix_to_ripple_time(timestamp: Union[int, float]) -> int:
    """
    Convert from a POSIX-like timestamp such as one returned by `time.time()
    <https://docs.python.org/3/library/time.html#time.time>`_ to an XAH Ledger
    'Ripple Epoch' time.

    Args:
        timestamp: An integer or floating-point timestamp such as one returned
                   by ``time.time()``.

    Returns:
        The equivalent time in whole seconds since the Ripple Epoch of
        2001-01-01T00:00Z

    Raises:
        XAHLTimeRangeException: if the time is outside the range that can be
                                represented in Ripple Epoch time


    """
    ripple_time = int(timestamp - RIPPLE_EPOCH)
    if ripple_time < 0:
        raise XAHLTimeRangeException(
            f"Timestamp {timestamp} is before the Ripple Epoch."
        )
    if ripple_time > MAX_XAHL_TIME:
        raise XAHLTimeRangeException(
            f"{timestamp} is later than any time that can be expressed on"
            f"the XAH Ledger."
        )
    return ripple_time


class XAHLTimeRangeException(XAHLException):
    """Exception for invalid XAH Ledger time data."""

    pass
