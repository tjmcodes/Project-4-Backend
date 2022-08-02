# from app import db
# # from models.base import BaseModel
# from models.venue import VenueModel

# class VenueCommentModel(db.Model, VenueModel):

#     __tablename__ = "venue_comments"

#     content = db.Column(db.Text, nullable=False)

#     venue_id =db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)