import os

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY") or "prionix-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = "prionixai@gmail.com"

    MAIL_PASSWORD = " mgpe aggc wqty mdev"

    MAIL_DEFAULT_SENDER = "prionixai@gmail.com"
    ADMIN_USERNAME = "Princekumar_1130"

    ADMIN_PASSWORD = "Prionixai12!@"