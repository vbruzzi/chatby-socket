from flask import Flask, jsonify, request, redirect, url_for
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
from bson import ObjectId
from os import environ
import os
import datetime
import json
import hashlib

# Encryption Salt
SALT = "thisistheSALT"
# Mongo URI
mongoURI = os.environ['connectionstring']
client = MongoClient(mongoURI)
db = client.Chatby


port = int(os.getenv('PORT', 5000))
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

@socketio.on('connection', namespace='/')
def test_connect():
    print("A user has connected")

@socketio.on('message')
def handle_message(message):
        emit('message', message, broadcast=True)
        
