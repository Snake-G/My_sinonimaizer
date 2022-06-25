# coding: utf-8
"""
Запуск сервера командой:
set FLASK_APP=__init__.py && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

Push ветки кода
git push --set-upstream origin feature/server_flask
"""

from flask import Flask, render_template, request, redirect, url_for
from webapp.projects.forms import MessageForm
from modul_word2vec.Rus2vec_my_models import get_sinonim_for_word


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html', title='Синонимайзер')

    @app.route('/for_input_word', methods=['GET', 'POST'])
    def for_input_word():
        input_text_form = MessageForm()
        if input_text_form.validate_on_submit():
            return_result = get_sinonim_for_word(input_text_form.message.data)
            print(return_result)
            return render_template('for_output_words.html', len=len(return_result), words=return_result)

        return render_template('for_input_word.html', title='Подбор синонимов для слова',
                               form=input_text_form)

    @app.route('/for_input_text', methods=['GET', 'POST'])
    def for_input_text():
        return render_template('for_input_text.html', title='Подбор синонимов для текста')

    return app
