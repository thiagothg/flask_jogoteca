from flask import Flask, render_template
from jogos import Jogo

app = Flask(__name__)

@app.route('/')

def hello():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Combat', 'Flight', 'PS2')

    list = [jogo1, jogo2, jogo3]
    return render_template('list.html', titulo='Jogos', jogos=list)



app.run(debug=True)