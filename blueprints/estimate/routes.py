from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import os
import smtplib
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

estimate_bp = Blueprint('estimate', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'estimates')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")


@estimate_bp.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        project_type = request.form.get('project_type')
        budget = request.form.get('budget')
        deadline = request.form.get('deadline')
        description = request.form.get('description')
        file = request.files.get('file')

        # Build email
        msg = MIMEMultipart()
        msg['Subject'] = f"New Estimate Request from {name}"
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL

        body = f"""
        Name: {name}
        Email: {email}
        Project Type: {project_type}
        Budget: {budget}
        Deadline: {deadline}

        Description:
        {description}
        """

        msg.attach(MIMEText(body, 'plain'))

        if file and file.filename != '':
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)

                with open(filepath, "rb") as f:
                    part = MIMEApplication(f.read(), Name=filename)
                    part['Content-Disposition'] = f'attachment; filename="{filename}"'
                    msg.attach(part)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_USER, EMAIL_PASS)
                smtp.send_message(msg)
            flash('Estimate submitted! I’ll be in touch soon.', 'success')
        except Exception as e:
            print("Email error:", e)
            flash('Something went wrong. Please try again.', 'danger')

        return redirect(url_for('estimate.estimate'))

    return render_template("estimate/estimate.html")