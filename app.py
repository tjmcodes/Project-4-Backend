from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI

app = Flask(__name__)
# ! Configuring it with flask
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
# ! Removes a warning for an unused part of the library
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ! Instatiates Marshmallow framework
ma = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import artists

app.register_blueprint(artists.router, url_prefix="/api")
# app.register_blueprint(preparation.router, url_prefix="/api")
# app.register_blueprint(users.router, url_prefix="/api")







