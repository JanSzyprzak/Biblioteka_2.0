from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author (add next)', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    number_of_pages = IntegerField('number_of_pages', validators=[DataRequired()])
    read = BooleanField('read')
    borrowed = BooleanField('borrowed')
