from flask import Blueprint, render_template

portfolio_bp = Blueprint(
    "portfolio",
    __name__
)

@portfolio_bp.route("/portfolio")
def portfolio():
    return render_template(
        "pages/portfolio.html"
    )