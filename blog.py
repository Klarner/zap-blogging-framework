from flask import Flask
from flask_jwt import JWT
from model import db, Users
from public import public
from private import private
from init_app import create_app
from manage_accounts import addUser, removeUser

app = create_app()
app.register_blueprint(public, url_prefix='/')
app.register_blueprint(private, url_prefix='/manage/')
app.app_context().push()

def authenticate(username, password):
    user = Users.query.filter_by(username=username).first()
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return Users.query.filter_by(id=user_id).first()

jwt = JWT(app, authenticate, identity)

if __name__ == '__main__':
    # addUser("test2", "test2", "testauthor2", "test@test.com", "Editor", 0)
    app.run(port=8000)
