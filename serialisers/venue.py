# from marshmallow import fields
from models.venue import VenueModel
from app import ma



class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VenueModel
        load_instance = True