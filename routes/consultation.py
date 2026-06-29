from flask import Blueprint, render_template

consultation_bp = Blueprint(
    "consultation",
    __name__
)

@consultation_bp.route("/consultation")
def consultation():
    return render_template(
        "pages/consultation.html"
    )