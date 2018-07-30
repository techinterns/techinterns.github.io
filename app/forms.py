from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
    home_address = StringField('Home Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    location = SelectField('Work Location',
        choices=[('ballDrive', 'Ball Drive'), ('riderTrail', 'Rider Trail'), ('westPortPlace', 'West Port Place')], 
        validators=[DataRequired()])
    gender_preferred = SelectField('Gender you would prefer to travel with', 
        choices=[('both', 'Both'), ('female', 'Female'), ('male', 'Male')],
        validators=[DataRequired()])
    car = SelectField('Do you have a car?',
        choices=[('no', 'No'), ('yes', 'Yes')],
        validators=[DataRequired()]
    )
    number_of_seats = IntegerField('Miles per Gallon')
    manufacturuer = StringField('Manufacturer')
    model = StringField('Model')
    plate_number = StringField('License Plate Number')
    submit = SubmitField('Register')