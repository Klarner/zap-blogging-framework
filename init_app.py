from flask import Flask
from model import db, ma
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SITE_NAME'] = 'ZAP Blogging Framework'
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=15)
    db.init_app(app=app)
    ma.init_app(app=app)
    return app
