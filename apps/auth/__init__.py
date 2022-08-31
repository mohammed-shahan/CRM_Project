from flask import Blueprint

# Blueprint Configuration
bp = Blueprint(
    'auth_bp', __name__,
    url_prefix='/auth'
)