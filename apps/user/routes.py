from flask import render_template, request
from flask_login import login_required, current_user

from . import bp
from apps.auth.utils import user_required
from apps.models import Trainers, Qualifications, Courses, Categories, Enquiries, Users

@bp.route('/')
@login_required
@user_required
def dashboard():
    return render_template('user/pages/dashboard.html', user=current_user,)

@bp.route('/enquiries', methods=['GET'])
@login_required
@user_required
def enquiries_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    users = {}
    for user in Users.query.all():
        users[user.id] = user.email
    courses = {}
    for course in Courses.query.all():
        courses[course.id] = course.name
    if search != '':
        search = f'%{search}%'
        _courses = Courses.query.filter(Courses.name.like(search))
        for course in _courses:
            enquiries = Enquiries.query.filter(Enquiries.course == course.id).paginate(page=page, per_page=rowsPerPage)
            courses = Enquiries.query.filter(Enquiries.course.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        for user in users:
            enquiries = Enquiries.query.filter_by(user=current_user.id)
            enquiries = Enquiries.query.order_by(Enquiries.id.desc()).paginate(page=page, per_page=rowsPerPage)
            if enquiries.pages:
                break
    return render_template('user/pages/enquiries.html', user=current_user, enquiries=enquiries, users=users, courses=courses,)

@bp.route('/courses')
@login_required
@user_required
def courses_get():
    trainers = {}
    qualifications = {}
    categories = {}
    for t in Trainers.query.all():
        trainers[t.id] = t.name
    for q in Qualifications.query.all():
        qualifications[q.id] = {'name': q.qualification, 'status': q.status}
    for c in Categories.query.all():
        categories[c.id] = c.category
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search != '':
        search = f'%{search}%'
        courses = Courses.query.filter(Courses.name.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        courses = Courses.query.order_by(Courses.id.desc()).paginate(page=page, per_page=rowsPerPage)
    return render_template(
        'user/pages/courses.html',
        user=current_user,
        courses=courses,
        trainers=trainers,
        categories=categories,
        qualifications=qualifications
    )

@bp.route('/profile')
@login_required
@user_required
def profile_get():
    return render_template('user/base.html', user=current_user,)
    # return render_template('user/pages/profile.html')