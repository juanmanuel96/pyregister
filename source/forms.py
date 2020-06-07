from .libraries import (BooleanField, DataRequired, Email, EqualTo, FlaskForm,
                        Length, PasswordField, StringField, SubmitField,
                        ValidationError)

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            DataRequired('You must choose a username')
        ]
    )
