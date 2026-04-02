# ==============================
# 1. app/__init__.py (App Factory)
# ==============================

from flask import Flask
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)


    # Register blueprints
    from .auth import auth_bp
    from .patients import patients_bp
    from .appointments import appointments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(appointments_bp)

    return app
