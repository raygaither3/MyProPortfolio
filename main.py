from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, jsonify, url_for
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


            
load_dotenv()


app = Flask(__name__)


bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('home.html')    


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


if __name__ == '__main__':
    app.run(debug=True)