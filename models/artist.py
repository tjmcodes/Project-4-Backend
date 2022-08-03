from datetime import datetime, timedelta

import jwt
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt
from models.base import BaseModel
from config.environment import secret
from models.artist_comments import ArtistCommentModel
from models.genres import GenreModel
from models.artist_genres import artist_genre


class ArtistModel(db.Model, BaseModel):

    __tablename__ = "artists"

    # ida = db.Column(db.Integer, nullable=False, primary_key=True)
    # created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    
    artistName = db.Column(db.Text, nullable=False, unique=False)
    profileImage = db.Column(db.Text, nullable=False, unique=False)
    genre = db.Column(db.Text, nullable=False, unique=False)
    location = db.Column(db.Text, nullable=False, unique=False)
    travel = db.Column(db.Integer, nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False)
    websiteUrl = db.Column(db.Text, nullable=False, unique=True)
    videoUrl = db.Column(db.Text, nullable=False, unique=True)
    optionUrl = db.Column(db.Text, nullable=True, unique=True)
    musicUrl = db.Column(db.Text, nullable=False, unique=True)
    backgroundCardImage = db.Column(db.Text, nullable=False, unique=False)
    galleryImage1 = db.Column(db.Text, nullable=False, unique=False)
    galleryImage2 = db.Column(db.Text, nullable=True, unique=False)
    galleryImage3 = db.Column(db.Text, nullable=True, unique=False)
    bio = db.Column(db.Text, nullable=False, unique=True)
    socialMediaUrl1 = db.Column(db.Text, nullable=False, unique=True)
    socialMediaUrl2 = db.Column(db.Text, nullable=True, unique=True)
    socialMediaUrl3 = db.Column(db.Text, nullable=True, unique=True)

    genre = db.relationship('GenreModel', backref='genre_type', secondary=artist_genre)
    comments = db.relationship('ArtistCommentModel', backref='artist_comments', cascade="all, delete")


    # ! Password field to apply hash
    password_hash = db.Column(db.Text, nullable=True)

    @hybrid_property
    def password(self):
        pass

    # ! We then use this password function as a decorator. It'll get called by Flask SQLAlchemy when the model gets created, BEFORE saving to the DB.

    @password.setter
    def password(self, password_plaintext):
        print("inside artist password hash method")
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

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    
    # def update(self, coffee):
    #     db.session.add(coffee)
    #     db.session.commit()

    # def remove(self):
    #     db.session.delete(self)
    #     db.session.commit()

