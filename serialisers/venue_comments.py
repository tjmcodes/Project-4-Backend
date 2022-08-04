from marshmallow import fields
from app import ma
from models.venue_comments import VenueCommentModel
# from serialisers.venue_populate import VenuePopulateSchema


class VenueCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = VenueCommentModel
        load_instance = True
        include_fk = True

    venuePopulate = fields.Nested("VenuePopulateSchema")

    