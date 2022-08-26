from os import path
from flask import Blueprint, render_template

# Blueprint Configuration
bp = Blueprint(
    'admin_bp', __name__,
    static_folder='static',
    url_prefix='/admin'
)


@bp.route('/', methods=['GET'])
def dashboard():
    return render_template('admin/pages/dashboard.html')


@bp.route('/qualifications', methods=['GET'])
def qualifications():
    return render_template('admin/pages/qualifications.html')


@bp.route('/batches')
def batches():
    return render_template('admin/pages/batches.html')


@bp.route('/categories')
def categories():
    return render_template('admin/pages/categories.html')


@bp.route('/courses')
def courses():
    return render_template('admin/pages/courses.html')
