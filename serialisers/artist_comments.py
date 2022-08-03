from marshmallow import fields
from app import ma
from models.artist_comments import ArtistCommentModel
from serialisers.venue import VenueSchema

class ArtistCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ArtistCommentModel
        load_instance = True

        include_fk = True

    user = fields.Nested("VenueSchema", many=True)
