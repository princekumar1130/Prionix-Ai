from flask import Blueprint, render_template

blog_bp = Blueprint(
    "blog",
    __name__
)

@blog_bp.route("/blog")
def blog():
    return render_template(
        "pages/blog.html"
    )