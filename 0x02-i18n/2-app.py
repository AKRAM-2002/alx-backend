#!/usr/bin/env python3
'''
0. 2. Get locale from request Module
'''
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    '''
    Configuration class
    '''
    LANGUAGES = ["en", "2-app.pyfr"]
    DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    Get locale
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    Index route
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
