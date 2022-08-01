from app import db
from models.base import BaseModel

class ArtistCommentModel(db.Model, BaseModel):

    __tablename__ = "artist_comments"

    content = db.Column(db.Text, nullable=False)

    # venue_id =db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)
    artist_a_id =db.Column(db.Integer, db.ForeignKey("artists.a_id"), nullable=False)
