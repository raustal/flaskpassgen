from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class PassLength(FlaskForm):
    password_length = IntegerField("Password Length?", validators=[DataRequired()])
    submit = SubmitField("Generate Password")
