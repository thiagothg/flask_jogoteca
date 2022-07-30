from flask import Flask, flash, redirect, render_template, request, session, url_for
from jogos import Jogo
from user import User

app = Flask(__name__)
app.secret_key = 'alura'

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combat', 'Flight', 'PS2')

list = [jogo1, jogo2, jogo3]

user1 = User("Bruno Divino", "BD", "alohomora")
user2 = User("Camila Ferreira", "Mila", "paozinho")
user3 = User("Guilherme Louro", "Cake", "Python_eh_vida")

users = { user1.nickname : user1,
             user2.nickname : user2,
             user3.nickname : user3 }

@app.route('/')
def index():
    print(session)
    if 'user_logged' not in session or session['user_logged'] == None:
        redirect(url_for('login'))
    return render_template('list.html', titulo='Jogos', jogos=list)
    # if session['userLoggedIn'] == True:
    # else:
    #     return redirect('/login')

@app.route('/new')
def new():
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login'))
    return render_template('new.html', titulo='Novo')

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    
    jogo = Jogo(name, category, console)
    
    list.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    print(session)
    if 'user_logged' in session:
        return redirect(url_for('index'))
    next_page = request.args.get('next')
    return render_template('login.html', titulo='Login', next_page=next_page)
    

@app.route('/autenticate', methods=['POST',])
def autenticate(): 
    if request.form['user'] in users:
        user = users[request.form['user']]
        if request.form['password'] == user.password:
            session['user_logged'] = user.nickname
            flash(user.nickname + ' logado com sucesso!')
            next_page = request.form['next_page']
            print(next_page)
            return redirect(next_page)
        else:
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado.', category='error')
        return redirect(url_for('login'))
        
@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('User logout success!')
    return redirect(url_for('login'))
    
app.run(debug=True)