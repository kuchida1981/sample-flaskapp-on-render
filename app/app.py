from flask import Flask


def create_app():
    app = Flask(__name__)

    from .hello import bp as hello
    app.register_blueprint(hello, url_prefix="/hello")

    return app
