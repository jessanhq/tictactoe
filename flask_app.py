from flask import Flask, request, abort

app = Flask(__name__)

BOARD_PARAM = 'board'

@app.route('/')
def Tictactoe():
    if BOARD_PARAM not in request.args:
      abort(400)
    board_str = request.args.get(BOARD_PARAM)
    return '        o'
