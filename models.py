from mongoengine import *
from app import *
from helpers import *
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
import gc
 
 
class User(Document):
	# __tablename__ = 'users'
	current_user = BinaryField()
	username = StringField(max_length=50, required=True)
	password = StringField(max_length=50, required=True)
	numCoins = DecimalField() 
	# bets = Array()
    # last_bet

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    
# class Bet(db.User):
# 	# t = x
# 	# cost 
# 	# cloud
# 	# success = BinaryField().  # 1 or 0

 
class Meme():
	def __init__(self,meme,freq):
		self.meme = meme
		self.freq = freq