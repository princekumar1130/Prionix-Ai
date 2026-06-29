from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consultation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100))

    email = db.Column(db.String(120))

    company_name = db.Column(db.String(100))

    project_type = db.Column(db.String(100))

    budget = db.Column(db.String(100))

    deadline = db.Column(db.String(100))

    description = db.Column(db.Text)
class ContactMessage(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(120))

    phone = db.Column(db.String(50))

    message = db.Column(db.Text)