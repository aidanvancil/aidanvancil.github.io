#Caching
import functools
import time

# Simple cache decorator using a dictionary
def cache(func):
    memo = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    
    return wrapper

# Example usage
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#------------------------------------------
# User Sessions
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Validate username and password
        if username == 'admin':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/')
def home():
    if 'username' in session:
        return f'Welcome, {session["username"]}!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
