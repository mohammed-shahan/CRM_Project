from flask import render_template

from . import bp

@bp.route('/')
def dashboard():
    return render_template('user/pages/dashboard.html')

@bp.route('/enquiries')
def enquiries():
    return render_template('user/pages/enquiries.html')

@bp.route('/courses')
def courses():
    return render_template('user/pages/courses.html')

@bp.route('/profile')
def profile_get():
    return render_template('user/base.html')
    # return render_template('user/pages/profile.html')