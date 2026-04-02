from . import auth_bp
from flask import render_template


@auth_bp.route('/login')
def login():
    return "Login Page"


@auth_bp.route('/register')
def register():
    return "Register Page"