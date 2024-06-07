from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo

class signup(FlaskForm):
    uname = StringField('Username',validators=[DataRequired('Give Username'),Length(5,30)])
    mail = StringField('Email',validators=[DataRequired('Give Email'),Email()])
    gen = SelectField('Gender',choices=['M','F','Oth'], validators=[Optional()])
    dob = DateField('DOB',validators=[DataRequired('Enter DOB')])
    pwd = PasswordField('Password', validators=[DataRequired('Enter Password'), Length(8,15)])
    cpwd = PasswordField('Confirm Password', validators=[DataRequired('Confirm the  Password'), Length(8,15), EqualTo('pwd')])
    sub = SubmitField('Signup')

class login(FlaskForm):
    uname = StringField('Username',validators=[DataRequired('Give Username'),Length(5,30)])
    pwd = PasswordField('Password', validators=[DataRequired('Enter Password'), Length(8,15)])
    sub = SubmitField('Login')