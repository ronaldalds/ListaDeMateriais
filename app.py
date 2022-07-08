from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# from helpers import FileForm

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max-limit.

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

# @app.route('/')
# def index():
#     if 'usuario_logado' not in session or session['usuario_logado'] == None:
#         return redirect(url_for('login', proxima=url_for('index')))
#     return redirect(url_for('anexar'))
#
# @app.route('/upload')
# def anexar():
#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return redirect(url_for('login', proxima=url_for('anexar')))
#     form = FileForm()
#     return render_template('novo.html', form=form)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
