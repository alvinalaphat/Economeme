from flask import Flask, url_for, request, render_template, session, redirect
from markupsafe import escape
from flask_mongoengine import MongoEngine
from models import *

# creates the Flask application
app = Flask(__name__)
app.config.from_pyfile('the-config.cfg')
db = MongoEngine(app)

# views:
@app.route('/')
def index():
	return render_template("index.html")

# GET is default method, just renders the login page
# POST method is for users to send a POST request w their login info to /login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		session['username'] = request.form['username']
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid, please try again'
		else:
			return redirect('/')
	return render_template("login.html", error=error)

# def login():
# error = None
# if request.method == 'POST':
#     if valid_login(request.form['username'],
#                    request.form['password']):
#         return log_the_user_in(request.form['username'])
#     else:
#         error = 'Invalid username/password'
# # the code below is executed if the request method
# # was GET or the credentials were invalid
# return render_template('login.html', error=error)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	print("logging out\n")
	session.pop('username', None)
	return redirect("/")
	
# unique user profile
#@app.route('/user/<username>')
@app.route('/profile')
def profile():
	return render_template("profile.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/subpage')
def hello_world():
    return 'Hello, World!'
    
# Causes the website to rerender whenever you save your file
app.config["DEBUG"] = True

# Secret key for sessions
app.config["SECRET_KEY"] = b'H\xcf\xf9\x8f\x98\xf8\xe3\x82\xcfd'
