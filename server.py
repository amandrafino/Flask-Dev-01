# Import the Flask Class
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, flash, redirect, render_template, request, url_for, flash


# Create an instance of this class
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "He is the Rock"


@app.route('/')
@app.route('/home')
def home():
    first_name = 'Albert'
    return render_template('index.html', first_name=first_name)


# User
@app.route('/<name>')
def user(name):
    return f'''
    <h3>Welcom back {name}!</h3>
    <p>Back Home: <a href="{url_for('home')}">Home</a></p>
    '''

# Redirect to user 
@app.route('/admin')
def admin():
    return redirect(url_for('user', name="Admin!"))


@app.route('/about')
def about():
    flash('Hello Albert. This is the about page!')
    first_name = 'Albert'
    return render_template('about.html', first_name=first_name)


# Sandbox
@app.route('/sandbox')
def sandbox():
    return render_template('sandbox.html')


if __name__ == '__main__':
    app.run()

