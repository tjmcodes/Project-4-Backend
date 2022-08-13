import types
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config.environment import db_URI

app = Flask(__name__)
CORS(app)


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import artists, venues, genres, types

app.register_blueprint(artists.router, url_prefix="/api")
app.register_blueprint(venues.router, url_prefix="/api")
app.register_blueprint(genres.router, url_prefix="/api")
app.register_blueprint(types.router, url_prefix="/api")
