from crypt import methods
from flask import Flask, redirect, render_template, request
from jogos import Jogo

app = Flask(__name__)

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combat', 'Flight', 'PS2')

list = [jogo1, jogo2, jogo3]

@app.route('/')
def hello():
    return render_template('list.html', titulo='Jogos', jogos=list)

@app.route('/new')
def new():
    return render_template('new.html', titulo='Novo')

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    
    jogo = Jogo(name, category, console)
    
    list.append(jogo)
    return redirect('/')
    

app.run(debug=True)