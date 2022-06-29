from os.path import dirname,abspath, join

UPLOAD_PATH = join(dirname(abspath(__file__)), "uploads")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'ruma'


SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='postgresql',
        usuario='ralds',
        senha='admin',
        servidor='localhost',
        database='eng'
    )
