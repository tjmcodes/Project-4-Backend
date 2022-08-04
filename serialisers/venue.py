from marshmallow import fields
from models.venue import VenueModel
from serialisers.venue_types import TypeSchema
from app import ma



class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VenueModel
        load_instance = True

        exclude = ("password_hash",)
        load_only = ('email', 'password')

    password = fields.String(required=True)
    type = fields.Nested("TypeSchema", many=True)