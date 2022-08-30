from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from . import bp
from apps.models import Categories
from apps.database import db
from apps.auth.utils import admin_required


@bp.route('/', methods=['GET'])
@login_required
@admin_required
def dashboard():
    return render_template('admin/pages/dashboard.html')


@bp.route('/qualifications', methods=['GET'])
@login_required
@admin_required
def qualifications():
    return render_template('admin/pages/qualifications.html')

@bp.route('/batches')
@login_required
@admin_required
def batches():
    print(current_user)
    return render_template('admin/pages/batches.html')



@bp.route('/categories', methods=['GET'])
@login_required
@admin_required
def categories_get():
    return render_template('admin/pages/categories.html', categories=Categories.query.all())


@bp.route("/categories", methods=['POST'])
@login_required
@admin_required
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
@login_required
@admin_required
def courses():
    return render_template('admin/pages/courses.html')
