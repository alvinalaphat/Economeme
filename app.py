from flask import Flask, url_for, request, render_template, session, redirect
from markupsafe import escape

# creates the Flask application
app = Flask(__name__)

# views:
@app.route('/')
def index():
	if 'username' in session:
		logged_in = 1
	logged_in = 0
	return render_template("index.html")

# GET is default method, just renders the login page
# POST method is for users to send a POST request w their login info to /login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid, please try again'
		else:
			return redirect('/')
	return render_template("login.html", error=error)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# unique user profile
@app.route('/user/<username>')
def profile(username):
	return '{}\'s profile'.format(escape(username))

@app.route('/subpage')
def hello_world():
    return 'Hello, World!'
    
# Causes the website to rerender whenever you save your file
app.config["DEBUG"] = True

# Secret key for sessions
app.config["SECRET_KEY"] = b'H\xcf\xf9\x8f\x98\xf8\xe3\x82\xcfd'
