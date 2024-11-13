from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from a .env file

app = Flask(__name__)
api = Api(app)
CORS(app)

app.json.compact = False  # Disable JSON compact representation
