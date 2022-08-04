
from app import ma
from models.types import TypeModel

class TypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeModel
        load_instance = True

