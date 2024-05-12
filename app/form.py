from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class PostForm(FlaskForm):
    communities = SelectField('Communities', choices=[('1', 'Community 1'), ('2', 'Community 2'), ('3', 'Community 3')],
                              validators=[DataRequired()])
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


# Defining login form
class LoginForm(FlaskForm):
    # get username, input required.
    email_addr = StringField(validators=[DataRequired(), Email()])
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
