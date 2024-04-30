from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
    title = TextAreaField('Your title', validators=[
        DataRequired(), Length(min=1, max=80)])
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField('Submit')