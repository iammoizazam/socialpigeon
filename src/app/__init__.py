from flask import Flask
app = Flask(__name__)
app.secret_key = 'convex_application'
# Import your views or routes here if you have them.
from app import routes
