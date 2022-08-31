from flask_login import UserMixin
import datetime
from .database import db


class Categories(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), unique=True)

    courses  = db.relationship('Courses')

    def __init__(self, category) -> None:
        self.category = category


class Trainers(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(20))
    email   = db.Column(db.String(20))
    phone   = db.Column(db.String(13))

    courses = db.relationship('Courses')

    def __init__(self, name, email, phone) -> None:
        self.name  = name
        self.email = email
        self.phone = phone


class Courses(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(50))
    durationWeeks = db.Column(db.Integer)
    description   = db.Column(db.String(100))
    rating        = db.Column(db.Float)
    comment       = db.Column(db.String(100))
    
    category      = db.Column(db.Integer, db.ForeignKey('categories.id'))
    trainer       = db.Column(db.Integer, db.ForeignKey('trainers.id'))

    batches       = db.relationship('Batches')
    reviews       = db.relationship('Reviews')
    enrollments   = db.relationship("Enrollments")
    enquiries     = db.relationship("Enquiries")

    def __init__(self, name, description, durationWeeks, category, trainer) -> None:
        self.name           = name
        self.description    = description
        self.durationWeeks  = durationWeeks
        self.category       = category
        self.trainer        = trainer


class Roles(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    role    = db.Column(db.String(20), unique=True)

    users   = db.relationship('Users')

    def __init__(self, role) -> None:
        self.role = role



class Qualifications(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.String(20), unique=True)
    status        = db.Column(db.Boolean)

    users         = db.relationship('UserQualifications')
    courses       = db.relationship('CourseQualifications')

    def __init__(self, qualification) -> None:
        self.qualification = qualification
        self.status        = True


class UserQualifications(db.Model):
    id            = db.Column(db.Integer, primary_key = True)
    user          = db.Column(db.Integer, db.ForeignKey('users.id'))
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))

        
class Users(db.Model, UserMixin):
    id          = db.Column(db.Integer, primary_key=True)
    firstName   = db.Column(db.String(20), nullable=False)
    lastName    = db.Column(db.String(20), nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(300), nullable=False, unique=True)

    role        = db.Column(db.Integer, db.ForeignKey('roles.id'))

    qualifications = db.relationship('UserQualifications')
    logs        = db.relationship('UserLogs')
    reviews     = db.relationship("Reviews")
    enrollments = db.relationship("Enrollments")
    enquiries   = db.relationship("Enquiries")

    def __init__(self, firstName, lastName, password, email, role) -> None:
        self.firstName  = firstName
        self.lastName   = lastName
        self.password   = password
        self.email      = email
        self.role       = role


class UserLogs(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user) -> None:
        self.user = user


class CourseQualifications(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    course        = db.Column(db.Integer, db.ForeignKey('courses.id'))
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))

    def __init__(self, course, qualification) -> None:
        self.course        = course
        self.qualification = qualification


class Batches(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    size   = db.Column(db.Integer)
    status = db.Column(db.Integer,)

    course = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, size, status, course) -> None:
        self.size   = size
        self.status = status
        self.course = course


class Reviews(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    rating      = db.Column(db.Integer)

    user        = db.Column(db.Integer, db.ForeignKey("users.id"))
    course      = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, description, rating, user, course) -> None:
        self.description = description
        self.rating      = rating
        self.user        = user
        self.course      = course


class Enrollments(db.Model):
    id      = db.Column(db.Integer, primary_key=True)

    user    = db.Column(db.Integer, db.ForeignKey("users.id"))
    course  = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, user, course) -> None:
        self.user   = user
        self.course = course


class Enquiries(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    status      = db.Column(db.Boolean)
    
    user        = db.Column(db.Integer, db.ForeignKey("users.id"))
    course      = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, description, status, user, course) -> None:
        self.description = description
        self.status      = status
        self.user        = user
        self.course      = course
