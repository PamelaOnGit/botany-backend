from functools import wraps
from http import HTTPStatus
from http.client import UNAUTHORIZED
from flask import request, g
import jwt
from models.admin import AdminModel


from config.environment import secret


def secure_route(func): 
    @wraps(func)
    def wrapper(*args, **kwargs): 
        
        # extract token
        # check it is valid
        # call function to pass through to create etc

        raw_token = request.headers.get('Authorization')
        if not raw_token: 
            return { "message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        clean_token = raw_token.replace("Bearer ", "")
        try:
          # This stuff has to match the stuff we attached in... 
            payload = jwt.decode(
              clean_token, 
              secret, 
              "HS256"
            )
            # get the admin id from the token (called 'sub')
            admin_id = payload['sub']
            admin = AdminModel.query.get(admin_id)
            if not admin: 
                return { "message": "unauthorized" }, HTTPStatus.unauthorized
            # at this point, we know that the admin is authorized
        except jwt.ExpiredSignatureError: 
            return { "message": "unauthorized"}
        except Exception: 
            return { "message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

        return func(*args, **kwargs)
    
    return wrapper

