from flask import Blueprint

# Blueprint Configuration
bp = Blueprint(
    'root_bp', __name__,
    static_folder='static',
    url_prefix='/'
)