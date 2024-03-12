import hashlib
from xrpl.core import addresscodec
from xrpl.utils import str_to_hex

# Constants
HEX = 16
BYTE_LENGTH = 32

# Ledger space dictionary
ledger_spaces = {
    'account': 'a',
    'dirNode': 'd',
    'generatorMap': 'g',
    'rippleState': 'r',
    'offer': 'o',
    'ownerDir': 'O',
    'bookDir': 'B',
    'contract': 'c',
    'skipList': 's',
    'escrow': 'u',
    'amendment': 'f',
    'feeSettings': 'e',
    'ticket': 'T',
    'signerList': 'S',
    'paychan': 'x',
    'check': 'C',
    'uriToken': 'U',
    'depositPreauth': 'p',
}


def sha512_half(data: str) -> str:
    """Compute the SHA-512 hash and then take the first half of the result."""
    hash_obj = hashlib.sha512(bytes.fromhex(data))
    return hash_obj.hexdigest()[:64].upper()


def address_to_hex(address: str) -> str:
    """Convert an address to its hexadecimal representation."""
    # Assuming the address is already in hexadecimal form.
    # If the address is in another format, you will need to convert it to hex.
    return addresscodec.decode_classic_address(address).hex()

def ledger_space_hex(name: str) -> str:
    """Get the hexadecimal representation of a ledger space."""
    return format(ord(ledger_spaces[name]), 'x').zfill(4)


def hash_offer(address: str, sequence: int) -> str:
    """Compute the hash of a Offer."""
    return sha512_half(
        ledger_space_hex('offer') +
        address_to_hex(address) +
        format(sequence, 'x').zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_check(address: str, sequence: int) -> str:
    """Compute the hash of a Check."""
    return sha512_half(
        ledger_space_hex('check') +
        address_to_hex(address) +
        format(sequence, 'x').zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_escrow(address: str, sequence: int) -> str:
    """Compute the hash of a Escrow."""
    return sha512_half(
        ledger_space_hex('escrow') +
        address_to_hex(address) +
        format(sequence, 'x').zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_payment_channel(address: str, dst_address: str, sequence: int) -> str:
    """Compute the hash of a Payment Channel."""
    return sha512_half(
        ledger_space_hex('paychan') +
        address_to_hex(address) +
        address_to_hex(dst_address) +
        format(sequence, 'x').zfill(BYTE_LENGTH * 2)
    ).upper()


def hash_uri_token(issuer: str, uri: str) -> str:
    """Compute the hash of a URIToken."""
    return sha512_half(
        ledger_space_hex('uriToken') +
        address_to_hex(issuer) +
        str_to_hex(uri)
    ).upper()

def hash_hook(hex: str) -> str:
    """Compute the hash of a Hook."""
    return sha512_half(
        hex
    ).upper()