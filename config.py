# ==============================
# 3. config.py
# ==============================

import os


class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dental_hmis.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
