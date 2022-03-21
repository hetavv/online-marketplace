from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # UR 'I' : i is for identifier
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '7312b53e88549c0b66c61e4f'
from market import routes
