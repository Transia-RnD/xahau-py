"""Handles the XAHL type and definition specifics."""

from xahau.core.binarycodec.definitions.definitions import (
    _TRANSACTION_TYPE_MAP,
    _TRANSACTION_TYPES,
    get_field_header_from_name,
    get_field_instance,
    get_field_name_from_header,
    get_ledger_entry_type_code,
    get_ledger_entry_type_name,
    get_transaction_result_code,
    get_transaction_result_name,
    get_transaction_type_code,
    get_transaction_type_name,
    load_definitions,
)
from xahau.core.binarycodec.definitions.field_header import FieldHeader
from xahau.core.binarycodec.definitions.field_info import FieldInfo
from xahau.core.binarycodec.definitions.field_instance import FieldInstance

__all__ = [
    "_TRANSACTION_TYPE_MAP",
    "_TRANSACTION_TYPES",
    "FieldHeader",
    "FieldInfo",
    "FieldInstance",
    "load_definitions",
    "get_field_header_from_name",
    "get_field_name_from_header",
    "get_field_instance",
    "get_ledger_entry_type_code",
    "get_ledger_entry_type_name",
    "get_transaction_result_code",
    "get_transaction_result_name",
    "get_transaction_type_code",
    "get_transaction_type_name",
]
