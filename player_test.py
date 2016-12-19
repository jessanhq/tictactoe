import unittest

import board
from player import *


EMPTY_BOARD = board.FromString('         ')
class PlayerTest(unittest.TestCase):

    def testPlay_empty(self):
        Player(LETTER_O).Play(EMPTY_BOARD)
        Player(LETTER_X).Play(EMPTY_BOARD)

    def testPlay_NotOTurn(self):
        with self.assertRaises(NotMyTurn):
            Player(LETTER_O).Play(board.FromString('o        '))

    def testPlay_NotXTurn(self):
        with self.assertRaises(NotMyTurn):
            Player(LETTER_X).Play(board.FromString('x        '))

    def testPlay_GameOver(self):
        with self.assertRaises(NotMyTurn):
            Player(LETTER_X).Play(board.FromString('xxxoo    '))
if __name__ == "__main__":
    unittest.main(exit=False)
