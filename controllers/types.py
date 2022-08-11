from http import HTTPStatus
from operator import imod

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from serialisers.venue import VenueSchema
from serialisers.venue_types import TypeSchema
from models.types import TypeModel
from models.venue import VenueModel
from middleware.venue_secure_route import venue_secure_route



NOT_FOUND = 404
STATUS_CREATED = 201
UNAUTHORIZED = 401
NO_CONTENT = 204
OK = 200
CREATED = 201

Venue_schema = VenueSchema()
type_schema = TypeSchema()

router = Blueprint("types", __name__)

@router.route("/types", methods=["POST"])
def post_genres():
    type_dictionary = request.json

    try:
        type = type_schema.load(type_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "validation error"}

    type.save()

    return type_schema.jsonify(type), HTTPStatus.CREATED


@router.route("type/<int:type_id>", methods=["DELETE"])
def remove_genre(type_id):
    type = TypeModel.query.get(type_id)

    if not type:
        return { "message": "no venue type" }, HTTPStatus.NOT_FOUND

    type.remove()

    return '', HTTPStatus.NO_CONTENT



@router.route("/venues/<int:venue_id>/type/<int:type_id>", methods=["POST"])
@venue_secure_route
def create_tea_note(venue_id, type_id):

    venue = VenueModel.query.get(venue_id)

    type = TypeModel.query.get(type_id)

    if not type or not venue:
        return {"message": "Item not found"}, HTTPStatus.NOT_FOUND

    venue.notes.append(type)

    venue.save()

    return Venue_schema.jsonify(venue), HTTPStatus.OK