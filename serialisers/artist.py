from marshmallow import fields
from app import ma

from models.artist import ArtistModel


class ArtistSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ArtistModel

        load_instance = True

        exclude = ("password_hash",)
        load_only = ('email', 'password')
    
    comments = fields.Nested("VenueCommentSchema", many=True)
    password = fields.String(required=True)

