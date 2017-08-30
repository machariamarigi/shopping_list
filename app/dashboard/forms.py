from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ShoppinglistForm(FlaskForm):
    """Form used to create a shopping list"""
    name = StringField('Add or edit list', validators=[DataRequired()])
    submit = SubmitField('Add')
