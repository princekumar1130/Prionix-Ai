import os

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY","prionix-secret-key")
    SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    BREVO_API_KEY=os.environ.get("BREVO_API_KEY")
    BREVO_SENDER_EMAIL=os.environ.get("BREVO_SENDER_EMAIL","prionixai@gmail.com")

    ADMIN_USERNAME="Princekumar_1130"
    ADMIN_PASSWORD="Prionixai12!@"

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
