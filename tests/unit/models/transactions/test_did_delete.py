from unittest import TestCase

from xahau.models import DIDDelete

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"


class NoTestDIDDelete(TestCase):
    def test_valid(self):
        tx = DIDDelete(
            account=_ACCOUNT,
        )
        self.assertTrue(tx.is_valid())

    def test_invalid(self):
        with self.assertRaises(TypeError):
            DIDDelete(account=_ACCOUNT, field="invalid")
