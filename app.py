import flask
import os
import json
import requests 
import sys
from flask_cors import CORS

#app = flask.Flask(__name__)
#CORS(app)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    
    return "Hello World"
if __name__ == '__main__':
  app.run()
# Get port from environment variable or choose 9099 as local default
