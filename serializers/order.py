from app import ma 
from models.order import OrderModel
from marshmallow import fields

class OrderSchema(ma.SQLAlchemyAutoSchema):

    order_lines = fields.Nested("OrderLineSchema", many=True)

    class Meta: 
        model = OrderModel
        load_instance = True
        include_fk = True