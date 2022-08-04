from marshmallow import fields
from app import ma

from models.venue import VenueModel
from serialisers.artist_comments import ArtistCommentSchema
from serialisers.venue_types import TypeSchema


class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VenueModel
        load_instance = True

        exclude = ("password_hash",)
        load_only = ('email', 'password')

    comments = fields.Nested("ArtistCommentSchema", many=True)
    password = fields.String(required=True)
    type = fields.Nested("TypeSchema", many=True)
