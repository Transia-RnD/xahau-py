"""The base class for models that involve a nested dictionary e.g. memos."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Type, Union

from typing_extensions import Self

from xahau.models.base_model import BaseModel, _key_to_json
from xahau.models.exceptions import XAHLModelException


def _get_nested_name(cls: Union[NestedModel, Type[NestedModel]]) -> str:
    if isinstance(cls, NestedModel):
        name = cls.__class__.__name__
    else:
        name = cls.__name__
    return _key_to_json(name)


class NestedModel(BaseModel):
    """The base class for models that involve a nested dictionary e.g. memos."""

    flags: Optional[Union[Dict[str, bool], int, List[int]]]

    @classmethod
    def is_dict_of_model(cls: Type[Self], dictionary: Any) -> bool:
        """
        Returns True if the input dictionary was derived by the `to_dict`
        method of an instance of this class. In other words, True if this is
        a dictionary representation of an instance of this class.

        NOTE: does not account for model inheritance, IE will only return True
        if dictionary represents an instance of this class, but not if
        dictionary represents an instance of a subclass of this class.

        Args:
            dictionary: The dictionary to check.

        Returns:
            True if dictionary is a dict representation of an instance of this
            class.
        """
        return (
            isinstance(dictionary, dict)
            and _get_nested_name(cls) in dictionary
            and super().is_dict_of_model(dictionary[_get_nested_name(cls)])
        )

    @classmethod
    def from_dict(cls: Type[Self], value: Dict[str, Any]) -> Self:
        """
        Construct a new NestedModel from a dictionary of parameters.

        Args:
            value: The value to construct the NestedModel from.

        Returns:
            A new NestedModel object, constructed using the given parameters.

        Raises:
            XAHLModelException: If the dictionary provided is invalid.
        """
        if _get_nested_name(cls) not in value:
            return super(NestedModel, cls).from_dict(value)
        return super(NestedModel, cls).from_dict(value[_get_nested_name(cls)])

    def _iter_to_int(
        self: Self,
        lst: List[int],
    ) -> int:
        """Calculate flag as int."""
        accumulator = 0
        for flag in lst:
            accumulator |= flag
        return accumulator

    def _flags_to_int(self: Self) -> int:
        if not self.flags:
            return 0
        if isinstance(self.flags, int):
            return self.flags
        if isinstance(self.flags, dict):
            raise XAHLModelException(
                f"Nested Model Flags must be a list of integers, "
                f"not a dictionary: {self.flags}"
            )

        return self._iter_to_int(lst=self.flags)

    def to_dict(self: Self) -> Dict[str, Any]:
        """
        Returns the dictionary representation of a NestedModel.

        Returns:
            The dictionary representation of a NestedModel.
        """
        if _get_nested_name(self) == "hook":
            return {
                _get_nested_name(self): {
                    **super().to_dict(),
                    "flags": self._flags_to_int(),
                }
            }
        return {_get_nested_name(self): super().to_dict()}
