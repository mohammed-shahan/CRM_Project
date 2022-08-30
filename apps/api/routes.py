from flask import redirect, url_for, render_template, jsonify, abort, request
from flask_login import login_required

from . import bp
from apps.models import Categories, Qualifications
from apps.database import db
from apps.auth.utils import admin_required

@bp.route('/categories/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def categories_delete(id):
    try:
        cat = Categories.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if cat.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)


@bp.route('/qualifications/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def qualifications_delete(id):
    try:
        q = Qualifications.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if q.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)