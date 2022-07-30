# from marshmallow import fields
from app import ma

from models.artist import ArtistModel

class ArtistSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ArtistModel

        load_instance = True

    # comments = fields.Nested("CommentSchema", many=True)

    # preparation = fields.Nested("PreparationSchema", many=True)
