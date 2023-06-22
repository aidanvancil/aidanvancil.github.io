from flask import Flask, request, render_template, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define routes and their corresponding functions
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About page'

@app.route('/user/<username>')
def user_profile(username):
    return f'User: {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        if username == 'admin' and password == 'password':
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Run the Flask app
if __name__ == '__main__':
    app.run()
