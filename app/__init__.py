from flask import Flask
from flask_mongoengine import MongoEngine
from .config import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["MONGODB_SETTINGS"] = {
        "db": mongodb,
        "host": mongodb_url,
    }

    db = MongoEngine()
    db.init_app(app)

    with app.app_context():
        from .api.item import item_api

        app.register_blueprint(item_api)

    @app.after_request
    async def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = (
            "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        )
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    return app
