#!/usr/bin/env python
# coding: utf-8

"""Hooks-related helper util functions."""

import binascii
from typing import Any, Dict, List  # noqa: F401

from xrpl.constants import XRPLException
from xrpl.core.binarycodec.definitions import _TRANSACTION_TYPE_MAP, _TRANSACTION_TYPES


def calculate_hook_on(arr: List[str]) -> str:
    """
    Calculate the hook on value for a given list of transaction types.

    Args:
        arr: List of transaction types.

    Returns:
        A 256 hash of the transactions the hook will invoke on

    Raises:
        XRPLException: if the HookOn transaction type is not in the transaction types
    """
    tts = _TRANSACTION_TYPE_MAP
    s = "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffff"
    for n in arr:
        if n not in _TRANSACTION_TYPES:
            raise XRPLException(f"invalid transaction type '{n}' in HookOn array")
        v = int(s, 16)
        v ^= 1 << tts[n]
        s = "0x" + hex(v)[2:]

    s = s.replace("0x", "")
    s = s.zfill(64)
    return s.upper()


def hex_hook_parameters(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Hexlify the hook parameters

    Args:
        data: A list of Hook Parameters

    Returns:
        A list of Hook Parameters with the values in hex format
    """
    hook_parameters: List[Dict[str, Any]] = []
    for parameter in data:
        hook_parameters.append(
            {
                "HookParameter": {
                    "HookParameterName": binascii.hexlify(
                        parameter["HookParameter"]["HookParameterName"].encode("utf8")
                    )
                    .decode("utf-8")
                    .upper(),
                    "HookParameterValue": binascii.hexlify(
                        parameter["HookParameter"]["HookParameterValue"].encode("utf8")
                    )
                    .decode("utf-8")
                    .upper(),
                }
            }
        )
    return hook_parameters
