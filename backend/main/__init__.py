from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import pymysql
# pymysql.install_as_MySQLdb()
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'main.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from main import route