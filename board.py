
class InvalidBoard(Exception):
    pass


class InvalidMove(Exception):
    pass

_VALID_PLACE_CHARACTERS = frozenset({'x', ' ', 'o'})
_VICTORY_POSITIONS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
    (0, 4, 8), (2, 4, 6)  # Diagonal
    )

def FromString(board_str):
    if not board_str or len(board_str) != 9:
        raise InvalidBoard('Less than 9 places provided: %s' % board_str )

    return Board(board_str)


class Board(object):
    def __init__(self, board_str):
        self.board_str = board_str
        self.counts = self._CountBoard(self.board_str)

    def __str__(self):
        return self.board_str

    def _CountBoard(self, board_str):
        """Counts and validates the given board_str."""
        counts = {
            'o': 0,
            'x': 0,
            ' ': 0,
        }

        # Accept upper or lower case x/o.
        for place in board_str.lower():
            if place not in _VALID_PLACE_CHARACTERS:
                raise InvalidBoard('Invalid character: %s' % place)
            counts[place] += 1
        if abs(counts['o'] - counts['x']) > 1:
            raise InvalidBoard('Impossible state: %s' % board_str)
        return counts

    def GetOutcome(self):
        """Returns the outcome of the game.

        Returns the letter of the winner if there is a winner.
        Returns None if the game is not over. Returns DRAW if neither won.
        """

        for positions in _VICTORY_POSITIONS:
            # If a player captured all 3 of these, they won.
            if ((self.board_str[positions[0]] ==
                self.board_str[positions[1]] ==
                self.board_str[positions[2]]) and
                self.board_str[positions[0]] != ' '):
                return self.board_str[positions[0]]
        if self.counts[' '] == 0:
            return 'DRAW'
        return None  # No outcome yet.

    def WhoseTurn(self):
        """Returns the set of letters who could play."""
        if self.GetOutcome():
            return {}  # Game's over.
        move_diff = self.counts['o'] - self.counts['x']
        if move_diff == 0:
            return {'x', 'o'}
        elif move_diff < 0:
            return {'o'}
        else:
            return {'x'}

    def ValidMoves(self):
        """Yields valid positions."""
        for i in range(0, len(self.board_str)):
            if self.board_str[i] == ' ':
                yield i


    def MakeMove(self, pos, letter):
        """Returns a new board with the position filled with the letter."""
        if letter not in ('x', 'o'):
            raise InvalidMove('Invalid letter')
        if self.board_str[pos] != ' ':
            raise InvalidMove('Invalid position')
        mutable_board = list(self.board_str)
        mutable_board[pos] = letter
        return FromString(''.join(mutable_board))
