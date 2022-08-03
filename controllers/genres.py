from http import HTTPStatus

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from serialisers.artist import ArtistSchema
from serialisers.artist_genres import GenreSchema
from models.genres import GenreModel


artist_schema = ArtistSchema()
genre_schema = GenreSchema()

router = Blueprint("genres", __name__)

@router.route("/genres", methods=["POST"])
def post_genres():
    genre_dictionary = request.json

    try:
        genre = genre_schema.load(genre_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong"}

    genre.save()

    return genre_schema.jsonify(genre), HTTPStatus.CREATED


@router.route("genres/<int:genre_id>", methods=["DELETE"])
def remove_genre(genre_id):
    genre = GenreModel.query.get(genre_id)

    if not genre:
        return { "message": "No preparation type was found" }, HTTPStatus.NOT_FOUND

    genre.remove()

    return '', HTTPStatus.NO_CONTENT
