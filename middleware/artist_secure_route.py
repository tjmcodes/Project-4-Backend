from http import HTTPStatus
from functools import wraps
import jwt
from flask import request, g
from models.artist import ArtistModel
from config.environment import secret


def artist_secure_route(route_function):

    @wraps(route_function)
    def decorated_function(*args, **kwargs):

        raw_token = request.headers.get("Authorization")

        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.Unauthorized

        clean_token = raw_token.replace("Bearer ", "")
        
        try:
            payload = jwt.decode(clean_token, secret, "HS256")
            #remember to import the secret from config > environment

            artist_id = payload["sub"]

            artist = ArtistModel.query.get(artist_id)

            if not artist:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

            g.current_user = artist

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e: 
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


        return route_function(*args, **kwargs)

    return decorated_function