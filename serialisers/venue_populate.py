from marshmallow import fields
from models.venue import VenueModel
from app import ma



class VenueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VenueModel
        load_instance = True

        exclude = # exclude the fields you don't want to use here.
        load_only = ('email', 'password')

    password = fields.String(required=True)