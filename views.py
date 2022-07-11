# from werkzeug.utils import secure_filename
import time

from flask import flash, request, redirect, render_template, session, url_for
from flask_bcrypt import check_password_hash, generate_password_hash

from app import app, db
from helpers import FileForm, UsuariosForm
from models import Usuarios
from processing import load_file, osnap, tp, list_fiber, list_strap, list_tie, list_sco, pole_user, platelet_launch, \
    wire_la


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('index')))
    return redirect(url_for('anexar'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = UsuariosForm()
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/novo_usuario')
def novo_usuario():
    proxima = request.args.get('proxima')
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = UsuariosForm()
    return render_template('novo_usuario.html', proxima=proxima, form=form)


@app.route('/criar_login', methods=['POST', ])
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


@app.route('/trata', methods=['GET', 'POST'])
def upload_file():
    form = FileForm(request.files)
    if form.is_submitted():
        file = form.file.data
        a = time.time()
        project = load_file(file)  # load project
        pole = project.data_pole()  # load pole
        style = project.data_style()  # load style
        element = project.element('REDE FTTH')  # list Main project
        osnap(value=element[1], pole=pole)  # osnap point
        tp(value=element[1], style=style)  # type point
        osnap(value=element[0], pole=pole)  # osnap fiber



        b = time.time()
        return render_template('lista.html',
                               fiber=list_fiber(element[0]),
                               strap=list_strap(element[0]),
                               tie=list_tie(element[0]),
                               user_fusion=pole_user(pole),
                               sco=len(list_sco(element[0])),
                               platelet_launch=platelet_launch(element[0]),
                               wire_launch=wire_la(element[0]))
    return redirect(url_for('index'))


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
