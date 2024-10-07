"""
Specifies an amount in an issued currency, but without a value field.
This format is used for some book order requests.

See https://xrpl.org/currency-formats.html#specifying-currency-amounts
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Union

from typing_extensions import Self

import xahau.models.amounts  # not a direct import, to get around circular imports
from xahau.constants import HEX_CURRENCY_REGEX, ISO_CURRENCY_REGEX
from xahau.models.base_model import BaseModel
from xahau.models.required import REQUIRED
from xahau.models.utils import KW_ONLY_DATACLASS, require_kwargs_on_init


def _is_valid_currency(candidate: str) -> bool:
    return bool(
        ISO_CURRENCY_REGEX.fullmatch(candidate)
        or HEX_CURRENCY_REGEX.fullmatch(candidate)
    )


@require_kwargs_on_init
@dataclass(frozen=True, **KW_ONLY_DATACLASS)
class IssuedCurrency(BaseModel):
    """
    Specifies an amount in an issued currency, but without a value field.
    This format is used for some book order requests.

    See https://xrpl.org/currency-formats.html#specifying-currency-amounts
    """

    currency: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    issuer: str = REQUIRED  # type: ignore
    """
    This field is required.

    :meta hide-value:
    """

    def _get_errors(self: Self) -> Dict[str, str]:
        errors = super()._get_errors()
        if self.currency.upper() == "XAH":
            errors["currency"] = "Currency must not be XAH for issued currency"
        elif not _is_valid_currency(self.currency):
            errors["currency"] = f"Invalid currency {self.currency}"
        return errors

    def to_amount(
        self: Self, value: Union[str, int, float]
    ) -> xahau.models.amounts.IssuedCurrencyAmount:
        """
        Converts an IssuedCurrency to an IssuedCurrencyAmount.

        Args:
            value: The amount of issued currency in the IssuedCurrencyAmount.

        Returns:
            An IssuedCurrencyAmount that represents the issued currency and the
                provided value.
        """
        return xahau.models.amounts.IssuedCurrencyAmount(
            currency=self.currency, issuer=self.issuer, value=str(value)
        )
