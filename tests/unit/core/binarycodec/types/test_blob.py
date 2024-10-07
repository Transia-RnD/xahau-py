from unittest import TestCase

from xahau.core.binarycodec import XAHLBinaryCodecException
from xahau.core.binarycodec.types.blob import Blob


class TestBlob(TestCase):
    def test_from_value(self):
        value = "00AA"
        value_bytes = bytes.fromhex(value)

        blob1 = Blob.from_value(value)
        blob2 = Blob(value_bytes)

        self.assertEqual(blob1.buffer, blob2.buffer)

    def test_raises_invalid_value_type(self):
        invalid_value = [1, 2, 3]
        self.assertRaises(XAHLBinaryCodecException, Blob.from_value, invalid_value)
