from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired


class MessageFormWord(FlaskForm):
    message = TextAreaField('Введите слово', validators=[InputRequired()])
    submit = SubmitField('Подобрать синонимы')


class MessageFormText(FlaskForm):
    message = TextAreaField('Введите текст', validators=[InputRequired()])
    submit = SubmitField('Подобрать синонимы')
