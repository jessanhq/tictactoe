
import board
import player
# 3rd party libs
from flask import Flask, request, abort

app = Flask(__name__)

BOARD_PARAM = 'board'


@app.route('/')
def TicTacToe():
    # TODO: Pass along error message to requestor.
    if BOARD_PARAM not in request.args:
        abort(400)
    try:
        current_board = board.FromString(request.args.get(BOARD_PARAM)
    except board.InvalidBoard:
        abort(400)
    try:
        return player.Player(player.LETTER_O).Play(current_board)
    except player.NotMyTurn:
        abort(400)
