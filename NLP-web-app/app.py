from flask import Flask, render_template, request, redirect, session
from db import Database

app = Flask(__name__)
app.secret_key = '123456'

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    response = dbo.insert(name, email, password)
    
    if response:
        return render_template('login.html', message='Registration successful!! Kindly login to continue.', color='success')
    else:
        return render_template('register.html', message='Registration failed!! Email Already Exists. Please try again.')
    
@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    response = dbo.login(email, password)
    
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message='Login failed!! Invalid credentials. Please try again.', color='danger')
    
@app.route('/profile')
def profile():
    if session.get('logged_in') == 1:
        return render_template('profile.html')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)