from app import db
from models.base import BaseModel
from models.artist import ArtistModel

class VenueCommentModel(db.Model, BaseModel):

    __tablename__ = "venue_comments"

    content = db.Column(db.Text, nullable=False)
    artist_id =db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    venue_id =db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)
    # artist=db.relationship("ArtistModel", backref="artist")
    