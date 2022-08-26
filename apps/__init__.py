from flask import Flask
from .database import db
from importlib import import_module

from .config import Config

# import for creating test items, can be removed
from .models import Users, InternalUse


appsList = (
    'admin',
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # flask initializes Alchemy with the application
    db. init_app(app)
    # Register Blueprints and routes, one route is also sufficient
    for module_name in appsList:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.bp)
    
    return app


def setup_database(flask_app):
    with flask_app.app_context():
        # alchemy creates the db from SQLALCHEMY_DATABASE_URI and models.py classes
        db.create_all()

        # only for test items, can be removed
        db.session.add(InternalUse(browser_open=1, statistics='98.6', commercials='sold'))
        db.session.add(InternalUse(browser_open=0, statistics=70.2, commercials='bid'))
        db.session.add(Users(username='pi', email='pi@pipapo.org', profile='ceo'))
        db.session.add(Users(username='pa', email='pa@pipapo.org', profile='chief'))
        db.session.add(Users(username='po', email='po@pipapo.org', profile='leader'))
        db.session.commit()

