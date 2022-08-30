from flask import render_template, request, flash, redirect, url_for

from . import bp
from apps.models import Categories
from apps.database import db

# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))

@bp.route('/', methods=['GET'])
def dashboard():
    return render_template('admin/pages/dashboard.html')


@bp.route('/qualifications', methods=['GET'])
def qualifications():
    return render_template('admin/pages/qualifications.html')


@bp.route('/batches')
def batches():
    return render_template('admin/pages/batches.html')


@bp.route('/categories', methods=['GET'])
def categories_get():
    return render_template('admin/pages/categories.html', categories=Categories.query.all())


@bp.route("/categories", methods=['POST'])
def categories_post():
    id = request.form.get('id')
    catName = request.form.get('catName')
    try:
        if id:
            cat = Categories.query.filter_by(id=int(id)).first()
            setattr(cat, 'category', catName)
            db.session.commit()
        else:
            db.session.add(Categories(catName))
            db.session.commit()
    except:
        flash('Failed to add Category')
        return redirect(url_for('admin_bp.categories_get'))
    else:
        flash('Category added successfully')
        return redirect(url_for('admin_bp.categories_get'))


@bp.route('/courses')
def courses():
    return render_template('admin/pages/courses.html')
