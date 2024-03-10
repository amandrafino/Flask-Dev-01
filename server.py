# Import the Flask Class
from flask import Flask, flash, redirect, render_template, request, url_for
# Create an instance of this class
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "He is the Rock"


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', first_name=first_name)

@app.route('/about')
def about():
    flash('Hello Albert. This is the about page!')
    first_name = 'Albert'
    return render_template('about.html', first_name=first_name)

# Add User Albert
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


if __name__ == '__main__':
    app.run()
