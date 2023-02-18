from app import ma 
from models.admin import AdminModel
from marshmallow import fields

class AdminSchema(ma.SQLAlchemyAutoSchema): 

    # add a password field so that I can serialize it
    password = fields.String(required=True)
      
    class Meta:
        model = AdminModel
        exclude = ("password_hash",)
        load_only = ("username", "password")
