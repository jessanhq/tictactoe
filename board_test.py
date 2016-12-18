import unittest
from board import *


class HelperTest(unittest.TestCase):
    def test_emptyString(self):
        with self.assertRaises(InvalidBoard):
            FromString('')

    def test_none(self):
        with self.assertRaises(InvalidBoard):
            FromString(None)

    def test_invalidChar(self):
        with self.assertRaises(InvalidBoard):
            FromString('        q')

    def test_tooManyX(self):
        with self.assertRaises(InvalidBoard):
            FromString('       xx')

    def test_tooManyO(self):
        with self.assertRaises(InvalidBoard):
            FromString('       oo')

    def test_tooLong(self):
        with self.assertRaises(InvalidBoard):
            FromString('       xox')

    def test_tooLongEmpty(self):
        with self.assertRaises(InvalidBoard):
            FromString('          ')

    def test_basic(self):
        self.assertEquals('        x', str(FromString('        x')))

    def test_emptyBoard(self):
        self.assertEquals('         ', str(FromString('         ')))

    def test_notMyTurn(self):
        with self.assertRaises(NotMyTurn):
            FromString('o        ')

if __name__ == "__main__":
    unittest.main(exit=False)
