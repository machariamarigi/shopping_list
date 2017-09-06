""" Module for handling landing_page blueprint views """

from flask import render_template, session

from . import landing_page


@landing_page.route('/')
def landing():
    """Render the landing_page template on the / route"""
    session['logged_in'] = False
    return render_template('index.html')
