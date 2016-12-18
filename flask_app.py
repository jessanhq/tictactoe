
import board

# 3rd party libs
from flask import Flask, request, abort

app = Flask(__name__)

BOARD_PARAM = 'board'


@app.route('/')
def TicTacToe():
    if BOARD_PARAM not in request.args:
      abort(400)
    return board.FromString(request.args.get(BOARD_PARAM))
