from flask import redirect, url_for, render_template, jsonify, abort, request
from flask_login import login_required, current_user

from . import bp
from apps.models import Categories, Qualifications, Users, Roles, Enquiries, Courses, Trainers
from apps.database import db
from apps.auth.utils import admin_required, user_required


@bp.route('/categories/<int:id>', methods=['GET'])
def categories_get(id):
    cat = Categories.query.filter_by(id=id).first()
    if cat:
        return jsonify({'category': {
            'id': id,
            'category': cat.category
        }}), 200
    else:
        abort(404)

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


@bp.route('/qualifications/<int:id>', methods=['GET'])
def qualifications_get(id):
    q = Qualifications.query.filter_by(id=id).first()
    if q:
        return jsonify({'qualification': {
            'id': id,
            'qualification': q.qualification,
            'level': q.level,
            'status': q.status,
        }}), 200
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



@bp.route('/users/<int:id>', methods=['GET'])
@login_required
@admin_required
def users_get(id):
    user = Users.query.filter_by(id=id).first()
    if user:
        return jsonify({'user': {
            'id': id,
            'firstname': user.firstName,
            'lastname': user.lastName,
            'email': user.email,
            'role': user.role
        }}), 200
    else:
        abort(404)

@bp.route('/users/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def users_delete(id):
    try:
        user = Users.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if user.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)


@bp.route('/roles', methods=['GET'])
@login_required
@admin_required
def roles_get():
    roles = []
    for role in Roles.query.all():
        roles.append({
            'id': role.id,
            'role': role.role
        })
    if roles:
        return jsonify({'roles': roles}), 200
    else:
        return jsonify({}), 204


        
@bp.route('/enquiries/<int:id>', methods=['GET'])
def enquiries_get(id):
    enq = Enquiries.query.filter_by(id=id).first()
    if enq:
        return jsonify({'enquiry': {
            'id': id,
            'status': enq.status,
            'user': enq.user,
            'course': enq.course
        }}), 200
    else:
        abort(404)

@bp.route('/enquiries/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def enquiries_delete(id):
    try:
        enq = Enquiries.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if enq.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)

@bp.route('/enquiries/<int:id>', methods=['POST'])
@login_required
@user_required
def enquiries_post(id):
    course = Courses.query.filter_by(id=id).first()
    if course:
        db.session.add(Enquiries(current_user.id, id))
        db.session.commit()
        return jsonify({'message': 'success'}), 200
    else:
        return jsonify({'error': 'course does not exist'})

        
@bp.route('/courses/<int:id>', methods=['GET'])
def courses_get(id):
    course = Courses.query.filter_by(id=id).first()
    if course:
        return jsonify({'course': {
            'id': id,
            'name': course.name,
            'duration': course.durationWeeks,
            'description': course.description,
            'rating': course.rating,
            'comment': course.comment,
            'videolink': course.videoLink,
            'status': course.status,
            'category': course.category,
            'trainer': course.trainer,
            'qualification': course.qualification
        }}), 200
    else:
        abort(404)

@bp.route('/courses/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def courses_delete(id):
    try:
        course = Courses.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if course.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)



@bp.route('/trainers/<int:id>', methods=['GET'])
def trainers_get(id):
    t = Trainers.query.filter_by(id=id).first()
    if t:
        return jsonify({'trainer': {
            'id': id,
            'name': t.name,
            'email': t.email,
            'phone': t.phone,
        }}), 200
    else:
        abort(404)

@bp.route('/trainers/<int:id>', methods=['DELETE'])
@login_required
@admin_required
def trainers_delete(id):
    try:
        t = Trainers.query.filter_by(id=id)
    except:
        abort(500)
    else:
        if t.delete() == 1:
            db.session.commit()
            return jsonify({}), 204
        else:
            abort(404)