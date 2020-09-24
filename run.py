from app import app
from views import *
from models import *

# Acts as "main" function in Python, starts the Flask app
if __name__ == "__main__":
    app.run(debug=True)
