from app import ma
from models.artist_comments import ArtistCommentModel

class ArtistCommentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ArtistCommentModel
        load_instance = True

        include_fk = True
