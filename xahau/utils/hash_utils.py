"""Hash Utilities"""

import hashlib

from xahau.core import addresscodec
from xahau.utils import str_to_hex

# Constants
HEX = 16
BYTE_LENGTH = 32

# Ledger space dictionary
ledger_spaces = {
    "account": "a",
    "dirNode": "d",
    "generatorMap": "g",
    "rippleState": "r",
    "offer": "o",
    "ownerDir": "O",
    "bookDir": "B",
    "contract": "c",
    "skipList": "s",
    "escrow": "u",
    "amendment": "f",
    "feeSettings": "e",
    "ticket": "T",
    "signerList": "S",
    "paychan": "x",
    "check": "C",
    "uriToken": "U",
    "depositPreauth": "p",
}


def sha512_half(data: str) -> str:
    """Compute the SHA-512 hash and then take the first half of the result.

    Args:
        data (str): The input data in hexadecimal format.

    Returns:
        str: The first half of the SHA-512 hash in uppercase hexadecimal.
    """
    hash_obj = hashlib.sha512(bytes.fromhex(data))
    return hash_obj.hexdigest()[:64].upper()


def address_to_hex(address: str) -> str:
    """Convert an address to its hexadecimal representation.

    Args:
        address (str): The address to convert.

    Returns:
        str: The hexadecimal representation of the address.
    """
    return addresscodec.decode_classic_address(address).hex()


def ledger_space_hex(name: str) -> str:
    """Get the hexadecimal representation of a ledger space.

    Args:
        name (str): The name of the ledger space.

    Returns:
        str: The hexadecimal representation of the ledger space.
    """
    return format(ord(ledger_spaces[name]), "x").zfill(4)


def hash_offer(address: str, sequence: int) -> str:
    """Compute the hash of an Offer.

    Args:
        address (str): The address associated with the offer.
        sequence (int): The sequence number of the offer.

    Returns:
        str: The computed hash of the offer in uppercase hexadecimal.
    """
    return sha512_half(
        ledger_space_hex("offer")
        + address_to_hex(address)
        + format(sequence, "x").zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_check(address: str, sequence: int) -> str:
    """Compute the hash of a Check.

    Args:
        address (str): The address associated with the check.
        sequence (int): The sequence number of the check.

    Returns:
        str: The computed hash of the check in uppercase hexadecimal.
    """
    return sha512_half(
        ledger_space_hex("check")
        + address_to_hex(address)
        + format(sequence, "x").zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_escrow(address: str, sequence: int) -> str:
    """Compute the hash of an Escrow.

    Args:
        address (str): The address associated with the escrow.
        sequence (int): The sequence number of the escrow.

    Returns:
        str: The computed hash of the escrow in uppercase hexadecimal.
    """
    return sha512_half(
        ledger_space_hex("escrow")
        + address_to_hex(address)
        + format(sequence, "x").zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_payment_channel(address: str, dst_address: str, sequence: int) -> str:
    """Compute the hash of a Payment Channel.

    Args:
        address (str): The address of the payment channel.
        dst_address (str): The destination address for the payment channel.
        sequence (int): The sequence number of the payment channel.

    Returns:
        str: The computed hash of the payment channel in uppercase hexadecimal.
    """
    return sha512_half(
        ledger_space_hex("paychan")
        + address_to_hex(address)
        + address_to_hex(dst_address)
        + format(sequence, "x").zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_uri_token(issuer: str, uri: str) -> str:
    """Compute the hash of a URIToken.

    Args:
        issuer (str): The address of the issuer.
        uri (str): The URI associated with the token.

    Returns:
        str: The computed hash of the URI token in uppercase hexadecimal.
    """
    return sha512_half(
        ledger_space_hex("uriToken") + address_to_hex(issuer) + str_to_hex(uri)
    ).upper()


def hash_hook(hex: str) -> str:
    """Compute the hash of a Hook.

    Args:
        hex (str): The hexadecimal representation of the hook.

    Returns:
        str: The computed hash of the hook in uppercase hexadecimal.
    """
    return sha512_half(hex).upper()
