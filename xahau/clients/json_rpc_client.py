"""A sync client for interacting with the rippled JSON RPC."""
from xahau.asyncio.clients.json_rpc_base import JsonRpcBase
from xahau.clients.sync_client import SyncClient


class JsonRpcClient(SyncClient, JsonRpcBase):
    """A sync client for interacting with the rippled JSON RPC."""

    pass
