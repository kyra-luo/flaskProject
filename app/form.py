from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app import db, SQLAlchemy as sa
from app.models import User, Post, Comment


class PostForm(FlaskForm):
    communities = SelectField('Communities', choices=[('', 'Select a community...'),('1', 'Community 1'), ('2', 'Community 2'), ('3', 'Community 3')], validators=[DataRequired()])
    topic = TextAreaField('Your topic', validators=[
        DataRequired(), Length(min=1, max=250)])
    body = TextAreaField('Say something...', validators=[
        DataRequired(), Length(min=1, max=5000)])
    
    
class CommentForm(FlaskForm):
    comment_body = TextAreaField('Comment', validators=[
        DataRequired(), Length(min=1, max=1000)])
    post_id = IntegerField('Post ID', validators=[DataRequired()])


# Defining login form
class LoginForm(FlaskForm):
    # get username, input required.
    email_addr = StringField(validators=[DataRequired(), Email()])
    # get Type, input required.
    # userid = StringField(validators=[DataRequired()])
    # get password, input required.
    password = PasswordField(validators=[DataRequired()])
    # This will display on the HTML
    submit = SubmitField('Sign In')


# Defining register form
class RegisterForm(FlaskForm):
    Firstname = StringField(validators=[DataRequired(), Length(min=1, max=10)])
    Lastname = StringField(validators=[DataRequired(), Length(min=1, max=10)])
    Username = StringField(validators=[DataRequired(), Length(min=2, max=10)])
    gender = SelectField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'non-binary')], validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired(), Length(min=6, max=20)])
    confirm_Password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('Password', message='Passwords must match.'),
        Length(min=6, max=20)
    ])
    email_address = StringField(validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
