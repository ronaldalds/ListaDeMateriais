import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'ruma')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///database.db')
