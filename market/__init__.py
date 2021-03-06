'''
We don't need them with the current architecture
export FLASK_APP='market'
export FLASK_DEBUG=1
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__) #__name__ => local file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '00c850c1210e1e42eb6c4edc'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes