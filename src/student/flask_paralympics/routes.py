""" This is an example of a minimal Flask application."""
# Import the Flask class from the Flask library
from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")  # Rendering from 'templates/index.html'

