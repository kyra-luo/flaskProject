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
    # This will display on the HTML
    submit = SubmitField('Sign In')

# Defining register form
class RegisterForm(FlaskForm):
    Firstname = StringField(validators=[DataRequired(), Length(min=1, max=10)])
    Lastname = StringField(validators=[DataRequired(), Length(min=1, max=10)])
    gender = SelectField(choices=[('1', 'Male'), ('2', 'Female'),('3', 'non-binary')], validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired(), Length(min=6, max=20)])
    confirm_Password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('Password', message='Passwords must match.'),
        Length(min=6, max=20)
    ])
    email_address = StringField(validators=[DataRequired(), Email()])
    submit = SubmitField('Register')