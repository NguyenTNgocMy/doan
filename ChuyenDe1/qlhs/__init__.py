from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = '#%^&(*$%^&(78678675$%&^&$^%*&^%&*^'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/qlhs?charset=utf8mb4' % quote('123456')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)