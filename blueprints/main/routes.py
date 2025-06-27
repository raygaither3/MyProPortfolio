from flask import Blueprint, flash, redirect, render_template, request, url_for
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv 

load_dotenv(dotenv_path="./.env")

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('main/landing.html')

@main_bp.route('/projects')
def projects():
    return render_template('main/projects.html')

@main_bp.route('/services')
def services():
    return render_template('main/services.html')

@main_bp.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')

        subject = f"New Contact Message from {email}"
        body = f"Message from {email}:\n\n{message}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_USER, EMAIL_PASS)
                smtp.send_message(msg)
            flash('Message sent! I’ll get back to you soon.', 'success')
        except Exception as e:
            print("Email error:", e)
            flash('There was a problem sending your message.', 'danger')

        return redirect(url_for('main.contact'))

    return render_template("main/contact.html")