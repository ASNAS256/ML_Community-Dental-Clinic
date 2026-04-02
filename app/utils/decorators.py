# app/utils/decorators.py
from functools import wraps
from flask_login import current_user
from flask import abort


def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return wrapper