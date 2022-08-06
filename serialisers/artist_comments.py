from marshmallow import fields
from app import ma
from models.artist_comments import ArtistCommentModel
from serialisers.nested_venue_info import NestedVenueInfoSchema

class ArtistCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ArtistCommentModel
        load_instance = True

        include_fk = True



    venue = fields.Nested("NestedVenueInfoSchema")
    # venue = fields.Nested("VenueSchema") # nests venue schema in the artist comments. Also links to relationship in artist comment model table. 
