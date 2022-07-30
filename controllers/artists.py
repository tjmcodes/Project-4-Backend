from http import HTTPStatus

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from models.artist import ArtistModel
from serialisers.artist import ArtistSchema
from middleware.secure_route import secure_route

artist_schema = ArtistSchema()

router = Blueprint("artists", __name__)

@router.route('/artist-signup', methods=["POST"])
def register():
    try:
        artist_dictionary = request.json
        artist = artist_schema.load(artist_dictionary)
        artist.save()
        return artist_schema.jsonify(artist)
    
    # ! Specific error
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    # ! General error
    except Exception as e:
        return { "messages": "Something went wrong" }
  
@router.route('/artist-login', methods=["POST"])
def login():
    try:
        credentials_dictionary = request.json

        #get user by email (from postgresql)
        artist = ArtistModel.query.filter_by(email=credentials_dictionary["email"]).first()

        if not artist:
            return { "message": "No user found for this email" }

        if not artist.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorized"}, HTTPStatus.UNAUTHORIZED

        token = artist.generate_token()

        return { "token": token, "message": "Welcome Back!" }

    except Exception as e: 
        return { "messages": "Something went wrong" }

# ! G E T  A L L  A R T I S T S
@router.route("/artists", methods=["GET"])
def get_artists():
    artist = ArtistModel.query.all() # query is an object that lives on model and has methods like .all to interface with SQLAlchemy.
    print(type(artist_schema))
    print(type(artist))
    return artist_schema.jsonify(artist, many=True)


# ! G E T  A R T I S T S  B Y  I D
@router.route("/artists/<int:artists_id>", methods=["GET"])
def get_single_artist(artists_id):

    artist = ArtistModel.query.get(artists_id)

    if not artist:

        return { "message": "Coffee not found" }, HTTPStatus.NOT_FOUND

    return artist_schema.jsonify(artist)