# from werkzeug.utils import secure_filename
import time

from flask import flash, request, redirect, render_template, session, url_for
from flask_bcrypt import check_password_hash, generate_password_hash

from app import app, db
from helpers import FileForm, UsuariosForm
from models import Usuarios
import processing

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
        list_ex = request.form.getlist('project')
        print(list_ex)
        project = processing.load_file(file)  # load project
        pole = project.data_pole()  # load pole
        style = project.data_style()  # load style
        element = project.element('REDE FTTH')  # list Main project
        processing.osnap(value=element[1], pole=pole)  # osnap point
        processing.tp(value=element[1], style=style)  # type point
        processing.osnap(value=element[0], pole=pole)  # osnap fiber
        user_main = processing.pole_user(pole)
        if 'Expansion' in list_ex:
            element_ex = project.element('EXPANSION')  # list Expansion project
            processing.osnap(value=element_ex[1], pole=pole)  # osnap point
            processing.tp(value=element_ex[1], style=style)  # type point
            processing.osnap(value=element_ex[0], pole=pole)  # osnap fiber
            return render_template('lista_ex.html',
                                   project=project.name,
                                   # list Launch
                                   fiber=processing.list_fiber(element_ex[0]),
                                   strap=processing.list_strap(element_ex[0]),
                                   tie=processing.list_tie(element_ex[0]),
                                   user_fusion=processing.pole_user(pole) - user_main,
                                   sco=len(processing.list_sco(element_ex[0])),
                                   platelet_launch=processing.platelet_launch(element_ex[0]),
                                   wire_launch=processing.wire_la(element_ex[0]),
                                   rt=processing.rt(element_ex[1]),
                                   # list Fusion
                                   box=processing.box(element_ex[1]),

                                   bandeja_presley=processing.tray_presley(element_ex[1]),
                                   spliter=processing.spliter(element_ex[1]),
                                   bap_fusion=processing.bap_fusion(element_ex[1]),
                                   platelet_fusion=processing.platelet_fusion(element_ex[0]),
                                   wire_fusion=processing.wire_fus(element_ex[0]),
                                   prensa_fiber=processing.prensa_fiber(element_ex[1]),
                                   tube_45=processing.tube_45(element_ex),
                                   tube_60=processing.tube_60(element_ex)
                                   )
        elif 'Full' in list_ex:
            element_ex = project.element('EXPANSION')  # list Expansion project
            processing.osnap(value=element_ex[1], pole=pole)  # osnap point
            processing.tp(value=element_ex[1], style=style)  # type point
            processing.osnap(value=element_ex[0], pole=pole)  # osnap fiber
            return render_template('lista_full.html',
                                   project=project.name,
                                   # list Launch
                                   fiber=processing.list_fiber(element[0]),
                                   strap=processing.list_strap(element[0]),
                                   tie=processing.list_tie(element[0]),
                                   user_fusion=user_main,
                                   sco=len(processing.list_sco(element[0])),
                                   platelet_launch=processing.platelet_launch(element[0]),
                                   wire_launch=processing.wire_la(element[0]),
                                   rt=processing.rt(element[1]),

                                   fiber_ex=processing.list_fiber(element_ex[0]),
                                   strap_ex=processing.list_strap(element_ex[0]),
                                   tie_ex=processing.list_tie(element_ex[0]),
                                   user_fusion_ex=processing.pole_user(pole) - user_main,
                                   sco_ex=len(processing.list_sco(element_ex[0])),
                                   platelet_launch_ex=processing.platelet_launch(element_ex[0]),
                                   wire_launch_ex=processing.wire_la(element_ex[0]),
                                   rt_ex=processing.rt(element_ex[1]),
                                   # list Fusion
                                   box=processing.box(element[1]),
                                   bandeja_presley=processing.tray_presley(element[1]),
                                   spliter=processing.spliter(element[1]),
                                   bap_fusion=processing.bap_fusion(element[1]),
                                   platelet_fusion=processing.platelet_fusion(element[0]),
                                   wire_fusion=processing.wire_fus(element[0]),
                                   prensa_fiber=processing.prensa_fiber(element[1]),
                                   tube_45=processing.tube_45(element),
                                   tube_60=processing.tube_60(element),

                                   box_ex=processing.box(element_ex[1]),
                                   bandeja_presley_ex=processing.tray_presley(element_ex[1]),
                                   spliter_ex=processing.spliter(element_ex[1]),
                                   bap_fusion_ex=processing.bap_fusion(element_ex[1]),
                                   platelet_fusion_ex=processing.platelet_fusion(element_ex[0]),
                                   wire_fusion_ex=processing.wire_fus(element_ex[0]),
                                   prensa_fiber_ex=processing.prensa_fiber(element_ex[1]),
                                   tube_45_ex=processing.tube_45(element_ex),
                                   tube_60_ex=processing.tube_60(element_ex)
                                   )
        else:
            return render_template('lista.html',
                                   project=project.name,
                                   # list Launch
                                   fiber=processing.list_fiber(element[0]),
                                   strap=processing.list_strap(element[0]),
                                   tie=processing.list_tie(element[0]),
                                   user_fusion=user_main,
                                   sco=len(processing.list_sco(element[0])),
                                   platelet_launch=processing.platelet_launch(element[0]),
                                   wire_launch=processing.wire_la(element[0]),
                                   rt=processing.rt(element[1]),
                                   # list Fusion
                                   box=processing.box(element[1]),

                                   bandeja_presley=processing.tray_presley(element[1]),
                                   spliter=processing.spliter(element[1]),
                                   bap_fusion=processing.bap_fusion(element[1]),
                                   platelet_fusion=processing.platelet_fusion(element[0]),
                                   wire_fusion=processing.wire_fus(element[0]),
                                   prensa_fiber=processing.prensa_fiber(element[1]),
                                   tube_45=processing.tube_45(element),
                                   tube_60=processing.tube_60(element)
                                   )
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
