from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
app.config['SQLALCHEMY_TRACK_MY_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from controllers import products, customers, orders, admins
app.register_blueprint(products.router, url_prefix="/api")
app.register_blueprint(customers.router, url_prefix="/api")
app.register_blueprint(orders.router, url_prefix='/api')
app.register_blueprint(admins.router, url_prefix='/api')


