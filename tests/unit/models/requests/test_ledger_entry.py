from unittest import TestCase

from xahau.models import XAH, LedgerEntry, XChainBridge
from xahau.models.exceptions import XAHLModelException
from xahau.models.requests.ledger_entry import Oracle, RippleState


class TestLedgerEntry(TestCase):
    def test_has_only_index_is_valid(self):
        req = LedgerEntry(
            index="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_account_root_is_valid(self):
        req = LedgerEntry(
            account_root="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_directory_is_valid(self):
        req = LedgerEntry(
            directory="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_offer_is_valid(self):
        req = LedgerEntry(
            offer="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_ripple_state_is_valid(self):
        req = LedgerEntry(
            ripple_state=RippleState(
                accounts=["account1", "account2"],
                currency="USD",
            ),
        )
        self.assertTrue(req.is_valid())

    def test_has_only_check_is_valid(self):
        req = LedgerEntry(
            check="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_escrow_is_valid(self):
        req = LedgerEntry(
            escrow="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_payment_channel_is_valid(self):
        req = LedgerEntry(
            payment_channel="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_deposit_preauth_is_valid(self):
        req = LedgerEntry(
            deposit_preauth="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_ticket_is_valid(self):
        req = LedgerEntry(
            ticket="hello",
        )
        self.assertTrue(req.is_valid())

    def test_has_only_xchain_claim_id_is_valid(self):
        req = LedgerEntry(
            xchain_claim_id=1,
        )
        self.assertTrue(req.is_valid())

    def test_has_only_xchain_create_account_claim_id_is_valid(self):
        req = LedgerEntry(
            xchain_create_account_claim_id=1,
        )
        self.assertTrue(req.is_valid())

    def test_has_both_bridge_fields_is_valid(self):
        req = LedgerEntry(
            bridge=XChainBridge(
                locking_chain_door="rGzx83BVoqTYbGn7tiVAnFw7cbxjin13jL",
                locking_chain_issue=XAH(),
                issuing_chain_door="r3kmLJN5D28dHuH8vZNUZpMC43pEHpaocV",
                issuing_chain_issue=XAH(),
            ),
            bridge_account="rGzx83BVoqTYbGn7tiVAnFw7cbxjin13jL",
        )
        self.assertTrue(req.is_valid())

    def test_missing_bridge_field_is_invalid(self):
        with self.assertRaises(XAHLModelException):
            LedgerEntry(
                bridge=XChainBridge(
                    locking_chain_door="rGzx83BVoqTYbGn7tiVAnFw7cbxjin13jL",
                    locking_chain_issue=XAH(),
                    issuing_chain_door="r3kmLJN5D28dHuH8vZNUZpMC43pEHpaocV",
                    issuing_chain_issue=XAH(),
                ),
            )

        with self.assertRaises(XAHLModelException):
            LedgerEntry(
                bridge_account="rGzx83BVoqTYbGn7tiVAnFw7cbxjin13jL",
            )

    def test_has_no_query_param_is_invalid(self):
        with self.assertRaises(XAHLModelException):
            LedgerEntry()

    def test_has_multiple_query_params_is_invalid(self):
        with self.assertRaises(XAHLModelException):
            LedgerEntry(
                index="hello",
                account_root="hello",
            )

    # fetch a valid PriceOracle object
    def test_get_price_oracle(self):
        # oracle_document_id is specified as uint
        req = LedgerEntry(
            oracle=Oracle(
                account="rB6XJbxKx2oBSK1E3Hvh7KcZTCCBukWyhv",
                oracle_document_id=1,
            ),
        )
        self.assertTrue(req.is_valid())

        # oracle_document_id is specified as string
        req = LedgerEntry(
            oracle=Oracle(
                account="rB6XJbxKx2oBSK1E3Hvh7KcZTCCBukWyhv",
                oracle_document_id="1",
            ),
        )
        self.assertTrue(req.is_valid())

    def test_invalid_price_oracle_object(self):
        # missing oracle_document_id
        with self.assertRaises(XAHLModelException):
            LedgerEntry(
                oracle=Oracle(account="rB6XJbxKx2oBSK1E3Hvh7KcZTCCBukWyhv"),
            )

        # missing account information
        with self.assertRaises(XAHLModelException):
            LedgerEntry(
                oracle=Oracle(oracle_document_id=1),
            )
