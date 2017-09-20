"""
    Module has forms for manipulating shopping lists and shopping list items
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def invalidate_numbers_only(form, field):
    """Function to invalidate form fields that contain numbers only"""
    if field.data.isdigit():
        raise ValidationError('Field must have letters')


class ShoppinglistForm(FlaskForm):
    """Form used to create a shopping list"""
    name = StringField(
        'Add or edit a shopping list',
        validators=[DataRequired(), invalidate_numbers_only]
    )
    submit = SubmitField('Add')


class ShoppingitemForm(FlaskForm):
    """For used to create a shopping list item"""
    name = StringField('Add or edit an item', validators=[
        DataRequired(), invalidate_numbers_only])
    quantity = IntegerField(
        'Add or edit quantity of items',
        validators=[DataRequired(
            message='This field is required and must only contain numbers'
            )]
    )
    submit = SubmitField('Add')
