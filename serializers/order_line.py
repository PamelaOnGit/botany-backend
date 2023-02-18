from app import ma 
from models.order_line import OrderLineModel
# from marshmallow import fields

class OrderLineSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = OrderLineModel
        load_instance = True
        include_fk = True