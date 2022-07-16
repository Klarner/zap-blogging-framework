from model import Users, db

def addUser(username, password, name, email, roleName, roleIndexPosition):
    user = Users(username=username, password=password, name=name, email=email, roleName=roleName, roleIndexPosition=roleIndexPosition)
    db.session.add(user)
    db.session.commit()

def removeUser(username):
    user = Users.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()