from marshmallow import fields
from app import ma

from models.artist import ArtistModel
# from serialisers.venue_comments import VenueCommentSchema


class VenuePopulateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = ArtistModel
        load_instance = True

        # exclude = ("password_hash", "location")
        # load_only = ('email', 'password')
    
    comments = fields.Nested("VenueCommentSchema", many=True)
    password = fields.String(required=True)
    type = fields.Nested("TypeSchema", many=True)