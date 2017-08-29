""" Blueprint for our app's landing page"""
from flask import Blueprint

landing_page = Blueprint('landing_page', __name__)

from . import views
