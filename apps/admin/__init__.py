from flask import Blueprint

# Blueprint Configuration
bp = Blueprint(
    'admin_bp', __name__,
    static_folder='static',
    url_prefix='/admin'
)