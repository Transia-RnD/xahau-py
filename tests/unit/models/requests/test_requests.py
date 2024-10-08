from unittest import TestCase

from xahau.models.requests import Fee, GenericRequest
from xahau.models.requests.request import _DEFAULT_API_VERSION


class TestRequest(TestCase):
    def test_to_dict_includes_method_as_string(self):
        tx = Fee()
        value = tx.to_dict()["method"]
        self.assertEqual(type(value), str)

    def test_generic_request_to_dict_sets_command_as_method(self):
        command = "validator_list_sites"
        tx = GenericRequest(command=command).to_dict()
        self.assertDictEqual(
            tx, {"method": command, "api_version": _DEFAULT_API_VERSION}
        )
