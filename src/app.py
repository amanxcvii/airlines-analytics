# src/app.py
from flask import Flask
from flask_cors import CORS
from src.controller.data_controller import DataController  
from src.controller.test_controller import TestController

def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Initialize the controller
    DataController(app)
    TestController(app)
    
    return app
