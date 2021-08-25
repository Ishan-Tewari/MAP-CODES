from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy

# creating flask app
app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

