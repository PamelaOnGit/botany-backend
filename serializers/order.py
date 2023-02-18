from app import ma 
from models.order import OrderModel
from marshmallow import fields

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = OrderModel
        load_instance = True
        include_fk = True