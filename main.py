from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


            
load_dotenv()

UPLOAD_FOLDER = 'static/estimates'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('landing.html')    

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/estimate', methods=['GET', 'POST'])
def request_estimate():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        project_type = request.form.get('project_type')
        budget = request.form.get('budget')
        deadline = request.form.get('deadline')
        description = request.form.get('description')
        file = request.files.get('file')

        if not all([name, email, project_type, budget, deadline, description]):
            flash('Please fill out all required fields.', 'danger')
            return redirect(url_for('estimate.request_estimate'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        # TODO: Add logic to store or email estimate data
        flash('Estimate request sent! I’ll be in touch soon.', 'success')
        return redirect(url_for('estimate.request_estimate'))

    return render_template('estimate.html')



if __name__ == '__main__':
    app.run(debug=True)