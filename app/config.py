import os

# Retrieve enviroment variables from .env file

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASS = os.environ.get("DATABASE_PASS")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

SECRET_KEY: str = os.environ.get("SECRET_KEY")

APP_FRONTEND_URL = os.environ.get("APP_FRONTEND_URL")
APP_BACKEND_OP_URL = os.environ.get("APP_BACKEND_URL")

TIMEZONE = os.environ.get("TIMEZONE", "Chile/Continental")

ORIGINS: list = [
    "*"
]