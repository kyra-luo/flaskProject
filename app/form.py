from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
    communities = SelectField('Communities', choices=[('', 'Select a community...'),('1', 'Community 1'), ('2', 'Community 2'), ('3', 'Community 3')], validators=[DataRequired()])
    topic = TextAreaField('Your topic', validators=[
        DataRequired(), Length(min=1, max=250)])
    body = TextAreaField('Say something...', validators=[
        DataRequired(), Length(min=1, max=5000)])
    
    
class CommentForm(FlaskForm):
    comment_body = TextAreaField('Comment', validators=[
        DataRequired(), Length(min=1, max=1000)])