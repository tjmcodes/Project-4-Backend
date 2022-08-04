from app import db
from models.base import BaseModel
from models.venue import VenueModel

class ArtistCommentModel(db.Model, BaseModel):

    __tablename__ = "artist_comments"

    content = db.Column(db.Text, nullable=False)
    venue_id =db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)
    artist_id =db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False) 
    venue = db.relationship('VenueModel', backref='venue')