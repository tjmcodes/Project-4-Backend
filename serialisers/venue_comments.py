from marshmallow import fields
from app import ma
from models.venue_comments import VenueCommentModel
from serialisers.nested_artist_info import NestedArtistInfoSchema


class VenueCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = VenueCommentModel
        load_instance = True
        include_fk = True

    artist = fields.Nested("NestedArtistInfoSchema")
    # venuePopulate = fields.Nested("VenuePopulateSchema")
    
