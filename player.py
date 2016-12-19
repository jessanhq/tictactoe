
LETTER_X = 'x'
LETTER_O = 'o'


class NotMyTurn(Exception):
    pass


class Player(object):
    def __init__(self, letter):
        self.letter = letter

    def Play(self, board):
        """Takes a Board and makes a valid move."""
        if self.letter not in board.WhoseTurn():
            raise NotMyTurn()
        return board
