from flask import render_template

from . import bp


@bp.route('/courses')
def courses():
    return render_template('user/pages/courses.html')
