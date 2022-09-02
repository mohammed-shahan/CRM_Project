from apps import db
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from functools import wraps


def admin_required(func):
    @wraps(func)
    def isadmin(*args,**kwargs):
        if(current_user.role!=1):
            return redirect(url_for('auth_bp.warning'))
        return func(*args,**kwargs)
    return isadmin

def user_required(func):
    @wraps(func)
    def isuser(*args,**kwargs):
        if(current_user.role!=2):
            return redirect(url_for('auth_bp.warning'))
        return func(*args,**kwargs)
    return isuser

        
