import json, os, sys
from RequestsUtil import RequestsUtil
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import *

app = Flask(__name__, template_folder='templates')

client_database = MongoClient('mongodb://root:root@mongo:27017/')

API_CONTROL = RequestsUtil(base_url="api-control:5000")
API_DASHBOARD = RequestsUtil(base_url="api-dashboard:5001")
API_SHOP = RequestsUtil(base_url="api-shop:5002")


@app.route('/', methods=['GET'])
def index():
    mydb = client_database["test"]
    return f"{client_database.list_database_names()}"