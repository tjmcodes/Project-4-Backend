from http import HTTPStatus
from operator import imod

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from serialisers.venue import VenueSchema
from serialisers.venue_types import TypeSchema
from models.types import TypeModel


Venue_schema = VenueSchema()
type_schema = TypeSchema()

router = Blueprint("types", __name__)

@router.route("/types", methods=["POST"])
def post_genres():
    type_dictionary = request.json

    try:
        genre = type_schema.load(type_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "validation error"}

    genre.save()

    return type_schema.jsonify(genre), HTTPStatus.CREATED


@router.route("type/<int:type_id>", methods=["DELETE"])
def remove_genre(type_id):
    type = TypeModel.query.get(type_id)

    if not type:
        return { "message": "no venue type" }, HTTPStatus.NOT_FOUND

    type.remove()

    return '', HTTPStatus.NO_CONTENT
