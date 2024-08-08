import json, os, sys
from RequestsUtil import RequestsUtil
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import *

app = Flask(__name__, template_folder='templates')

client_database = MongoClient('mongodb://root:root@mongo:27017/')

API_DASHBOARD = RequestsUtil(base_url="api-dashboard:5001")

@app.route('/', methods=['GET'])
def index():
    return "Je suis sur le dashboard."