from marshmallow import fields
from app import ma

from models.artist import ArtistModel

class ArtistSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ArtistModel

        load_instance = True

        exclude = ("password_hash",)
        load_only = ('email', 'password')

    user = fields.Nested("ArtistSchema", many=True)
    password = fields.String(required=True)
