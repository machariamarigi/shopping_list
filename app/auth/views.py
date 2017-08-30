
"""Module handle authentification views"""

from flask import render_template, flash, redirect, url_for, session

from . import auth
from .forms import SignUpForm, LoginForm
from app import store


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Method to handle views for loging in"""
    form = LoginForm()
    if form.validate_on_submit():
        for user in store.users:
            if form.email.data == user['email']:
                if form.password.data == user['password']:
                    store.current_user = user
                    session['logged_in'] = True
                    flash('You are logged on.')
                    return redirect(
                        url_for(
                            'dashboard.dashboard_page'))

    return render_template('auth/login.html', title='login', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Method to handle sign up of users"""
    form = SignUpForm()
    if form.validate_on_submit():
        store.add_user(form.username.data, form.email.data, form.password.data)
        for user in store.users:
            if form.email.data == user['email']:
                store.current_user = user
        session['logged_in'] = True
        flash('You are logged on.')
        return redirect(url_for('dashboard.dashboard_page'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/logout')
def logout():
    """Log out a user"""
    session.pop('logged_in', None)
    return redirect(url_for('landing_page.landing'))
