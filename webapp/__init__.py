'''
тут будет какая-то хрень...
'''

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html',
                               title='Синонимайзер',
                               )
    return app
