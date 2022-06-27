from flask import flash, request, redirect, render_template, session, url_for
from os import path, remove
from werkzeug.utils import secure_filename
from lista_de_materiais import app
from models import Usuarios
from equipamento import Equipamento
from helpers import FileForm


@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('index')))
    return redirect(url_for('anexar'))


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
    return render_template('login.html', proxima=proxima)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!!!')
    return redirect(url_for('login'))


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = request.form['usuario']
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            if 'None' in proxima_pagina:
                return redirect(url_for('index'))
            return redirect(proxima_pagina)
        else:
            flash('senha incorreta!!')
            return redirect(url_for('login'))
    else:
        flash('log incorreta!!')
        return redirect(url_for('login'))
