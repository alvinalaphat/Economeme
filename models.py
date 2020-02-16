# models.py 
 
from mongoengine import *
from app import db
from helpers import *
 
 
class User(db.Document):
   # __tablename__ = 'users'
   	current_user = BinaryField()
    username = StringField(max_length=50, required=True)
    password = StringField(max_length=50, required=True)
    # numCoins = DecimalField() 
    # last_bet

class Bet(db.User):
	# t = x
	# cost 
	# cloud
	# success = BinaryField().  # 1 or 0

 
class Meme(db.Document):
	# frequency
	# virality

