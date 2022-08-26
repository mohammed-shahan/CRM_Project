from flask import Flask
from .database import db
from importlib import import_module

from .config import Config

# import for creating test items, can be removed
# from .models import Categories, Trainers, Courses


appsList = (
    'admin',
    'user',
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
    pass
#     with flask_app.app_context():
#         db.create_all()

#         db.session.add(Categories('Web'))
#         db.session.add(Categories('Mobile'))
#         db.session.add(Trainers('Abhilash'))
#         db.session.add(Courses('flask', 'python flask', 4, 1, 1))
#         db.session.commit()

