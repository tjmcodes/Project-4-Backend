
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
            "location",
            "travel",
            "price",
            "websiteUrl",
            "videoUrl",
            "optionUrl",
            "musicUrl",
            "backgroundCardImage",
            "galleryImage1",
            "galleryImage2",
            "galleryImage3",
            "bio",
            "socialMediaUrl1",
            "socialMediaUrl2",
            "socialMediaUrl3",
            "created_at",
            "updated_at",)