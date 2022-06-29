from os.path import dirname,abspath, join

UPLOAD_PATH = join(dirname(abspath(__file__)), "uploads")
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'ruma'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='postgresql',
        usuario='gtxmgfpnwqemej',
        senha='0a3ade179595158f9d6c9440ed155a467b361e197146ac6af303b234085d1518',
        servidor='ec2-44-195-162-77.compute-1.amazonaws.com',
        database='dckbnake75kr9r'
    )
