import os


class Config:
    API_TITLE = "Quenic REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Consider loading this from an environment variable
    SECRET_KEY = os.getenv("SECRET_KEY")  # Consider loading this from an environment variable


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    pass
