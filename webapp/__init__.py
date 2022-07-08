# coding: utf-8
"""
Запуск сервера командой:
set FLASK_APP=__init__.py && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run --host=0.0.0.0

Push ветки кода
git push --set-upstream origin feature/server_flask
"""

from flask import Flask, render_template
from webapp.projects.forms import MessageFormWord, MessageFormText
from modul_word2vec.Rus2vec import get_synonym_for_word, get_synonym_for_text


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html', title='Синонимайзер')

    @app.route('/for_input_word', methods=['GET', 'POST'])
    def for_input_word():
        input_text_form = MessageFormWord()
        if input_text_form.validate_on_submit():
            list_of_synonyms = get_synonym_for_word(input_text_form.message.data)
            return render_template('for_input_word.html', title='Подбор синонимов для слова',
                                   form=input_text_form, words=list_of_synonyms,
                                   output='Подобранные синонимы для введенного слова:')
        else:
            return render_template('for_input_word.html', title='Подбор синонимов для слова',
                                   form=input_text_form)

    @app.route('/for_input_text', methods=['GET', 'POST'])
    def for_input_text():
        input_text_form = MessageFormText()
        if input_text_form.validate_on_submit():
            dict_of_synonyms = get_synonym_for_text(input_text_form.message.data)
            return render_template('for_input_text.html', title='Подбор синонимов для слова',
                                   form=input_text_form, dict=dict_of_synonyms,
                                   output='Подобранные синонимы:')

        return render_template('for_input_text.html', title='Синонимайзер с корректировкой текста',
                               form=input_text_form)

    return app
