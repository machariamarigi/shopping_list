
"""Module handle authentification views"""

from flask import render_template, flash, redirect, url_for, session

from . import auth
from .forms import SignUpForm, LoginForm
from app import store


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Method to handle views for loging in"""
    if 'username' not in session.keys():
        form = LoginForm()
        if form.validate_on_submit():
            for user in store.users:
                if form.email.data == user['email']:
                    if form.password.data == user['password']:
                        current_user = {
                            user['username']: user
                        }
                        store.current_users.update(current_user)
                        session['username'] = user['username']
                        return redirect(
                            url_for(
                                'dashboard.dashboard_page'))
                    else:
                        flash('Wrong password, please try again')
                        return redirect(url_for('auth.login'))
            flash('Email not recognised, please Register or try again')
            return redirect(url_for('auth.login'))

        return render_template('auth/login.html', title='login', form=form)
    else:
        return redirect(url_for('dashboard.dashboard_page'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Method to handle sign up of users"""
    if 'username' not in session.keys():
        form = SignUpForm()
        if form.validate_on_submit():
            for user in store.users:
                if form.email.data == user['email']:
                    flash("Email already exists. Try again")
                    return redirect(url_for('auth.register'))
                elif form.username.data == user['username']:
                    flash("Username is already taken. Try another one")
                    return redirect(url_for('auth.register'))
            else:
                store.add_user(
                    form.username.data, form.email.data, form.password.data)
                flash('Account created you can now login')
                return redirect(url_for('auth.login'))
        return render_template('auth/register.html', form=form, title='Register')
    else:
        return redirect(url_for('dashboard.dashboard_page'))


@auth.route('/logout')
def logout():
    """Log out a user"""
    session.pop('username', None)
    return redirect(url_for('auth.login'))
