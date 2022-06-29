from flask import flash, request, redirect, render_template, session, url_for
from os import path, remove
from werkzeug.utils import secure_filename
from main import app, db
from models import Usuarios
from equipamento import Equipamento
from helpers import FileForm, UsuariosForm
from flask_bcrypt import check_password_hash, generate_password_hash



@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('index')))
    return redirect(url_for('anexar'))


@app.route('/novo_usuario')
def novo_usuario():
    proxima = request.args.get('proxima')
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = UsuariosForm()
    return render_template('novo_usuario.html', proxima=proxima, form=form)


@app.route('/criar_login', methods=['POST',])
def criar_login():
    form = UsuariosForm(request.form)
    nickname = form.nickname.data
    nome = form.nome.data
    senha = generate_password_hash(form.senha.data).decode('utf-8')

    nick = Usuarios.query.filter_by(nickname=nickname).first()
    if nick:
        flash('Login Existente!!')
        return redirect(url_for('login'))

    novo_login = Usuarios(nickname=nickname, nome=nome, senha=senha)
    db.session.add(novo_login)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/upload')
def anexar():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('anexar')))
    form = FileForm()
    return render_template('novo.html', form=form)


@app.route('/trata', methods=['POST',])
def upload_file():
    form = FileForm(request.files)
    if form.is_submitted():
        file = form.file.data
        filename = secure_filename(file.filename)
        local_file = app.config['UPLOAD_PATH']
        file.save(path.join(local_file,filename))
        session['arquivo'] = path.join(local_file,filename)
        return redirect(url_for('lista_material'))
    return redirect(url_for('index'))


@app.route('/lista')
def lista_material():
    if 'usuario_logado' not in session or session['usuario_logado'] is None or not path.exists(session['arquivo']):
        return redirect(url_for('anexar'))
    arquivo = Equipamento(session['arquivo'])
    if path.exists(session['arquivo']):
        remove(session['arquivo'])
    return render_template('lista.html', equipamento=arquivo)


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = UsuariosForm()
    return render_template('index.html', proxima=proxima, form=form)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!!')
    return redirect(url_for('login'))


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = UsuariosForm(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if 'None' in proxima_pagina:
            return redirect(url_for('index'))
        return redirect(proxima_pagina)
    else:
        flash('login ou senha incorreta!!')
        return redirect(url_for('login'))
