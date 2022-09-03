from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from . import bp
from apps.models import Categories, Qualifications, Trainers, Users, Batches, Roles, Courses, Enquiries, Enrollments
from apps.database import db
from apps.auth.utils import admin_required


@bp.route('/', methods=['GET'])
@login_required
@admin_required
def dashboard():
    return render_template('admin/pages/dashboard.html', user=current_user)


@bp.route('/qualifications', methods=['GET'])
@login_required
@admin_required
def qualifications_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search != '':
        search = f'%{search}%'
        qualifications = Qualifications.query.filter(Qualifications.qualification.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        qualifications = Qualifications.query.order_by(Qualifications.level.desc()).paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/qualifications.html', qualifications=qualifications, user=current_user)

@bp.route("/qualifications", methods=['POST'])
@login_required
@admin_required
def qualifications_post():
    # POST not working
    id = request.form.get('id')
    qName = request.form.get('qName')
    status = request.form.get('status') == 'true'
    level = request.form.get('level', type=int)
    print(id, qName, status, level)
    try:
        if id:
            q = Qualifications.query.filter_by(id=int(id)).first()
            setattr(q, 'qualification', qName)
            setattr(q, 'status', status)
            setattr(q, 'level', level)
            db.session.commit()
        else:
            db.session.add(Qualifications(qName, status, level))
            db.session.commit()
    except:
        flash('Failed to add Qualification')
        return redirect(url_for('admin_bp.qualifications_get'))
    else:
        flash('Qualification added successfully')
        return redirect(url_for('admin_bp.qualifications_get'))


@bp.route('/batches', methods=['GET'])
@login_required
@admin_required
def batches():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    batches = Batches.query.paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/batches.html', batches=batches, user=current_user)


@bp.route('/users', methods=['GET'])
@login_required
@admin_required
def users_get():
    roles = {}
    for role in Roles.query.all():
        roles[role.id] = role.role
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search != '':
        search = f'%{search}%'
        users = Users.query.filter(Users.email.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        users = Users.query.paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/users.html', users=users, user=current_user, roles=roles)

@bp.route("/users", methods=['POST'])
@login_required
@admin_required
def users_post():
    id = request.form.get('id')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    role = request.form.get('role')
    try:
            user = Users.query.filter_by(id=int(id)).first()
            setattr(user, 'firstName', firstName)
            setattr(user, 'lastName', lastName)
            setattr(user, 'email', email)
            setattr(user, 'role', role)
            db.session.commit()
    except:
        flash('Failed to add User')
        return redirect(url_for('admin_bp.users_get'))
    else:
        flash('User added successfully')
        return redirect(url_for('admin_bp.users_get'))


@bp.route('/categories', methods=['GET'])
@login_required
@admin_required
def categories_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search != '':
        search = f'%{search}%'
        categories = Categories.query.filter(Categories.category.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        categories = Categories.query.order_by(Categories.id.desc()).paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/categories.html', categories=categories, user=current_user)


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
        'admin/pages/courses.html',
        user=current_user,
        courses=courses,
        trainers=trainers,
        categories=categories,
        qualifications=qualifications
    )

@bp.route('/courses', methods=['POST'])
@login_required
@admin_required
def courses_post():
    id            = request.form.get('id', type=int)
    name          = request.form.get('name')
    videolink     = request.form.get('videolink')
    duration      = request.form.get('duration', type=int)
    qualification = request.form.get("qualification", type=int)
    status        = request.form.get("status") == 'true'
    category      = request.form.get("category", type=int)
    trainer       = request.form.get('trainer', type=int)
    description   = request.form.get("description", '')
    comment       = request.form.get('comment', '')

    try:
        if id:
            course = Courses.query.filter_by(id=id).first()
            setattr(course, 'name', name)
            setattr(course, 'durationWeeks', duration)
            setattr(course, 'description', description)
            setattr(course, 'comment', comment)
            setattr(course, 'videoLink', videolink)
            setattr(course, 'status', status)
            setattr(course, "category", category)
            setattr(course, "trainer", trainer)
            setattr(course, "qualification", qualification)
            db.session.commit()
        else:
            db.session.add(Courses(
                name,
                description,
                duration,
                category,
                trainer,
                videolink,
                comment,
                qualification,
                status
            ))
            db.session.commit()
    except:
        flash('Failed to add Course')
        return redirect(url_for('admin_bp.courses_get'))
    else:
        flash('Course added successfully')
        return redirect(url_for('admin_bp.courses_get'))


@bp.route('/enquiries', methods=['GET'])
@login_required
@admin_required
def enquiries_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    enquiries = Enquiries.query.paginate(page=page, per_page=rowsPerPage)
    search = request.args.get('search', '')
    users = {}
    for user in Users.query.all():
        users[user.id] = user.email
    courses = {}
    for course in Courses.query.all():
        courses[course.id] = course.name
    if search != '':
        search = f'%{search}%'
        _users = Users.query.filter(Users.email.like(search))
        for user in _users:
            enquiries = Enquiries.query.filter(Enquiries.user == user.id).paginate(page=page, per_page=rowsPerPage)
            if enquiries.pages:
                break
    else:
        enquiries = Enquiries.query.paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/enquiries.html', user=current_user, enquiries=enquiries, users=users, courses=courses)

@bp.route("/enquiries", methods=['POST'])
@login_required
@admin_required
def enquiries_post():
    id = request.form.get('id')
    user_id = request.form.get('user_id')
    course_id = request.form.get('course_id')
    user = request.form.get('user')
    course = request.form.get('course')
    description = request.form.get('description')
    status = request.form.get('status')
    stat = "true" == status
    try:
        enquiry = Enquiries.query.filter_by(id=int(id)).first()
        if stat:
            setattr(enquiry, 'status', stat)
            db.session.add(Enrollments(user_id,course_id))
        db.session.commit()
    except:
        flash('Failed to add Enquiry')
        return redirect(url_for('admin_bp.enquiries_get'))
    else:
        flash('Enquiry added successfully')
        return redirect(url_for('admin_bp.enquiries_get'))


@bp.route('/trainers', methods=['GET'])
@login_required
@admin_required
def trainers_get():
    rowsPerPage = request.args.get('rows', 10, type=int)
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    if search != '':
        search = f'%{search}%'
        ts = Trainers.query.filter(Trainers.email.like(search)).paginate(page=page, per_page=rowsPerPage)
    else:
        ts = Trainers.query.order_by(Trainers.id.desc()).paginate(page=page, per_page=rowsPerPage)
    return render_template('admin/pages/trainers.html', trainers=ts, user=current_user)

@bp.route("/trainers", methods=['POST'])
@login_required
@admin_required
def trainers_post():
    id = request.form.get('id', type=int)
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    try:
        if id:
            t = Trainers.query.filter_by(id=id).first()
            setattr(t, 'name', name)
            setattr(t, 'email', email)
            setattr(t, 'phone', phone)
        else:
            db.session.add(Trainers(name, email, phone))
        db.session.commit()
    except Exception as e:
        print(e)
        flash('Failed to add Trainer')
        return redirect(url_for('admin_bp.trainers_get'))
    else:
        flash('Trainer added successfully')
        return redirect(url_for('admin_bp.trainers_get'))