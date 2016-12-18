
class InvalidBoard(Exception):
    pass

class NotMyTurn(Exception):
    pass

VALID_PLACE_CHARACTERS = frozenset({'x', ' ', 'o'})


def FromString(board_str):
    if not board_str or len(board_str) != 9:
        raise InvalidBoard('Less than 9 places provided: %s' % board_str )
    counts = {
        'o': 0,
        'x': 0,
        ' ': 0,
    }

    # Accept upper or lower case x/o.
    for place in board_str.lower():
        if place not in VALID_PLACE_CHARACTERS:
            raise InvalidBoard('Invalid character: %s' % place)
        counts[place] += 1
    if abs(counts['o'] - counts['x']) > 1:
        raise InvalidBoard('Impossible state: %s' % board_str)
    if counts['o'] > counts['x']:
        raise NotMyTurn()
    return Board(board_str)


class Board(object):
    def __init__(self, board_str):
        self.board_str = board_str

    def __str__(self):
        return board_str
