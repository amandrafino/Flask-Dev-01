# Import the Flask Class
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, flash, redirect, render_template, request, url_for, flash
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


# GET & POST
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
         user = request.form["nm"]  
         return redirect(url_for("user", usr=user))
    else:
         return render_template('login.html') 


@app.route('/<usr>')
def user(usr):
    return f"<h3>{ usr }</h3>"





if __name__ == '__main__':
    app.run()

