#!/usr/bin/env python3
'''
0. Basic Flask app Module
'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config():
    '''
    Configuration class
    '''
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''
    Index route
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
