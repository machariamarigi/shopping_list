""" Blueprint for our app's homepage"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
