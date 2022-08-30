from flask import redirect, url_for, render_template, jsonify, abort, request

from . import bp
from apps.models import Categories
from apps.database import db

@bp.route('/categories/<int:id>', methods=['DELETE'])
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