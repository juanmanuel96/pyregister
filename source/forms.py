from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            DataRequired('You must choose a username')
        ]
    )