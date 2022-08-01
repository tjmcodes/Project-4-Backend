from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request
from models.venue import VenueModel
from serialisers.venue import VenueSchema


venue_schema = VenueSchema()

router = Blueprint("users", __name__)

@router.route('/venue-signup', methods=["POST"])
def register():
    try:
        user_dictionary = request.json
        user = venue_schema.load(user_dictionary)
        user.save()
        return venue_schema.jsonify(user)
    except ValidationError as e:
        print(e)
        return {"errors": e.messages, "messages": "Something went wrong"}
    except Exception as e:
        print(e)
        return { "messages": "Something went wrong" }


@router.route('/venue-login', methods=["POST"])
def login():
    try:
        credentials_dictionary = request.json
        user = VenueModel.query.filter_by(email=credentials_dictionary["email"]).first()
        if not user:
            return {"message": "No Registered user with this email, please re-enter email"}
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorized"}, HTTPStatus.UNAUTHORIZED
        token = user.generate_token()
        return {"token": token, "message": "Welcome back!"}
    except Exception as e:
        return {"messages": "Something went wrong" }


@router.route("/allvenues", methods=["GET"])
def get_teas():
    teas = VenueModel.query.all()

    return venue_schema.jsonify(teas, many=True), HTTPStatus.OK


@router.route("/allvenues/<int:venue_id>", methods=["GET"])
def get_single_tea(tea_id):

    tea = VenueModel.query.get(tea_id)

    if not tea:
        return {"message": "venue not found"}, HTTPStatus.NOT_FOUND

    return venue_schema.jsonify(tea), HTTPStatus.OK