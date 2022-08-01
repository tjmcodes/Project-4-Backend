from app import db
from models.base import BaseModel

class VenueCommentModel(db.Model, BaseModel):

    __tablename__ = "venue_comments"

    content = db.Column(db.Text, nullable=False)

    artists_id =db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)