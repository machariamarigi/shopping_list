""" Module contains forms to be used to register and login users """

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length
from wtforms.validators import ValidationError


def invalidate_numbers_only(form, field):
    """Function to invalidate form fields that contain numbers only"""
    if field.data.isdigit():
        raise ValidationError('Field must have letters')


class SignUpForm(FlaskForm):
    """Form for users to sign up"""
    username = StringField('Username', validators=[
        DataRequired(),
        invalidate_numbers_only
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        length(min=8)
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        EqualTo('password'),
    ])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """Form for users to login"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
