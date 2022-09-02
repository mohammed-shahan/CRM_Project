from importlib import import_module
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from .database import db
from .config import Config

# import for creating test items, can be removed
from .models import Categories, Trainers, Courses


appsList = (
    'admin',
    'user',
    'auth',
    'api',
    'root',
)


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth_bp.login"
login_manager.login_message_category = "info"

migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    # Register Blueprints and routes, one route is also sufficient
    for module_name in appsList:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.bp)
    
    return app
