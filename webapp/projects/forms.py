from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from bs4 import formatter


class MessageFormWord(FlaskForm):
    message = TextAreaField('Введите слово', validators=[DataRequired()])
    submit = SubmitField('Подобрать синонимы')


class MessageFormText(FlaskForm):
    message = TextAreaField('Введите текст', validators=[InputRequired()])
    submit = SubmitField('Подобрать синонимы')
