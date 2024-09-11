from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

from flask_migrate import Migrate

from app.model import db
from app.config import config_options


def create_app(config_name="prd"):

    app = Flask(__name__)
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config.SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI


    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)

    # app 
    from app.books import books_blueprint

    app.register_blueprint(books_blueprint)

    # -2 -> Home
    from app.home import home_blueprint

    app.register_blueprint(home_blueprint)


    return app





