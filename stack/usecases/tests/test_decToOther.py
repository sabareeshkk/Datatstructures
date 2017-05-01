import unittest
from ..decToOther import decToOther


class DecToBinTest(unittest.TestCase):

    def setUp(self):
        self.binary = decToOther(233, 2).show()
        self.octal = decToOther(25, 8).show()
        self.hex = decToOther(25, 16).show()

    def test_checkBinary(self):
        self.binary.reverse()
        binaryString = ''.join(self.binary)
        return self.assertEqual(binaryString, '11101001')

    def test_octal(self):
        self.octal.reverse()
        octalString = ''.join(self.octal)
        return self.assertEqual(octalString, '31')

    def test_hex(self):
        self.hex.reverse()
        hexString = ''.join(self.hex)
        return self.assertEqual(hexString, '19')


if __name__ == "__main__":
    unittest.main()
