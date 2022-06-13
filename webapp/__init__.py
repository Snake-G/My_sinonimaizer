# coding: utf-8


'''

Запуск сервера командой:
set FLASK_APP=__init__.py && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

Push ветки кода
git push --set-upstream origin feature/server_flask
'''

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html',
                               title='Синонимайзер',
                               )

    @app.route('/for_input_words')
    def for_input_words():
        return render_template('for_input_words.html', title='Синонимайзер')

    @app.route('/for_input_text')
    def for_input_text():
        return render_template('for_input_text.html', title='Синонимайзер')

    return app
