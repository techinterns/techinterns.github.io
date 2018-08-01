from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Email, Length, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirmPassword', message='Passwords must match')])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    contactNumber = StringField('Phone Number', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
    street = StringField('Home Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired(), Length(min=0, max=2)])
    work = SelectField('Work Location',
        choices=[('ballDrive', 'Ball Drive'), ('riderTrail', 'Rider Trail'), ('westPortPlace', 'West Port Place')], 
        validators=[DataRequired()])
    genderPreferred = SelectField('Gender you would prefer to travel with', 
        choices=[('both', 'Both'), ('female', 'Female'), ('male', 'Male')],
        validators=[DataRequired()])
    car = SelectField('Do you have a car?',
        choices=[('no', 'No'), ('yes', 'Yes')],
        validators=[DataRequired()]
    )
    numberOfSeats = IntegerField('Number of Seats', validators=[Optional()])
    mpg = DecimalField('Miles per Gallon', validators=[Optional()])
    manufacturer = StringField('Manufacturer', validators=[Optional()])
    model = StringField('Model', validators=[Optional()])
    number = StringField('License Plate Number', validators=[Optional()])
    submit = SubmitField('Register', validators=[Optional()])

class EditSettingsForm(RegisterForm):
    password = PasswordField('Password', validators=[EqualTo('confirmPassword', message='Passwords must match')])
    confirmPassword = PasswordField('Confirm Password', validators=[Optional()])
    submit = SubmitField('Save Changes')