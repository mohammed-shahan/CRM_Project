from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from apps import db
from flask_login import login_user, login_required, logout_user, current_user


from apps import login_manager
from . import bp
from apps.models import Users


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@bp.route('/')
def index():
    return redirect(url_for('auth_bp.login'))


#login route
@bp.route("/login/", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            print('hello')
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('admin_bp.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("auth/pages/login.html", user=current_user)

# Register route
@bp.route("/register/", methods=("GET", "POST"))
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            print("Already exists")
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            new_user = Users(email=email, firstName=first_name, lastName=last_name, password=generate_password_hash(
                password, method='sha256'),role=2)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for("auth_bp.login"))

    return render_template('auth/pages/register.html', user=current_user)