from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b0972641aaa6166b78492a0cae01aa65'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://anonyme:admin@localhost/projet'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:postgresql://localhost:5432/projet'

db = SQLAlchemy(app)
from . import routes

