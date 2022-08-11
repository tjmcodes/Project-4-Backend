from datetime import datetime, timedelta
import jwt
from sqlalchemy.ext.hybrid import hybrid_property
from app import db , bcrypt
from models.base import BaseModel
from config.environment import secret
from models.venue_comments import VenueCommentModel
from models.types import TypeModel
from models.venue_types import venue_type

class VenueModel(db.Model, BaseModel):

    __tablename__ = "venues"
    
    # id = db.Column(db.Integer, nullable=False, primary_key=True)
    # created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    email = db.Column(db.Text, nullable=False, unique=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    profileImage = db.Column(db.Text, nullable=False, unique=False)
    title = db.Column(db.Text, nullable=False, unique=False)
    role = db.Column(db.Text, nullable=False, unique=False)

# U S E  T H I S  M O D E L: D E P L O Y  
    # venueName = db.Column(db.Text, nullable=False, unique=True)
    # type = db.Column(db.Text, nullable=True, unique=False)
    # # venueImage = db.Column(db.Text, nullable=False, unique=True)
    # location = db.Column(db.Text, nullable=False, unique=False)
    # address = db.Column(db.Text, nullable=False, unique=True)
    # budget = db.Column(db.Integer, nullable=False, unique=False)
    # websiteUrl = db.Column(db.Text, nullable=False, unique=True)
    # # videoUrl = db.Column(db.Text, nullable=True, unique=False)
    # # optionUrl = db.Column(db.Text, nullable=True, unique=False)
    # backgroundCardImage = db.Column(db.Text, nullable=False, unique=False)
    # galleryImage1 = db.Column(db.Text, nullable=False, unique=False)
    # galleryImage2 = db.Column(db.Text, nullable=True, unique=False)
    # galleryImage3 = db.Column(db.Text, nullable=True, unique=False)
    # description = db.Column(db.Text, nullable=False, unique=True)
    # fbUrl = db.Column(db.Text, nullable=True, unique=False)
    # twitterUrl = db.Column(db.Text, nullable=True, unique=False)
    # youTubeUrl = db.Column(db.Text, nullable=True, unique=False)
    # instagramUrl = db.Column(db.Text, nullable=True, unique=False)

# U S E  T H I S  M O D E L: Q U I C K  P O S T
    venueName = db.Column(db.Text, nullable=True, unique=True)
    type = db.Column(db.Text, nullable=True, unique=False)
    # venueImage = db.Column(db.Text, nullable=False, unique=True)
    location = db.Column(db.Text, nullable=True, unique=False)
    address = db.Column(db.Text, nullable=True, unique=True)
    budget = db.Column(db.Integer, nullable=True, unique=False)
    websiteUrl = db.Column(db.Text, nullable=True, unique=True)
    # videoUrl = db.Column(db.Text, nullable=True, unique=False)
    # optionUrl = db.Column(db.Text, nullable=True, unique=False)
    backgroundCardImage = db.Column(db.Text, nullable=True, unique=False)
    galleryImage1 = db.Column(db.Text, nullable=True, unique=False)
    galleryImage2 = db.Column(db.Text, nullable=True, unique=False)
    galleryImage3 = db.Column(db.Text, nullable=True, unique=False)
    description = db.Column(db.Text, nullable=True, unique=True)
    fbUrl = db.Column(db.Text, nullable=True, unique=False)
    twitterUrl = db.Column(db.Text, nullable=True, unique=False)
    youTubeUrl = db.Column(db.Text, nullable=True, unique=False)
    instagramUrl = db.Column(db.Text, nullable=True, unique=False)

    comments = db.relationship('VenueCommentModel', backref='venue_comments', cascade="all, delete")
    type = db.relationship('TypeModel', backref='type_venue', secondary=venue_type)

    password_hash = db.Column(db.Text, nullable=True)
    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self,password_plaintext):
        print("inside venue password hash method")
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
