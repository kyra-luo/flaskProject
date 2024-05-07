from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class PostForm(FlaskForm):
    communities = SelectField('Communities', choices=[('1', 'Community 1'), ('2', 'Community 2'), ('3', 'Community 3')], validators=[DataRequired()])
    topic = TextAreaField('Your topic', validators=[
        DataRequired(), Length(min=1, max=200)])
    post = TextAreaField('Say something...', validators=[
        DataRequired(), Length(min=1, max=1000)])

# Defining login form
class LoginForm(FlaskForm):
    # get username, input required.
    username = StringField(validators=[DataRequired()])
    # get Type, input required.
    U_type = SelectField(choices=[('1', 'User'), ('2', 'Admin')], validators=[DataRequired(message=None)])
    # get password, input required.
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])