# from marshmallow import fields
from app import ma
from models.venue_comments import VenueCommentModel
# from serialisers.artist import ArtistSchema


class VenueCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = VenueCommentModel
        load_instance = True
        include_fk = True

    # user = fields.Nested("ArtistSchema", many=True)