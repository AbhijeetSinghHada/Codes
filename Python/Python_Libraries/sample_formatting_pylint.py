"""This is a sample file for formatting and linting."""
from flask import Flask
APP = Flask(__name__)
if __name__ == '__main__':
    APP.run(debug=True)
