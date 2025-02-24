from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, jsonify
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


@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    user_email = data.get('userEmail')
    user_message = data.get('userMessage')

    # Prepare the message
    message = f"""
    User Email: {user_email}
    Message: {user_message}
    """

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  
    sender_email = os.getenv('EMAIL_SENDER')
    sender_password = os.getenv('EMAIL_PASSWORD')
    receiver_email = os.getenv('EMAIL_RECEIVER')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Message'] = 'Contact Form Submission'

    msg.attach(MIMEText(message, 'plain'))

    try:
        # Sending the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return jsonify({'message': 'Email sent successfully!'}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to send email.'}), 500



if __name__ == '__main__':
    app.run(debug=True)