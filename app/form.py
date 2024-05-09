from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    communities = SelectField('Communities', choices=[('1', 'Community 1'), ('2', 'Community 2'), ('3', 'Community 3')], validators=[DataRequired()])
    topic = TextAreaField('Your topic', validators=[
        DataRequired(), Length(min=1, max=200)])
    post = TextAreaField('Say something...', validators=[
        DataRequired(), Length(min=1, max=1000)])
    
class CommunityForm(FlaskForm):
    communityName = StringField('CommunityName', validators=[DataRequired(), Length(min=1, max=15) ])
    category = SelectField('Category', choices=[('1','IT'), ('2','Mathmatic'), ('3','Physics'),('4','Engineering'),('5','Sport')])
    description = TextAreaField('What is this community all about', validators=[
        DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField('Create new community')