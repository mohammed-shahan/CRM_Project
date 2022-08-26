from flask import redirect, url_for, render_template

from . import bp


@bp.route('/')
def index():
    return redirect(url_for('auth_bp.login'))


@bp.route('/login')
def login():
    return render_template('auth/pages/login.html')


@bp.route('/register')
def register():
    return render_template('auth/pages/register.html')