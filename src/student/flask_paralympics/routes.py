""" This is an example of a minimal Flask application."""
# Import the Flask class from the Flask library
from flask import render_template, Blueprint, request

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/<name>')
def index(name=None):
    return render_template("index.html", name=name) 
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST request received. User logged in!"
    return "This is the login page. Send a POST request to log in."
