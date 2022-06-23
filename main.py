from flask import Flask, flash, request, redirect, render_template, session
import os
from werkzeug.utils import secure_filename
from equipamento import Equipamento


UPLOAD_FOLDER = '/Users/RALDS/Documents/GitHub/ListaDeMateriais'
ALLOWED_EXTENSIONS = {'kml'}

app = Flask(__name__)
app.secret_key = 'ruma'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def anexar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
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
    if 'usuario_logado' not in session or session['usuario_logado'] == None or not os.path.exists(session['arquivo']):
        return redirect('/')
    arquivo = Equipamento(session['arquivo'])
    if os.path.exists(session['arquivo']):
        os.remove(session['arquivo'])
    return render_template('lista.html', equipamento=arquivo)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!!')
    return redirect('/login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        return redirect('/')
    else:
        flash('Senha incorreta!!')
        return redirect('/login')

app.run(port=5001,debug=True)
