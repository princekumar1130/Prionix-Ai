from flask import Flask, render_template, request, redirect, flash, session, send_from_directory
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
from database.models import db, Consultation, ContactMessage

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

        try:
            msg = Message(
                subject="🚀 New Consultation Request - Prionix AI",
                recipients=["prionixai@gmail.com"]
            )

            msg.body = f"""
A new consultation request has been received.

Name: {lead.full_name}
Email: {lead.email}
Company: {lead.company_name}
Project Type: {lead.project_type}
Budget: {lead.budget}
Deadline: {lead.deadline}

Description:
{lead.description}
"""

            mail.send(msg)

            client_msg = Message(
                subject="Thank You For Contacting Prionix AI",
                recipients=[lead.email]
            )

            client_msg.body = f"""
Hello {lead.full_name},

Thank you for contacting Prionix AI.

We have successfully received your consultation request.

Our team will contact you shortly.

Regards,
Prionix AI Team
"""

            mail.send(client_msg)

        except Exception as e:
            print("Email Error:", e)

        flash(
            "✅ Thank you for contacting Prionix AI. We have received your request and will contact you shortly.",
            "success"
        )

        return redirect("/consultation")

    return render_template("pages/consultation.html")

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

        try:

            msg = Message(
                subject="📩 New Contact Message - Prionix AI",
                recipients=["prionixai@gmail.com"]
            )

            msg.body = f"""
A new contact message has been received.

Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}

Message:
{contact.message}
"""

            mail.send(msg)

        except Exception as e:
            print("Email Error:", e)

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
@app.route("/test-email")
def test_email():
    try:
        print("MAIL_SERVER:", app.config["MAIL_SERVER"])
        print("MAIL_PORT:", app.config["MAIL_PORT"])
        print("MAIL_USERNAME:", app.config["MAIL_USERNAME"])
        print("MAIL_USE_TLS:", app.config["MAIL_USE_TLS"])

        msg = Message(
            subject="Brevo Test",
            recipients=["prionixai@gmail.com"]
        )
        msg.body = "Testing Brevo SMTP"

        mail.send(msg)

        return "SUCCESS"

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"ERROR: {e}"
@app.route("/admin/logout")
def admin_logout():

    session.pop("admin", None)

    flash("Logged out successfully.", "success")

    return redirect("/admin/login")
@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")

if __name__ == "__main__":
    app.run(debug=True)

   
