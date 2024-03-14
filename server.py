# Import the Flask Class
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, flash, redirect, render_template,\
    request, url_for, flash, session
from lists import names
from datetime import timedelta
import sqlalchemy


# Create an instance of this class
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "He is the Rock"

# Time to Live
app.permanent_session_lifetime = timedelta(days=5)

# Home
@app.route('/')
@app.route('/home')
def home():
    first_name = 'Albert'
    spouse= 'Gail'
    return render_template('index.html', name=first_name, content=spouse)


# About
@app.route('/about')
def about():
    flash('Hello Albert. This is the about page!')
    first_name = 'Albert'
    return render_template('about.html', first_name=first_name)


# Sandbox
@app.route('/sandbox')
def sandbox():
    return render_template('sandbox.html', send_names=names)


# Login Page / GET & POST / Session
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]  
        session["user"] = user
        flash('Login Successful!')
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash('Already logged in!')
            return redirect(url_for('user'))
        return render_template('login.html')


# User Page
@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template('user.html', email=email)
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        flash(f'You have been successfully logged out.', 'info')
    session.pop('user', None)
    session.pop("email", None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()




