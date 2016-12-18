from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def Tictactoe():
    if request.args.get('fail'):
      abort(400)
    return '        O'
