from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired()])
    password = PasswordField('Password', validators=[ DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    first_name = StringField('First name')
    last_name  = StringField('Last name')
    username = StringField('Username',validators=[ DataRequired() ])
    email = StringField('Email', validators=[ DataRequired() ])
    password = PasswordField('Password', validators=[ DataRequired() ])
    verify_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password') ])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    body = StringField('Make Post', validators=[ DataRequired() ])
    submit = SubmitField('Post')