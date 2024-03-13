# Import the Flask Class
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, flash, redirect, render_template,\
    request, url_for, flash, session
from lists import names


# Create an instance of this class
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "He is the Rock"

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
         user = request.form["nm"]  
         session["user"] = user
         return redirect(url_for("user"))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html') 


# User Page
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h3>{ user }</h3>"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()




