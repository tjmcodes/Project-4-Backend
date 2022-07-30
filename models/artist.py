from datetime import datetime, timedelta

import jwt
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt
from models.base import BaseModel
from config.environment import secret

class ArtistModel(db.Model, BaseModel):

    __tablename__ = "artists"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    profileImage = db.Column(db.Text, nullable=False, unique=True)
    location = db.Column(db.Text, nullable=False, unique=False)
    travel = db.Column(db.Integer, nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, unique=False)
    websiteUrl = db.Column(db.Text, nullable=False, unique=False)
    videoUrl = db.Column(db.Text, nullable=False, unique=False)
    optionUrl = db.Column(db.Text, nullable=False, unique=True)
    musicUrl = db.Column(db.Text, nullable=False, unique=False)
    backgroundCardImage = db.Column(db.Text, nullable=False, unique=False)
    galleryImage1 = db.Column(db.Text, nullable=False, unique=False)
    galleryImage2 = db.Column(db.Text, nullable=False, unique=False)
    galleryImage3 = db.Column(db.Text, nullable=False, unique=False)
    bio = db.Column(db.Text, nullable=False, unique=False)
    socialMediaUrl1 = db.Column(db.Text, nullable=False, unique=False)
    socialMediaUrl2 = db.Column(db.Text, nullable=False, unique=False)
    socialMediaUrl3 = db.Column(db.Text, nullable=False, unique=False)
    
    # ! Password field to apply hash
    password_hash = db.Column(db.Text, nullable=True)

    @hybrid_property
    def password(self):
        print("passing the password function")
        pass

    # ! We then use this password function as a decorator. It'll get called by Flask SQLAlchemy when the model gets created, BEFORE saving to the DB.

    @password.setter
    def password(self, password_plaintext):
        print("inside password hash method")
        # ! Write our code to hash the password. It will give us back an encoded pw
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        # ! The decoded password, that we actually want to store.
        self.password_hash = encoded_pw.decode('utf-8')

    def validate_password(self, plaintext_password):   
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)

    def generate_token(self):
        payload = {
            # timedelta(days=1) --> you can change this to do different amount
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": self.id,
        }
    
        # Get the token
        token = jwt.encode(
            payload, 
            secret, 
            algorithm="HS256", # keywords after the 2 positional arguments
        )


        return token

