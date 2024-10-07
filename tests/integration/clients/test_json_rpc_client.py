"""Test the json_rpc_client."""

from __future__ import annotations

from unittest import TestCase

from xahau.clients import JsonRpcClient
from xahau.models.requests import ServerInfo


class TestJsonRpcClient(TestCase):
    """Test json_rpc_client."""

    def test_json_rpc_client_valid_url(self) -> None:
        # Valid URL
        JSON_RPC_URL = "https://xahau-test.net"
        client = JsonRpcClient(JSON_RPC_URL)
        client.request(ServerInfo())
