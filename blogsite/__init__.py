from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fa827ba53c8130521feb6706f0c0892d'

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///site.db'
db = SQLAlchemy(app)

from blogsite import routes