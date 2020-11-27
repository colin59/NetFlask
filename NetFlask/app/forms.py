from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    FilmName=StringField('Film Name', validators=[DataRequired()])
    Submit = SubmitField('Flask !')
