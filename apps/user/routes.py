from flask import render_template
from flask_login import login_required

from . import bp
from apps.auth.utils import user_required

@bp.route('/')
@login_required
@user_required
def dashboard():
    return render_template('user/pages/dashboard.html')

@bp.route('/enquiries')
@login_required
@user_required
def enquiries():
    return render_template('user/pages/enquiries.html')

@bp.route('/courses')
@login_required
@user_required
def courses():
    return render_template('user/pages/courses.html')

@bp.route('/profile')
@login_required
@user_required
def profile_get():
    return render_template('user/base.html')
    # return render_template('user/pages/profile.html')