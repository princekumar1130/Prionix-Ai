from flask import Flask, render_template, request, redirect, flash, session
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from database.models import db, Consultation, ContactMessage


def send_email(to_email, subject, text):
    payload = {
        "sender": {
            "email": app.config["BREVO_SENDER_EMAIL"],
            "name": "Prionix AI"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "textContent": text
    }

    headers = {
        "accept": "application/json",
        "api-key": app.config["BREVO_API_KEY"],
        "content-type": "application/json"
    }

    try:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers=headers,
            json=payload,
            timeout=20
        )

        print("=" * 50)
        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        print("=" * 50)

        response.raise_for_status()

    except Exception as e:
        print("BREVO ERROR:", str(e))  
db.init_app(app)

with app.app_context():
    db.create_all()

# ==========================
# Routes
# ==========================

@app.route("/")
def home():
    return render_template("pages/home.html")

@app.route("/services")
def services():
    return render_template("pages/services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("pages/portfolio.html")

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/consultation", methods=["GET", "POST"])
def consultation():

    if request.method == "POST":

        lead = Consultation(

            full_name=request.form["full_name"],
            email=request.form["email"],
            company_name=request.form["company_name"],
            project_type=request.form["project_type"],
            budget=request.form["budget"],
            deadline=request.form["deadline"],
            description=request.form["description"]

        )

        db.session.add(lead)

        db.session.commit()

        send_email("prionixai@gmail.com","🚀 New Consultation Request - Prionix AI",f"""A new consultation request has been received.

Name: {lead.full_name}

Email: {lead.email}

Company: {lead.company_name}

Project Type: {lead.project_type}

Budget: {lead.budget}

Deadline: {lead.deadline}

Description:
{lead.description}""")

        send_email(lead.email,"Thank You For Contacting Prionix AI",f"""Hello {lead.full_name},

Thank you for contacting Prionix AI.

We have successfully received your consultation request.

Our team will review your requirements and contact you shortly.

Project Type: {lead.project_type}
Budget: {lead.budget}

Thank you for choosing Prionix AI.

Regards,\nPrionix AI Team""")
        flash(
    "✅ Thank you for contacting Prionix AI. We have received your request and will contact you shortly.",
    "success"
)

        return redirect("/consultation")

    return render_template(
        "pages/consultation.html"
    )

        

    return render_template(
        "pages/consultation.html"
    )

@app.route("/testimonials")
def testimonials():
    return render_template("pages/testimonials.html")

@app.route("/blog")
def blog():
    return render_template("pages/blog.html")

@app.route("/faq")
def faq():
    return render_template("pages/faq.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        contact = ContactMessage(

            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            message=request.form["message"]

        )

        db.session.add(contact)

        db.session.commit()

        send_email("prionixai@gmail.com","📩 New Contact Message - Prionix AI",f"""A new contact message has been received.

Name: {contact.name}

Email: {contact.email}

Phone: {contact.phone}

Message:
{contact.message}""")

        flash(
            "✅ Thank you for contacting Prionix AI. We will get back to you shortly.",
            "success"
        )

        return redirect("/contact")

    return render_template("pages/contact.html")
@app.route("/test-leads")
def test_leads():

    leads = Consultation.query.all()

    output = ""

    for lead in leads:
        output += f"""
        <h3>{lead.full_name}</h3>
        <p>{lead.email}</p>
        <hr>
        """

    return output

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if (
    username == app.config["ADMIN_USERNAME"]
    and password == app.config["ADMIN_PASSWORD"]
):

            session["admin"] = True

            return redirect("/admin/leads")

        flash("Invalid Username or Password")

    return render_template("pages/admin_login.html")

@app.route("/admin/leads")
def admin_leads():

    if not session.get("admin"):

        return redirect("/admin/login")

    leads = Consultation.query.all()

    return render_template(
        "pages/admin_leads.html",
        leads=leads
    )


    return "Email Sent Successfully!"
@app.route("/admin/logout")
def admin_logout():

    session.pop("admin", None)

    flash("Logged out successfully.", "success")

    return redirect("/admin/login")

if __name__ == "__main__":
    app.run(debug=True)
from flask import send_from_directory

@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")
