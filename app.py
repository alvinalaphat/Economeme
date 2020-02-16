from flask import Flask, url_for, request, render_template, session, redirect
from markupsafe import escape
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from mongoengine import connect
from mongoengine import *

# use to connect the MongoDB databse:
# connect('project1', host='127.0.0.1', port=5000)

# creates the Flask application
app = Flask(__name__)
db = MongoEngine(app)

# views:
@app.route('/')
def preview():
 	return render_template("preview.html")

# GET is default method, just renders the login page
# POST method is for users to send a POST request w their login info to /login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		session['username'] = request.form['username']
		session['password'] = request.form['password']
		current_user = User(username=session.get('username'), password=session.get('password')).save()
		#print(current_user.username)
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			session['valid'] = 0;
			error = 'Invalid, please try again'
		else:
			session['valid'] = 1;
			return redirect('/')
	return render_template("login.html", error=error)



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

app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': '127.0.0.1',
    'port': 5000
}

