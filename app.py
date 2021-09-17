import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['ENV'] = "development"
app.config['DEBUG'] = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return jsonify('Hola Mundo')

@app.route("/user", methods=["POST"])
def user():
    user = User()
    user.name = request.json.get("name")
    user.password = request.json.get("password")
    user.email = request.json.get("email")
    user.isActive = request.json.get("isActive")

if __name__ == "__main__":
    app.run(host='localhost', port=8080)