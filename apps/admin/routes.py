from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from . import bp
from apps.models import Categories, Qualifications
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
def qualifications_get():
    return render_template('admin/pages/qualifications.html', qualifications=Qualifications.query.all())

@bp.route("/qualifications", methods=['POST'])
@login_required
@admin_required
def qualifications_post():
    id = request.form.get('id')
    qName = request.form.get('qName')
    try:
        if id:
            q = Qualifications.query.filter_by(id=int(id)).first()
            setattr(q, 'qualification', qName)
            db.session.commit()
        else:
            db.session.add(Qualifications(qName))
            db.session.commit()
    except:
        flash('Failed to add Qualification')
        return redirect(url_for('admin_bp.qualifications_get'))
    else:
        flash('Qualification added successfully')
        return redirect(url_for('admin_bp.qualifications_get'))


@bp.route('/batches')
@login_required
@admin_required
def batches():
    return render_template('admin/pages/batches.html')

@bp.route('/users')
@login_required
@admin_required
def users():
    return render_template('admin/pages/users.html')

@bp.route('/categories', methods=['GET'])
@login_required
@admin_required
def categories_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    categories = Categories.query.paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/categories.html', categories=categories)


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
