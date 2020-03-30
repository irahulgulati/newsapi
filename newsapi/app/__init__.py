from flask import Flask, jsonify
from flask_cors import CORS,cross_origin
from .views import news, thought
application = Flask(__name__)
#enabling Cross-Origin resource sharing
CORS(application)
from app import routes