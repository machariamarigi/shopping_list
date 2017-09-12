""" Blueprint for a user's dashboard page"""
from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

from . import views
