import os
import requests
import sys
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)