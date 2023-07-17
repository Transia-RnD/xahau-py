from typing import Any, List
from unittest import TestCase

from xrpl import XRPLException
from xrpl.utils import calculate_hook_on, hex_hook_parameters

_HOOK_ON_DEFAULT = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFFFF"
_HOOK_ON = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFFF7"
_PARAM_NAME = "6E616D6531"
_PARAM_VALUE = "76616C756531"


class TestHooks(TestCase):
    def test_calculate_hook_on_invalid(self):
        with self.assertRaises(XRPLException):
            calculate_hook_on(["AccountSet1"])

    def test_calculate_hook_on_all(self):
        hook_on: str = calculate_hook_on([])
        self.assertEqual(hook_on, _HOOK_ON_DEFAULT)

    def test_calculate_hook_on_account_set(self):
        invoke_on: List[str] = ["AccountSet"]
        hook_on_values: List[str] = [v for v in invoke_on]
        hook_on: str = calculate_hook_on(hook_on_values)
        self.assertEqual(hook_on, _HOOK_ON)

    def test_hook_parameters(self):
        parameters: List[Any] = [
            {
                "HookParameter": {
                    "HookParameterName": "name1",
                    "HookParameterValue": "value1",
                }
            }
        ]
        result: str = hex_hook_parameters(parameters)
        self.assertEqual(
            result,
            [
                {
                    "HookParameter": {
                        "HookParameterName": _PARAM_NAME,
                        "HookParameterValue": _PARAM_VALUE,
                    }
                }
            ],
        )
