from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Substitua por uma chave secreta segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Use o SQLite para simplificar

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)  # Adicionando a coluna 'completed'
    user_id = db.Column(db.String(80), db.ForeignKey('user.id'))

db.create_all()

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(id=session['username']).first()
    notes = Note.query.filter_by(user_id=session['username']).all()
    return render_template('index.html', notes=notes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifique se o usuário já existe
        existing_user = User.query.filter_by(id=username).first()
        if existing_user:
            return "O nome de usuário já está em uso. Escolha outro nome de usuário."

        # Crie um novo usuário
        new_user = User(id=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirecione o usuário para a página de login após o registro
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        task_content = request.form['task']
        user_id = session['username']
        task = Note(content=task_content, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('view_tasks'))

    return render_template('view_tasks.html')

@app.route('/view_tasks')
def view_tasks():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    user = User.query.filter_by(id=session['username']).first()
    tasks = Note.query.filter_by(user_id=session['username']).all()
    return render_template('view_tasks.html', tasks=tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(id=username, password=password).first()

        if user:
            session['username'] = username
            return redirect(url_for('view_tasks'))
    print("nao achou")
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')