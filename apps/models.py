from .database import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), unique=True)
    courses = db.relationship('Courses')

    def __init__(self, category) -> None:
        self.category = category


class Trainers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer = db.Column(db.String(20), unique=True)
    courses = db.relationship('Courses')

    def __init__(self, trainer) -> None:
        self.trainer = trainer


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    durationWeeks = db.Column(db.Integer)
    description = db.Column(db.String(100))
    
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    trainer = db.Column(db.Integer, db.ForeignKey('trainers.id'))

    def __init__(self, name, description, durationWeeks, category, trainer) -> None:
        self.name = name
        self.description = description
        self.durationWeeks = durationWeeks
        self.category = category
        self.trainer = trainer


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), unique=True)

    users = db.relationship('Users')

    def __init__(self, role) -> None:
        self.role = role



class Qualifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.String(20), unique=True)

    users = db.relationship('UserQualifications')

    def __init__(self, qualification) -> None:
        self.qualification = qualification

class UserQualifications(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))



        


        
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))

    role = db.Column(db.Integer, db.ForeignKey('roles.id'))

    qualifications = db.relationship('UserQualifications')

    def __init__(self, firstName, lastName, username, password, email, role) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.email = email
        self.role = role