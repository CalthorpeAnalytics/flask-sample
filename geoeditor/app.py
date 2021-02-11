from flask import Flask

from geoeditor.extensions import db
from geoeditor.extensions import migrate


def create_app(testing: bool = False) -> Flask:
    """Application factory, used to create application"""
    app = Flask("geoeditor")
    app.config.from_object("geoeditor.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_extensions(app: Flask) -> None:
    """configure flask extensions"""
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask) -> None:
    """register all blueprints for application"""
    pass
