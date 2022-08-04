from marshmallow import fields
from app import ma
from models.artist_comments import ArtistCommentModel
# from serialisers.venue_populate import VenuePopulateSchema

class ArtistCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ArtistCommentModel
        load_instance = True

        include_fk = True

    # venuePopulate = fields.Nested("VenuePopulateSchema")
    venue = fields.Nested("VenueSchema")
