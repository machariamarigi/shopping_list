""" Module for handling landing_page blueprint views """

from flask import render_template

from . import landing_page


@landing_page.route('/')
def landing():
    """Render the landing_page template on the / route"""
    return render_template('index.html')
