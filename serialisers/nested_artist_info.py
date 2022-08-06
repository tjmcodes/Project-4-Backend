from marshmallow import fields
from app import ma

from models.artist import ArtistModel


class NestedArtistInfoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ArtistModel

        load_instance = True

        exclude = ("password_hash",)
        load_only = ('email', 'password')

    # comments = fields.Nested("ArtistCommentSchema", many=True) # nests comments posted by venue to artist
    # genre = fields.Nested("GenreSchema", many=True)
    # password = fields.String(required=True)