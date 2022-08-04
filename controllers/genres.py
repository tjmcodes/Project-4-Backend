from http import HTTPStatus

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from serialisers.artist import ArtistSchema
from serialisers.artist_genres import GenreSchema
from models.genres import GenreModel
from middleware.artist_secure_route import artist_secure_route
from models.artist import ArtistModel


artist_schema = ArtistSchema()
genre_schema = GenreSchema()

router = Blueprint("genres", __name__)

# !  P O S T I N G  G E N R E  T Y P E 
@router.route("/genres", methods=["POST"])
def post_genres():
    genre_dictionary = request.json

    try:
        genre = genre_schema.load(genre_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong"}

    genre.save()

    return genre_schema.jsonify(genre), HTTPStatus.CREATED


# !  D E L E T E  G E N R E  B Y  I D  T O  A R T I S T  B Y  I D
@router.route("genres/<int:genre_id>", methods=["DELETE"])
def remove_genre(genre_id):
    genre = GenreModel.query.get(genre_id)

    if not genre:
        return { "message": "No preparation type was found" }, HTTPStatus.NOT_FOUND

    genre.remove()

    return '', HTTPStatus.NO_CONTENT

# !  P O S T  A  G E N R E  B Y  I D  T O  A R T I S T  B Y  I D
@router.route("/artists/<int:artist_id>/genres/<int:genre_id>", methods=["POST"])
@artist_secure_route
def create_artist_genre(artist_id, genre_id):

    artist = ArtistModel.query.get(artist_id)

    genre = GenreModel.query.get(genre_id)

    if not artist or not genre:
        return {"message": "Artist not found"}, HTTPStatus.NOT_FOUND

    artist.genre.append(genre)

    artist.save()

    return artist_schema.jsonify(artist), HTTPStatus.OK
