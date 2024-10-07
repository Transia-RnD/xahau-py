"""
The XAH Ledger has two kinds of money: XAH, and issued
currencies. Both types have high precision, although their
formats are different.
"""
from typing import Union

from xahau.models.currencies.issued_currency import IssuedCurrency
from xahau.models.currencies.xah import XAH

Currency = Union[IssuedCurrency, XAH]
