from flask import Flask, flash, request, redirect, render_template, session, url_for
import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from equipamento import Equipamento

UPLOAD_FOLDER = '/Users/RALDS/Documents/GitHub/ListaDeMateriais'
ALLOWED_EXTENSIONS = {'kml'}

app = Flask(__name__)
app.secret_key = 'ruma'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='eng'
    )

db = SQLAlchemy(app)

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def anexar():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login?proxima=')
    return render_template('novo.html')


@app.route('/trata', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['arquivo'] = filename
            return redirect('/lista')
    return ''


@app.route('/lista')
def lista_material():
    if 'usuario_logado' not in session or session['usuario_logado'] is None or not os.path.exists(session['arquivo']):
        return redirect('/')
    arquivo = Equipamento(session['arquivo'])
    if os.path.exists(session['arquivo']):
        os.remove(session['arquivo'])
    return render_template('lista.html', equipamento=arquivo)


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/logout', methods=['POST', ])
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!!')
    return redirect('/login')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = request.form['usuario']
            flash(usuario.nickname + ' logado com sucesso!')
            return redirect('/')
    else:
        flash('Senha incorreta!!')
        return redirect('/login')


app.run(debug=True)
