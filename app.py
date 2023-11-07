import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_pyfile('production_config.py')
else:
    app.config.from_pyfile('development_config.py')

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max-limit.

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
