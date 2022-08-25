from os import path
from flask import Blueprint, render_template

# Blueprint Configuration
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
    url_prefix='/admin'
)


@admin_bp.route('/', methods=['GET'])
def dashboard():
    return render_template('pages/dash1.html')


@admin_bp.route('/qualifications', methods=['GET'])
def qualifications():
    return render_template('pages/qualificationlist.html')
