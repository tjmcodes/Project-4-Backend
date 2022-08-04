from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from models.venue import VenueModel
from serialisers.venue import VenueSchema
from middleware.artist_secure_route import artist_secure_route
from middleware.venue_secure_route import venue_secure_route
from serialisers.venue_comments import VenueCommentSchema
# from serialisers.artist_comments import ArtistCommentSchema

venue_schema = VenueSchema()
venue_comments_schema = VenueCommentSchema()
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


@router.route("/venues", methods=["GET"])
def get_teas():
    venues = VenueModel.query.all()

    return venue_schema.jsonify(venues, many=True), HTTPStatus.OK


@router.route("/venues/<int:venue_id>", methods=["GET"])
def get_single_venue(venue_id):

    venue = VenueModel.query.get(venue_id)

    if not venue:
        return {"message": "venue not found"}, HTTPStatus.NOT_FOUND

    return venue_schema.jsonify(venue), HTTPStatus.OK



# !  P O S T  A  C O M M E N T  B Y  I D
@router.route("/venues/<int:venue_id>/comments", methods=["POST"])
@artist_secure_route # only registered and logged in Artists can make request
def create_comment(venue_id):

    comment_dictionary = request.json
    comment_dictionary["artist_id"] = g.current_user.id
    comment_dictionary["venue_id"] = venue_id
    print(comment_dictionary)


    try:
        comment = venue_comments_schema.load(comment_dictionary)
        print(comment)
    except ValidationError as e:
    
        return { "errors": e.messages, "message": "There is no such artist"}, HTTPStatus.NO_CONTENT

    comment.save()
    print(type(comment))
    return venue_comments_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/venues/<int:venue_id>", methods=["PUT"])
@venue_secure_route
def update_venueinfo(venue_id):
    venue_dictionary = request.json
    existing_venue = VenueModel.query.get(venue_id)

    if not existing_venue:
        return {"message": "No Venue with ID"}, HTTPStatus.NOT_FOUND

    # ! Add this check whenever we want to make sure the tea is the user's tea that they're trying to update/delete
    if not g.current_user.id == existing_venue.venue_id:
        return {"message": "No permission to edit"}, HTTPStatus.UNAUTHORIZED

    try:
        venue = venue_schema.load(venue_dictionary, instance=existing_venue, partial=True)

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    venue.save()

    return venue_schema.jsonify(venue), HTTPStatus.OK

    
