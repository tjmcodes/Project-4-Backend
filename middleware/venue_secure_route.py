from http import HTTPStatus
from functools import wraps
import jwt
from flask import request, g
from models.venue import VenueModel
from config.environment import secret


def venue_secure_route(route_function):

    @wraps(route_function)
    def decorated_function(*args, **kwargs):

        raw_token = request.headers.get("Authorization")

        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.Unauthorized

        clean_token = raw_token.replace("Bearer ", "")
        
        try:
            payload = jwt.decode(clean_token, secret, "HS256")
            #remember to import the secret from config > environment

            venue_idv = payload["sub"]

            venue = VenueModel.query.get(venue_idv)

            if not venue:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

            g.current_user = venue

        except jwt.ExpiredSignatureError: 
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e: 
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


        return route_function(*args, **kwargs)

    return decorated_function