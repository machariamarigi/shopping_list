""" Module for handling dashboard views"""

from flask import render_template, session

from . import dashboard


@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    """Render the homepage template on the / route"""
    if session['logged_in']:
        return render_template('dashboard/dashboard.html')
