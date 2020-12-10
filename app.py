from flask import Flask, url_for, request, render_template, session, redirect, flash
from markupsafe import escape
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
import matplotlib
matplotlib.use('Agg')
from mongoengine import connect
import random
from graph import *
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import gc
import pymongo as pm
from mongoengine import *
from models import *
from helpers import userBet, calculateReturn

connection = pm.MongoClient('mongodb+srv://alvinalaphat:1uScotvkqjQkM0HV@economeme-0ffr6.mongodb.net/test?retryWrites=true&w=majority', 27017)
dbs = connection.Profiles
collection = dbs.users

# creates the Flask application
app = Flask(__name__)
db = MongoEngine(app)

# Views
# GET is default method, just renders the login page
# POST method is for users to send a POST request w their login info to /login
@app.route('/', methods=['GET','POST'])
def preview():
	session["logged_in"] = False
	return render_template("index.html")

@app.route('/profile', methods=['GET','POST'])
def profile():
	find_user = {"username" : request.form['username']}
	current_profile = collection.find_one(find_user)
	return render_template("profile.html")

@app.route('/leaderboard', methods=['GET','POST'])
def leaderboard():
 	return render_template("leaderboard.html")

@app.route('/layout', methods=['GET','POST'])
def template():
	find_user = {"username" : request.form['username']}
	current_profile = collection.find_one(find_user)
	home()
	return render_template("layout.html", username=current_profile['username'], email=current_profile['email'], coins=current_profile['coins'])

@app.route('/home', methods=['GET','POST'])
def home():
	template()
	return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['logged_in'] = True
		email = request.form['email']
		password = request.form['psw']
		user = {"email" : email, "password" : password}
		if collection.find_one(user):
			return template()
	return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		session['logged_in'] = True
		new_user = {"username" : request.form['username'],
				"email" : request.form['email'],
				"password" : request.form['psw'],
				"coins" : 500}
		collection.insert_one(new_user)
		template()
		return home()
	return render_template("signup.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	print("Logging Out")
	session['logged_in'] = False
	return preview()

@app.route('/trade', methods=['GET','POST'])
def trade():
	final = []
	memes = graph()
	for key,value in memes.items():
		final.append(Meme(key,value[-1]))
	return render_template("trade.html", data=final)

@app.route('/profile', methods=['GET','POST'])
def bet():
	# days_to_win = str(request.form['days_bet']).lower()
	# percentage = str(request.form['Percentage']).lower()
	# coins = str(request.form['Coins']).lower()
	# total_coins = userBet(1000, coins, days_to_win, percentage)
	return render_template("profile.html")

# unique user profile
#@app.route('/user/<username>')

# def signup():
	# if request.method == 'POST':
	# 	session['username'] = request.form['username']
	# 	session['password'] = request.form['password']
	# 	newUser = User(session.get('username'),session.get('password'),numCoins = 250).save()
	# 	return redirect("https://economeme.webflow.io/")
	# return render_template("signup.html")
    
# Causes the website to rerender whenever you save your file
app.config["DEBUG"] = True

# Secret key for sessions
app.config["SECRET_KEY"] = b'H\xcf\xf9\x8f\x98\xf8\xe3\x82\xcfd'

app.config['MONGODB_SETTINGS'] = {
    'db': 'Economeme',
	'collection': 'users',
    'host': '127.0.0.1',
    'port': 5000
}