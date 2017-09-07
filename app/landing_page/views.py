""" Module for handling landing_page blueprint views """

from flask import render_template, session, redirect, url_for

from . import landing_page


@landing_page.route('/')
def landing():
    """Render the landing_page template on the / route"""
    if 'username' not in session.keys():
        return render_template('index.html')
    else:
        return redirect(url_for('dashboard.dashboard_page'))
