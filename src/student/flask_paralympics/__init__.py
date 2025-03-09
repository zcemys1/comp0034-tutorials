import os
from flask import Flask

def create_app(test_config=None):
    # Create Flask app
    app = Flask(__name__, instance_relative_config=True)

    # App Configuration
    app.config.from_mapping(
        SECRET_KEY='arDYuNBe3H7qMt7Haply-Q',  # Replace 'dev' with a secure key in Step 2 which is arDYuNBe3H7qMt7Haply-Q   use code "import secrets" & "secrets.token_urlsafe(16)" for secret key in termninal
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'paralympics.sqlite'),
    )



    if test_config is None:
        # Load config.py if it exists (for production settings)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test-specific config
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
    # Register Blueprint
        from student.flask_paralympics.routes import main

        app.register_blueprint(main)


    return app

 