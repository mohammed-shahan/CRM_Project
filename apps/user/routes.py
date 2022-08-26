from os import path
from flask import Blueprint, render_template

# Blueprint Configuration
bp = Blueprint(
    'user_bp', __name__,
    static_folder='static',
    url_prefix='/user'
)


@bp.route('/courses')
def courses():
    return render_template('user/pages/courses.html')
