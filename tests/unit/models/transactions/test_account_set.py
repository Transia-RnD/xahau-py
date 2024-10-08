from unittest import TestCase

from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import AccountSet, AccountSetAsfFlag

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"
_ANOTHER_ACCOUNT = "rsA2LpzuawewSBQXkiju3YQTMzW13pAAdW"
_FEE = "0.00001"
_SEQUENCE = 19048


class TestAccountSet(TestCase):
    def test_same_set_flag_and_clear_flag(self):
        set_flag = 3
        clear_flag = 3
        domain = "asjcsodafsaid0f9asdfasdf"
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "set_flag": set_flag,
            "clear_flag": clear_flag,
            "domain": domain,
            "sequence": _SEQUENCE,
        }
        with self.assertRaises(XAHLModelException):
            AccountSet(**transaction_dict)

    def test_no_set_flag_or_clear_flag(self):
        tx = AccountSet(
            **{
                "account": _ACCOUNT,
                "fee": _FEE,
                "sequence": _SEQUENCE,
            }
        )
        self.assertTrue(tx.is_valid())

    def test_uppercase_domain(self):
        clear_flag = 3
        domain = "asjcsodAOIJFsaid0f9asdfasdf"
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "clear_flag": clear_flag,
            "domain": domain,
            "sequence": _SEQUENCE,
        }
        with self.assertRaises(XAHLModelException):
            AccountSet(**transaction_dict)

    def test_domain_too_long(self):
        domain = "asjcsodafsaid0f9asdfasdf"
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "domain": domain * 1000,
            "sequence": _SEQUENCE,
        }
        with self.assertRaises(XAHLModelException):
            AccountSet(**transaction_dict)

    def test_invalid_tick_size(self):
        clear_flag = 3
        tick_size = 39
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "clear_flag": clear_flag,
            "tick_size": tick_size,
            "sequence": _SEQUENCE,
        }
        with self.assertRaises(XAHLModelException):
            AccountSet(**transaction_dict)

    def test_invalid_transfer_rate(self):
        clear_flag = 3
        transfer_rate = 39
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "clear_flag": clear_flag,
            "transfer_rate": transfer_rate,
            "sequence": _SEQUENCE,
        }
        with self.assertRaises(XAHLModelException):
            AccountSet(**transaction_dict)

    def test_nftoken_minter_set_without_minter_flag(self):
        with self.assertRaises(XAHLModelException):
            AccountSet(
                account=_ACCOUNT,
                fee=_FEE,
                nftoken_minter=_ANOTHER_ACCOUNT,
            )

    def test_nftoken_minter_not_set_with_minter_flag(self):
        with self.assertRaises(XAHLModelException):
            AccountSet(
                account=_ACCOUNT,
                fee=_FEE,
                set_flag=AccountSetAsfFlag.ASF_AUTHORIZED_NFTOKEN_MINTER,
            )

    def test_nftoken_minter_set_with_clear_minter_flag(self):
        with self.assertRaises(XAHLModelException):
            AccountSet(
                account=_ACCOUNT,
                fee=_FEE,
                clear_flag=AccountSetAsfFlag.ASF_AUTHORIZED_NFTOKEN_MINTER,
                nftoken_minter=_ANOTHER_ACCOUNT,
            )

    def test_nftoken_minter_set_with_minter_flag(self):
        tx = AccountSet(
            account=_ACCOUNT,
            fee=_FEE,
            set_flag=AccountSetAsfFlag.ASF_AUTHORIZED_NFTOKEN_MINTER,
            nftoken_minter=_ANOTHER_ACCOUNT,
        )
        self.assertTrue(tx.is_valid())

    def test_nftoken_minter_not_set_with_clear_minter_flag(self):
        tx = AccountSet(
            account=_ACCOUNT,
            fee=_FEE,
            clear_flag=AccountSetAsfFlag.ASF_AUTHORIZED_NFTOKEN_MINTER,
        )
        self.assertTrue(tx.is_valid())
