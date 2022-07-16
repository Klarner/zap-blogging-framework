from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(250))
    name = db.Column(db.String(250))
    email = db.Column(db.String(150))
    roleName = db.Column(db.String(150))
    roleIndexPosition = db.Column(db.Integer)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    author = db.Column(db.String(250), db.ForeignKey('users.name'))
    link = db.Column(db.String(250))
    content = db.Column(db.Text)
    summary = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)
    tags = db.Column(db.PickleType())
    categories = db.Column(db.PickleType())

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_fk = True

class ArticlesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Articles
        include_fk = True

userSchema = UsersSchema()
articleSchema = ArticlesSchema()
