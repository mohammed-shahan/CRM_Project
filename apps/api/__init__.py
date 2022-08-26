from flask import Blueprint

# Blueprint Configuration
bp = Blueprint(
    'api_bp', __name__,
    url_prefix='/api'
)