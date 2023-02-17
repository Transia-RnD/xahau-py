from unittest import TestCase

from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import Hook, SetHook, SetHookFlag

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"
_FEE = "0.00001"
_SEQUENCE = 19048
_BINARY = "0061736D01000000011C0460057F7F7F7F7F017E"
"60037F7F7E017E60027F7F017F60017F017E02230303656E76057"
"472616365000003656E7606616363657074000103656E76025F67"
"0002030201030503010002062B077F0141B088040B7F004180080"
"B7F0041A6080B7F004180080B7F0041B088040B7F0041000B7F00"
"41010B07080104686F6F6B00030AC4800001C0800001017F23004"
"1106B220124002001200036020C41920841134180084112410010"
"001A410022002000420010011A41012200200010021A200141106"
"A240042000B0B2C01004180080B254163636570742E633A204361"
"6C6C65642E00224163636570742E633A2043616C6C65642E22"
_BAD_HOOK_ON = "000000000000000000000000000000000000000000000000000000000000000000"
_HOOK_ON = "0000000000000000000000000000000000000000000000000000000000000000"
_BAD_NAMESPACE = "9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A0800"
_NAMESPACE = "9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08"
_VERSION = 0
_FLAGS = 1


class TestSetHook(TestCase):
    def test_invalid_hook_on(self):
        with self.assertRaises(XAHLModelException):
            hook = Hook(
                create_code=_BINARY,
                flags=_FLAGS,
                hook_api_version=_VERSION,
                hook_namespace=_NAMESPACE,
                hook_on=_BAD_HOOK_ON,
            )
            SetHook(
                account=_ACCOUNT,
                fee=_FEE,
                sequence=_SEQUENCE,
                hooks=[hook],
            )
        with self.assertRaises(XAHLModelException):
            hook = Hook(
                create_code=_BINARY,
                flags=_FLAGS,
                hook_api_version=_VERSION,
                hook_namespace=_NAMESPACE,
                hook_on="",
            )
            SetHook(
                account=_ACCOUNT,
                fee=_FEE,
                sequence=_SEQUENCE,
                hooks=[hook],
            )

    def test_invalid_hook_namespace(self):
        with self.assertRaises(XAHLModelException):
            hook = Hook(
                create_code=_BINARY,
                flags=_FLAGS,
                hook_api_version=_VERSION,
                hook_namespace=_BAD_NAMESPACE,
                hook_on=_HOOK_ON,
            )
            SetHook(
                account=_ACCOUNT,
                fee=_FEE,
                sequence=_SEQUENCE,
                hooks=[hook],
            )
        with self.assertRaises(XAHLModelException):
            hook = Hook(
                create_code=_BINARY,
                flags=_FLAGS,
                hook_api_version=_VERSION,
                hook_namespace="",
                hook_on=_HOOK_ON,
            )
            SetHook(
                account=_ACCOUNT,
                fee=_FEE,
                sequence=_SEQUENCE,
                hooks=[hook],
            )

    def test_invalid_num_hooks(self):
        with self.assertRaises(XAHLModelException):
            hook = Hook(
                create_code=_BINARY,
                flags=_FLAGS,
                hook_api_version=_VERSION,
                hook_namespace=_NAMESPACE,
                hook_on=_HOOK_ON,
            )
            SetHook(
                account=_ACCOUNT,
                fee=_FEE,
                sequence=_SEQUENCE,
                hooks=[
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                    hook,
                ],
            )

    def test_invalid_flag(self):
        hook = Hook(
            create_code=_BINARY,
            flags=[SetHookFlag.HSF_OVERRIDE, SetHookFlag.HSF_COLLECT],
            hook_api_version=_VERSION,
            hook_namespace=_NAMESPACE,
            hook_on=_HOOK_ON,
        )
        tx = SetHook(
            account=_ACCOUNT,
            fee=_FEE,
            sequence=_SEQUENCE,
            hooks=[
                hook,
            ],
        )
        self.assertTrue(tx.is_valid())
        self.assertEqual(tx.to_xrpl()["Hooks"][0]["Hook"]["Flags"], 5)
