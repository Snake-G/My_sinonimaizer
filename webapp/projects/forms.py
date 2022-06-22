from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class MessageForm(FlaskForm):
    # name = StringField('Name', validators=[DataRequired()])
    message = TextAreaField('Введите слово', validators=[InputRequired()])
    submit = SubmitField('Подобрать синонимы')
