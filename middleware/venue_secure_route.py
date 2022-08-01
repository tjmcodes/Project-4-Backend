from http import HTTPStatus

import jwt
from functools import wraps
from flask import request, g
from models.artist import ArtistModel
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

            venue_id = payload["sub"]

            venue = ArtistModel.query.get(venue_id)

            if not venue:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

            g.current_user = venue

        except jwt.ExpiredSignatureError: 
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e: 
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


        return route_function(*args, **kwargs)

    return decorated_function