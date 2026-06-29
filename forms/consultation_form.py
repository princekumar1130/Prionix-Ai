from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired

class ConsultationForm(FlaskForm):

    full_name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )

    company_name = StringField(
        "Company Name"
    )

    project_type = StringField(
        "Project Type",
        validators=[DataRequired()]
    )

    budget = StringField(
        "Budget"
    )

    deadline = StringField(
        "Deadline"
    )

    description = TextAreaField(
        "Project Description",
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "Book Consultation"
    )