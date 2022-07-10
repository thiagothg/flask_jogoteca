from flask import Flask, flash, redirect, render_template, request, session
from jogos import Jogo

app = Flask(__name__)
app.secret_key = 'alura'

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combat', 'Flight', 'PS2')

list = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('list.html', titulo='Jogos', jogos=list)
    # if session['userLoggedIn'] == True:
    # else:
    #     return redirect('/login')

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

@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')
    

@app.route('/autenticate', methods=['POST',])
def autenticate(): 
    if 'user' == request.form['user']:
        session['userLoggedIn'] = True
        flash('{} logon success'.format(request.form['user']))
        return redirect('/')
    else:
        flash('try again', category='error')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['userLoggedIn'] = False
    flash('User logout success!')
    return redirect('/')
    
app.run(debug=True)