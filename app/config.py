
import os


class Config:
    SECRET_KEY = os.urandom(32)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://library:iti2@localhost:5432/flask_project_2"
    )
    UPLOADED_PHOTOS_DEST = "app/static/"


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig,
}
