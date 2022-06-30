from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max-limit.

db = SQLAlchemy(app)
# csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)