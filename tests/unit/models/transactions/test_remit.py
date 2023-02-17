from unittest import TestCase

from xahau.models.amounts import AmountEntry, InnerAmount, IssuedCurrencyAmount
from xahau.models.exceptions import XAHLModelException
from xahau.models.transactions import MintURIToken, Remit
from xahau.utils import str_to_hex

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"
_FEE = "0.00001"
_SEQUENCE = 19048
_DIGEST = "AED08CC1F50DD5F23A1948AF86153A3F3B7593E5EC77D65A02BB1B29E05AB6AF"
_URI_TOKEN_ID = "AED08CC1F50DD5F23A1948AF86153A3F3B7593E5EC77D65A02BB1B29E05AB6AF"
_URI = "ipfs://CID"
_BAD_URI = "ipfs://AED08CC1F50DD5F23A1948AF86153A3F3B7593E5EC77D65A02BB1B29E05AB6A"
NATIVE_AMOUNT_ENTRY = AmountEntry(amount_entry=InnerAmount(amount="1"))
IC_AMOUNT_ENTRY = AmountEntry(
    amount_entry=InnerAmount(
        amount=IssuedCurrencyAmount(currency="BTC", value="1.002", issuer=_ACCOUNT)
    )
)
_DESTINATION = "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn"


class TestRemit(TestCase):
    def test_no_amounts(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
        }
        tx = Remit(**transaction_dict)
        self.assertTrue(tx.is_valid())

    def test_bad_native_amounts(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "amounts": [NATIVE_AMOUNT_ENTRY, NATIVE_AMOUNT_ENTRY],
        }
        with self.assertRaises(XAHLModelException):
            Remit(**transaction_dict)

    def test_bad_ic_amounts(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "amounts": [IC_AMOUNT_ENTRY, IC_AMOUNT_ENTRY],
        }
        with self.assertRaises(XAHLModelException):
            Remit(**transaction_dict)

    def test_amounts(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "amounts": [NATIVE_AMOUNT_ENTRY, IC_AMOUNT_ENTRY],
        }
        tx = Remit(**transaction_dict)
        self.assertTrue(tx.is_valid())

    def test_uri_token_mint(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "mint_uri_token": MintURIToken(
                uri=str_to_hex(_URI).upper(), digest=_DIGEST
            ),
        }
        tx = Remit(**transaction_dict)
        self.assertTrue(tx.is_valid())

    def test_uri_token_ids(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "uri_token_ids": [_URI_TOKEN_ID],
        }
        tx = Remit(**transaction_dict)
        self.assertTrue(tx.is_valid())

    def test_bad_uri_token_ids(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "uri_token_ids": [_URI_TOKEN_ID, _URI_TOKEN_ID],
        }
        with self.assertRaises(XAHLModelException):
            Remit(**transaction_dict)

    def test_all(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "amounts": [NATIVE_AMOUNT_ENTRY, IC_AMOUNT_ENTRY],
            "mint_uri_token": MintURIToken(
                uri=str_to_hex(_URI).upper(), digest=_DIGEST
            ),
            "uri_token_ids": [_URI_TOKEN_ID],
        }
        tx = Remit(**transaction_dict)
        self.assertTrue(tx.is_valid())

    def test_bad_inform(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "inform": _DESTINATION,
        }
        with self.assertRaises(XAHLModelException):
            Remit(**transaction_dict)

    def test_bad_digest(self):
        transaction_dict = {
            "account": _ACCOUNT,
            "fee": _FEE,
            "sequence": _SEQUENCE,
            "destination": _DESTINATION,
            "mint_uri_token": MintURIToken(
                uri=str_to_hex(_URI).upper(), digest="DEADBEEF"
            ),
        }
        with self.assertRaises(XAHLModelException):
            Remit(**transaction_dict)
