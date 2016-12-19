import unittest
from board import *


class BoardTest(unittest.TestCase):
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

    def testWhoseTurn_X(self):
        x_turn_board = FromString('o        ')
        self.assertEquals({'x'}, x_turn_board.WhoseTurn())

    def testWhoseTurn_O(self):
        o_turn_board = FromString('  xox    ')
        self.assertEquals({'o'}, o_turn_board.WhoseTurn())

    def testWhoseTurn_Empty(self):
        either_turn_board = FromString('         ')
        self.assertEquals({'o', 'x'}, either_turn_board.WhoseTurn())

    def testWhoseTurn_Either(self):
        either_turn_board = FromString('xo       ')
        self.assertEquals({'o', 'x'}, either_turn_board.WhoseTurn())

    def testWhoseTurn_GameOver(self):
        finished_board = FromString('xoxoxoxox')
        self.assertEquals({}, finished_board.WhoseTurn())

if __name__ == "__main__":
    unittest.main(exit=False)
