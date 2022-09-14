from flask import redirect, url_for, send_from_directory

from . import bp
from apps.config import Config
import os


@bp.route('/')
def index():
    return redirect(url_for('auth_bp.login'))


@bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(os.path.join(Config.basedir, Config.UPLOAD_FOLDER), name)