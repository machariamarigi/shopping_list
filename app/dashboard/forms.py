from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ShoppinglistForm(FlaskForm):
    """Form used to create a shopping list"""
    name = StringField('Add or edit list', validators=[DataRequired()])
    submit = SubmitField('Add')


class ShoppingitemForm(FlaskForm):
    """For used to create a shopping list item"""
    name = StringField('Add or edit an item', validators=[DataRequired()])
    quantity = StringField(
        'Add or edit quanity of items', validators=[DataRequired()])
    submit = SubmitField('Add')
