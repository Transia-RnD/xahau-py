[![Documentation Status](https://readthedocs.org/projects/xahau-py/badge)](https://xahau-py.readthedocs.io/)

# xahau-py

A pure Python implementation for interacting with the [XRP Ledger](https://xahau.org/).

The `xahau-py` library simplifies the hardest parts of XRP Ledger interaction, like serialization and transaction signing. It also provides native Python methods and models for [XRP Ledger transactions](https://xahau.org/transaction-formats.html) and core server [API](https://xahau.org/api-conventions.html) ([`rippled`](https://github.com/ripple/rippled)) objects.

As an example, this is how you would use this library to send a payment on testnet:

```py
from xahau.account import get_balance
from xahau.clients import JsonRpcClient
from xahau.models import Payment, Tx
from xahau.transaction import submit_and_wait
from xahau.wallet import generate_faucet_wallet

# Create a client to connect to the test network
client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# Create two wallets to send money between on the test network
wallet1 = generate_faucet_wallet(client, debug=True)
wallet2 = generate_faucet_wallet(client, debug=True)

# Both balances should be zero since nothing has been sent yet
print("Balances of wallets before Payment tx")
print(get_balance(wallet1.address, client))
print(get_balance(wallet2.address, client))

# Create a Payment transaction from wallet1 to wallet2
payment_tx = Payment(
    account=wallet1.address,
    amount="1000",
    destination=wallet2.address,
)

# Submit the payment to the network and wait to see a response
#   Behind the scenes, this fills in fields which can be looked up automatically like the fee.
#   It also signs the transaction with wallet1 to prove you own the account you're paying from.
payment_response = submit_and_wait(payment_tx, client, wallet1)
print("Transaction was submitted")

# Create a "Tx" request to look up the transaction on the ledger
tx_response = client.request(Tx(transaction=payment_response.result["hash"]))

# Check whether the transaction was actually validated on ledger
print("Validated:", tx_response.result["validated"])

# Check balances after 1000 drops (.001 XRP) was sent from wallet1 to wallet2
print("Balances of wallets after Payment tx:")
print(get_balance(wallet1.address, client))
print(get_balance(wallet2.address, client))
```

[![Downloads](https://pepy.tech/badge/xahau-py/month)](https://pepy.tech/project/xahau-py/month)
[![Contributors](https://img.shields.io/github/contributors/xpring-eng/xahau-py.svg)](https://github.com/xpring-eng/xahau-py/graphs/contributors)

## Installation and supported versions

The `xahau-py` library is available on [PyPI](https://pypi.org/). Install with `pip`:


```
pip3 install xahau-py
```

The library supports [Python 3.8](https://www.python.org/downloads/) and later.

[![Supported Versions](https://img.shields.io/pypi/pyversions/xahau-py.svg)](https://pypi.org/project/xahau-py)


## Features

Use `xahau-py` to build Python applications that leverage the [XRP Ledger](https://xahau.org/). The library helps with all aspects of interacting with the XRP Ledger, including:

* Key and wallet management
* Serialization
* Transaction Signing

`xahau-py` also provides:

* A network client — See [`xahau.clients`](https://xahau-py.readthedocs.io/en/stable/source/xahau.clients.html) for more information.
* Methods for inspecting accounts — See [XRPL Account Methods](https://xahau-py.readthedocs.io/en/stable/source/xahau.account.html) for more information.
* Codecs for encoding and decoding addresses and other objects — See [Core Codecs](https://xahau-py.readthedocs.io/en/stable/source/xahau.core.html) for more information.

## [➡️ Reference Documentation](https://xahau-py.readthedocs.io/en/stable/)

See the complete [`xahau-py` reference documentation on Read the Docs](https://xahau-py.readthedocs.io/en/stable/index.html).


## Usage

The following sections describe some of the most commonly used modules in the `xahau-py` library and provide sample code.

### Network client

Use the `xahau.clients` library to create a network client for connecting to the XRP Ledger.

```py
from xahau.clients import JsonRpcClient
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(JSON_RPC_URL)
```

### Manage keys and wallets

#### `xahau.wallet`

Use the [`xahau.wallet`](https://xahau-py.readthedocs.io/en/stable/source/xahau.wallet.html) module to create a wallet from a given seed or or via a [Testnet faucet](https://xahau.org/xrp-testnet-faucet.html).

To create a wallet from a seed (in this case, the value generated using [`xahau.keypairs`](#xahau-keypairs)):

```py
wallet_from_seed = xahau.wallet.Wallet.from_seed(seed)
print(wallet_from_seed)
# pub_key: ED46949E414A3D6D758D347BAEC9340DC78F7397FEE893132AAF5D56E4D7DE77B0
# priv_key: -HIDDEN-
# address: rG5ZvYsK5BPi9f1Nb8mhFGDTNMJhEhufn6
```

To create a wallet from a Testnet faucet:

```py
test_wallet = generate_faucet_wallet(client)
test_account = test_wallet.address
print("Classic address:", test_account)
# Classic address: rEQB2hhp3rg7sHj6L8YyR4GG47Cb7pfcuw
```

#### `xahau.core.keypairs`

Use the [`xahau.core.keypairs`](https://xahau-py.readthedocs.io/en/stable/source/xahau.core.keypairs.html#module-xahau.core.keypairs) module to generate seeds and derive keypairs and addresses from those seed values.

Here's an example of how to generate a `seed` value and derive an [XRP Ledger "classic" address](https://xahau.org/cryptographic-keys.html#account-id-and-address) from that seed.


```py
from xahau.core import keypairs
seed = keypairs.generate_seed()
public, private = keypairs.derive_keypair(seed)
test_account = keypairs.derive_classic_address(public)
print("Here's the public key:")
print(public)
print("Here's the private key:")
print(private)
print("Store this in a secure place!")
# Here's the public key:
# ED3CC1BBD0952A60088E89FA502921895FC81FBD79CAE9109A8FE2D23659AD5D56
# Here's the private key:
# EDE65EE7882847EF5345A43BFB8E6F5EEC60F45461696C384639B99B26AAA7A5CD
# Store this in a secure place!
```

**Note:** You can use `xahau.core.keypairs.sign` to sign transactions but `xahau-py` also provides explicit methods for safely signing and submitting transactions. See [Transaction Signing](#transaction-signing) and [XRPL Transaction Methods](https://xahau-py.readthedocs.io/en/stable/source/xahau.transaction.html#module-xahau.transaction) for more information.


### Serialize and sign transactions

To securely submit transactions to the XRP Ledger, you need to first serialize data from JSON and other formats into the [XRP Ledger's canonical format](https://xahau.org/serialization.html), then to [authorize the transaction](https://xahau.org/transaction-basics.html#authorizing-transactions) by digitally [signing it](https://xahau-py.readthedocs.io/en/stable/source/xahau.core.keypairs.html?highlight=sign#xahau.core.keypairs.sign) with the account's private key. The `xahau-py` library provides several methods to simplify this process.


Use the [`xahau.transaction`](https://xahau-py.readthedocs.io/en/stable/source/xahau.transaction.html) module to sign and submit transactions. The module offers three ways to do this:

* [`sign_and_submit`](https://xahau-py.readthedocs.io/en/stable/source/xahau.transaction.html#xahau.transaction.sign_and_submit) — Signs a transaction locally, then submits it to the XRP Ledger. This method does not implement [reliable transaction submission](https://xahau.org/reliable-transaction-submission.html#reliable-transaction-submission) best practices, so only use it for development or testing purposes.

* [`sign`](https://xahau-py.readthedocs.io/en/stable/source/xahau.transaction.html#xahau.transaction.sign) — Signs a transaction locally. This method **does  not** submit the transaction to the XRP Ledger.

* [`submit_and_wait`](https://xahau-py.readthedocs.io/en/stable/source/xahau.transaction.html#xahau.transaction.submit_and_wait) — An implementation of the [reliable transaction submission guidelines](https://xahau.org/reliable-transaction-submission.html#reliable-transaction-submission), this method submits a signed transaction to the XRP Ledger and then verifies that it has been included in a validated ledger (or has failed to do so). Use this method to submit transactions for production purposes.


```py
from xahau.models.transactions import Payment
from xahau.transaction import sign, submit_and_wait
from xahau.ledger import get_latest_validated_ledger_sequence
from xahau.account import get_next_valid_seq_number

current_validated_ledger = get_latest_validated_ledger_sequence(client)

# prepare the transaction
# the amount is expressed in drops, not XRP
# see https://xahau.org/basic-data-types.html#specifying-currency-amounts
my_tx_payment = Payment(
    account=test_wallet.address,
    amount="2200000",
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
    last_ledger_sequence=current_validated_ledger + 20,
    sequence=get_next_valid_seq_number(test_wallet.address, client),
    fee="10",
)
# sign the transaction
my_tx_payment_signed = sign(my_tx_payment,test_wallet)

# submit the transaction
tx_response = submit_and_wait(my_tx_payment_signed, client)
```

#### Get fee from the XRP Ledger


In most cases, you can specify the minimum [transaction cost](https://xahau.org/transaction-cost.html#current-transaction-cost) of `"10"` for the `fee` field unless you have a strong reason not to. But if you want to get the [current load-balanced transaction cost](https://xahau.org/transaction-cost.html#current-transaction-cost) from the network, you can use the `get_fee` function:

```py
from xahau.ledger import get_fee
fee = get_fee(client)
print(fee)
# 10
```

#### Auto-filled fields

The `xahau-py` library automatically populates the `fee`, `sequence` and `last_ledger_sequence` fields when you create transactions. In the example above, you could omit those fields and let the library fill them in for you.

```py
from xahau.models.transactions import Payment
from xahau.transaction import submit_and_wait, autofill_and_sign
# prepare the transaction
# the amount is expressed in drops, not XRP
# see https://xahau.org/basic-data-types.html#specifying-currency-amounts
my_tx_payment = Payment(
    account=test_wallet.address,
    amount="2200000",
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe"
)

# sign the transaction with the autofill method
# (this will auto-populate the fee, sequence, and last_ledger_sequence)
my_tx_payment_signed = autofill_and_sign(my_tx_payment, client, test_wallet)
print(my_tx_payment_signed)
# Payment(
#     account='rMPUKmzmDWEX1tQhzQ8oGFNfAEhnWNFwz',
#     transaction_type=<TransactionType.PAYMENT: 'Payment'>,
#     fee='10',
#     sequence=16034065,
#     account_txn_id=None,
#     flags=0,
#     last_ledger_sequence=10268600,
#     memos=None,
#     signers=None,
#     source_tag=None,
#     signing_pub_key='EDD9540FA398915F0BCBD6E65579C03BE5424836CB68B7EB1D6573F2382156B444',
#     txn_signature='938FB22AE7FE76CF26FD11F8F97668E175DFAABD2977BCA397233117E7E1C4A1E39681091CC4D6DF21403682803AB54CC21DC4FA2F6848811DEE10FFEF74D809',
#     amount='2200000',
#     destination='rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe',
#     destination_tag=None,
#     invoice_id=None,
#     paths=None,
#     send_max=None,
#     deliver_min=None
# )

# submit the transaction
tx_response = submit_and_wait(my_tx_payment_signed, client)
```


### Subscribe to ledger updates

You can send `subscribe` and `unsubscribe` requests only using the WebSocket network client. These request methods allow you to be alerted of certain situations as they occur, such as when a new ledger is declared.

```py
from xahau.clients import WebsocketClient
url = "wss://s.altnet.rippletest.net/"
from xahau.models import Subscribe, StreamParameter
req = Subscribe(streams=[StreamParameter.LEDGER])
# NOTE: this code will run forever without a timeout, until the process is killed
with WebsocketClient(url) as client:
    client.send(req)
    for message in client:
        print(message)
# {'result': {'fee_base': 10, 'fee_ref': 10, 'ledger_hash': '7CD50477F23FF158B430772D8E82A961376A7B40E13C695AA849811EDF66C5C0', 'ledger_index': 18183504, 'ledger_time': 676412962, 'reserve_base': 20000000, 'reserve_inc': 5000000, 'validated_ledgers': '17469391-18183504'}, 'status': 'success', 'type': 'response'}
# {'fee_base': 10, 'fee_ref': 10, 'ledger_hash': 'BAA743DABD168BD434804416C8087B7BDEF7E6D7EAD412B9102281DD83B10D00', 'ledger_index': 18183505, 'ledger_time': 676412970, 'reserve_base': 20000000, 'reserve_inc': 5000000, 'txn_count': 0, 'type': 'ledgerClosed', 'validated_ledgers': '17469391-18183505'}
# {'fee_base': 10, 'fee_ref': 10, 'ledger_hash': 'D8227DAF8F745AE3F907B251D40B4081E019D013ABC23B68C0B1431DBADA1A46', 'ledger_index': 18183506, 'ledger_time': 676412971, 'reserve_base': 20000000, 'reserve_inc': 5000000, 'txn_count': 0, 'type': 'ledgerClosed', 'validated_ledgers': '17469391-18183506'}
# {'fee_base': 10, 'fee_ref': 10, 'ledger_hash': 'CFC412B6DDB9A402662832A781C23F0F2E842EAE6CFC539FEEB287318092C0DE', 'ledger_index': 18183507, 'ledger_time': 676412972, 'reserve_base': 20000000, 'reserve_inc': 5000000, 'txn_count': 0, 'type': 'ledgerClosed', 'validated_ledgers': '17469391-18183507'}
```


### Asynchronous Code

This library supports Python's [`asyncio`](https://docs.python.org/3/library/asyncio.html) package, which is used to run asynchronous code. All the async code is in [`xahau.asyncio`](https://xahau-py.readthedocs.io/en/stable/source/xahau.asyncio.html) If you are writing asynchronous code, please note that you will not be able to use any synchronous sugar functions, due to how event loops are handled. However, every synchronous method has a corresponding asynchronous method that you can use.

This sample code is the asynchronous equivalent of the above section on submitting a transaction.

```py
import asyncio
from xahau.models.transactions import Payment
from xahau.asyncio.transaction import sign, submit_and_wait
from xahau.asyncio.ledger import get_latest_validated_ledger_sequence
from xahau.asyncio.account import get_next_valid_seq_number
from xahau.asyncio.clients import AsyncJsonRpcClient

async_client = AsyncJsonRpcClient(JSON_RPC_URL)

async def submit_sample_transaction():
    current_validated_ledger = await get_latest_validated_ledger_sequence(async_client)

    # prepare the transaction
    # the amount is expressed in drops, not XRP
    # see https://xahau.org/basic-data-types.html#specifying-currency-amounts
    my_tx_payment = Payment(
        account=test_wallet.address,
        amount="2200000",
        destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
        last_ledger_sequence=current_validated_ledger + 20,
        sequence=await get_next_valid_seq_number(test_wallet.address, async_client),
        fee="10",
    )
    # sign and submit the transaction
    tx_response = await submit_and_wait(my_tx_payment_signed, async_client, test_wallet)

asyncio.run(submit_sample_transaction())
```

### Encode addresses

Use [`xahau.core.addresscodec`](https://xahau-py.readthedocs.io/en/stable/source/xahau.core.addresscodec.html) to encode and decode addresses into and from the ["classic" and X-address formats](https://xahau.org/accounts.html#addresses).

```py
# convert classic address to x-address
from xahau.core import addresscodec
testnet_xaddress = (
    addresscodec.classic_address_to_xaddress(
        "rMPUKmzmDWEX1tQhzQ8oGFNfAEhnWNFwz",
        tag=0,
        is_test_network=True,
    )
)
print(testnet_xaddress)
# T7QDemmxnuN7a52A62nx2fxGPWcRahLCf3qaswfrsNW9Lps
```

## Migrating

If you're currently using `xahau-py` version 1, you can use [this guide to migrate to v2](https://xahau.org/blog/2023/xahau-py-2.0-release.html).

## Contributing

If you want to contribute to this project, see [CONTRIBUTING.md].

### Mailing Lists

We have a low-traffic mailing list for announcements of new `xahau-py` releases. (About 1 email per week)

+ [Subscribe to xahau-announce](https://groups.google.com/g/xahau-announce)

If you're using the XRP Ledger in production, you should run a [rippled server](https://github.com/ripple/rippled) and subscribe to the ripple-server mailing list as well.

+ [Subscribe to ripple-server](https://groups.google.com/g/ripple-server)

### Code Samples
- For samples of common use cases, see the [XRPL.org Code Samples](https://xahau.org/code-samples.html) page.
- You can also browse those samples [directly on GitHub](https://github.com/XRPLF/xrpl-dev-portal/tree/master/content/_code-samples).

### Report an issue

Experienced an issue? Report it [here](https://github.com/XRPLF/xahau-py/issues/new).

## License

The `xahau-py` library is licensed under the ISC License. See [LICENSE] for more information.



[CONTRIBUTING.md]: CONTRIBUTING.md
[LICENSE]: LICENSE
