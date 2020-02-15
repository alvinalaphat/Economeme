from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/subpage')
def hello_world():
    return 'Hello, World!'
