from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField("Item name", validators=[DataRequired()])
    received_date = DateField("Received date", validators=[DataRequired()])
    is_defect = BooleanField("Item has any defect?")
    description = TextAreaField("Item description")
    submit = SubmitField("Add")