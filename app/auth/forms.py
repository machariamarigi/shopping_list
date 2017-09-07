""" Module contains forms to be used to register and login users """

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length


class SignUpForm(FlaskForm):
    """Form for users to sign up"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password'),
        length(min=8)
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """Form for users to login"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
