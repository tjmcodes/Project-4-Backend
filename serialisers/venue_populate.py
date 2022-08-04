# from marshmallow import fields
from app import ma

from models.venue import VenueModel
# from serialisers.venue_comments import VenueCommentSchema


class VenuePopulateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = VenueModel
        load_instance = True

        # exclude = ("password_hash", "location")
        # load_only = ('email', 'password')
    