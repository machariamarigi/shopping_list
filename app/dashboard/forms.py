from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ShoppinglistForm(FlaskForm):
    """Form used to create a shopping list"""
    name = StringField(
        'Add or edit a shopping list',
        validators=[DataRequired()]
    )
    submit = SubmitField('Add')


class ShoppingitemForm(FlaskForm):
    """For used to create a shopping list item"""
    name = StringField('Add or edit an item', validators=[DataRequired()])
    quantity = StringField(
        'Add or edit quantity of items', validators=[DataRequired()])
    submit = SubmitField('Add')
