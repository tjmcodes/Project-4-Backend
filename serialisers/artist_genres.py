from app import ma
from models.genres import GenreModel

class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GenreModel
        load_instance = True
