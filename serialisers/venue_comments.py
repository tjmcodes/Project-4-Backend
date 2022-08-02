from app import ma
from models.venue_comments import VenueCommentModel

class VenueCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = VenueCommentModel
        load_instance = True
         
        include_fk = True