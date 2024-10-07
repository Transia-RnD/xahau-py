"""An async client for interacting with the rippled JSON RPC."""
from xahau.asyncio.clients.async_client import AsyncClient
from xahau.asyncio.clients.json_rpc_base import JsonRpcBase


class AsyncJsonRpcClient(AsyncClient, JsonRpcBase):
    """An async client for interacting with the rippled JSON RPC."""

    pass
