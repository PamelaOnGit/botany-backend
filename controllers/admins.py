from flask import Blueprint, request

from models.admin import AdminModel
from serializers.admin import AdminSchema


admin_schema = AdminSchema()

router = Blueprint("admins", __name__)

@router.route('/login', methods=["POST"])
def login():
    # user provides a username and password
    admin_dictionary = request.json
    # check if the user exists
    admin = AdminModel.query.filter_by(username=admin_dictionary["username"]).first()
    if not admin: 
        return { "message": "username or password was incorrect"}
    # validate password against database
    if not admin.validate_password(admin_dictionary["password"]):
        return { "message": "username or password was incorrect"}        
    # make a token and send it back
    token = admin.generate_token()
    return { "token" : token, "message":"Welcome back!"}