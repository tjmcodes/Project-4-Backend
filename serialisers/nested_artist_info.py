
from app import ma

from models.artist import ArtistModel


class NestedArtistInfoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ArtistModel

        load_instance = True

        exclude = ("password_hash",
            "password_hash",
            "username",
            "email",
            "genre",
            "willingToTravel",
            "location",
            "travel",
            "price",
            "websiteUrl",
            "videoUrl",
            "musicUrl",
            "backgroundCardImage",
            "galleryImage1",
            "galleryImage2",
            "galleryImage3",
            "bio",
            "fbUrl",
            "twitterUrl",
            "youTubeUrl",
            "instagramUrl",
            "created_at",
            "updated_at",)