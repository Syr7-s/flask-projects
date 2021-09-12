from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h432hisdf5465akjafsdsd65asdwca'

    from . import app

    app.register_blueprint(app.bp)
    return app


