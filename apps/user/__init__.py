from flask import Blueprint

# Blueprint Configuration
bp = Blueprint(
    'user_bp', __name__,
    static_folder='static',
    url_prefix='/user'
)